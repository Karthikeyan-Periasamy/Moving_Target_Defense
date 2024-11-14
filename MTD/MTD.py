import socket
import fcntl
import struct
import time
import threading
import subprocess
import random
import re

# ThreatDetection class from threat_detection.py
class ThreatDetection:
    def __init__(self, packet_threshold=100):
        self.packet_threshold = packet_threshold

    def count_packets(self, interface, duration=3):
        try:
            command = f"timeout {duration} tcpdump -i {interface}"
            process = subprocess.run(command, shell=True, capture_output=True, text=True)
            output = process.stderr
            packet_count = re.search(r"(\d+) packets received by filter", output)
            packet_count = int(packet_count.group(1)) if packet_count else 0
            print(f"Detected {packet_count} packets")
            return packet_count
        except Exception as e:
            print(f" count_packets: Error occurred: {e}")
            return 0

    def detect_threat(self, packet_count):
        if packet_count > self.packet_threshold * 2:
            print("Threat Level: HIGH - Possible DDoS or major threat detected.")
            return "high"
        elif packet_count > self.packet_threshold:
            print("Threat Level: MEDIUM - Potential reconnaissance or moderate threat detected.")
            return "medium"
        elif packet_count > 0:
            print("Threat Level: LOW - Low-level threat detected.")
            return "low"
        return None

    def monitor_interface(self, interface, check_interval=5):
        while True:
            packet_count = self.count_packets(interface, duration=check_interval)
            threat_level = self.detect_threat(packet_count)
            if threat_level:
                print(f"ThreatDetection - monitor_interface: {threat_level.upper()} ")
            time.sleep(check_interval)


# IPShuffler class from ip_shuffler.py
class IPShuffler:
    def __init__(self, mask, interface):
        self.interface = interface
        self.mask = mask
        self.baseIp = self.get_base_ip()
        self.current_ip = self.generate_ip()
        self.gateway = self.baseIp  # Set the initial gateway to the interface's base IP

    def get_base_ip(self):
        """Fetch the base IP of the specified interface dynamically."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            base_ip = socket.inet_ntoa(fcntl.ioctl(
                sock.fileno(),
                0x8915,  # SIOCGIFADDR
                struct.pack('256s', self.interface[:15].encode('utf-8'))
            )[20:24])
            print(f"get_base_ip: Retrieved base IP ***.**.*.****")
            return base_ip
        except Exception as e:
            print(f"get_base_ip: Error occurred: {e}")
            return None

    def generate_ip(self):
        """Generate a new IP based on the current base IP dynamically."""
        base_octets = self.baseIp.split('.')[:3]
        random_octet = str(random.randint(1, 254))
        return f"{'.'.join(base_octets)}.{random_octet}/{self.mask}"

    def check_ip_availability(self, ip):
        try:
            result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.returncode == 0
        except Exception as e:
            print(f"check_ip_availability: Error occurred: {e}")
            return False

    def change_ip(self, new_ip):
        """Change IP and set the gateway to match the current interface IP."""
        try:
            self.gateway = self.baseIp  # Update gateway to the interface's current base IP
            subprocess.run(['ip', 'link', 'set', self.interface, 'down'], check=True)
            subprocess.run(['ip', 'addr', 'flush', 'dev', self.interface], check=True)
            subprocess.run(['ip', 'addr', 'add', new_ip, 'dev', self.interface], check=True)
            subprocess.run(['ip', 'link', 'set', self.interface, 'up'], check=True)
            subprocess.run(['ip', 'route', 'add', 'default', 'via', self.gateway], check=True)
            print(f"change_ip: IP address changed to {new_ip} ")
        except Exception as e:
            print(f"IPShuffler - change_ip: Error occurred: {e}")

    def adaptive_shuffling(self, threat_level):
        if threat_level == "high":
            self.perform_ip_change()
            print("High threat detected! Immediate IP shuffle.")

    def perform_ip_change(self):
        new_ip = self.generate_ip()
        if not self.check_ip_availability(new_ip.split('/')[0]):
            self.change_ip(new_ip)
        else:
            print("IPShuffler - perform_ip_change: IP address conflict during change")


# Main function to run the MTD system (from main.py)
def main(interface, mask, changeIpPeriod, threshold):
    shuffler = IPShuffler(mask, interface)
    detector = ThreatDetection(threshold)

    def routine_ip_change():
        while True:
            time.sleep(changeIpPeriod)
            print("Performing routine IP change")
            shuffler.perform_ip_change()

    threading.Thread(target=routine_ip_change, daemon=True).start()

    while True:
        packet_count = detector.count_packets(interface)
        print(f"Monitoring traffic, packet count = {packet_count}")
        threat_level = detector.detect_threat(packet_count)
        if threat_level:
            print(f"Detected {threat_level} threat level, adapting IP shuffling")
            shuffler.adaptive_shuffling(threat_level)
        time.sleep(1)


################ Parameters ############################
interface = 'eth0'         # Interface to apply MTD
mask = '24'                # Network mask
changeIpPeriod = 20         # Routine IP changing period in seconds
threshold = 18            # Packet threshold for detecting threats
########################################################

main(interface, mask, changeIpPeriod, threshold)
