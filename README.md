# Moving Target Defense

A project implementing Moving Target Defense (MTD) strategies using Docker and Python to enhance network security.

## Installation

### Prerequisites
Ensure you have **Python** and **Docker** installed.

#### Python
Install Python:

pip install python

#### Docker
Install Docker by following instructions at Docker's official site.

Download the Files

Open a terminal and navigate to the folder containing the files.

use command to navigate to the file "cd <file_path>"

#### Docker Setup

Build the Docker Image

Run the following command to build the Docker image:
```
docker build -t "your_image_name" . 
``` 
Verify the image build:
```
docker images
```
Run the Docker Image

To start the Docker container, use:
```
docker run "your_image_name"
```
If the above command doesn’t work, try running it with elevated privileges:
```
docker run --privileged -it "your_image_name"
```
Access the Running Container

Open another terminal.

List running containers to find the container ID and port:
```
docker ps
```
Use the container port to enter the running container:
```
docker exec -it "container_id" /bin/bash
```
Once you went inside, you can check for files with:
```
ls
```
you can see the MTD.py file.

come back again using command [cd] to the rrot

Check IP Changing

To verify IP changes within the container:

we need to still inside the container port, use:
```
ip addr
```
or
```
ifconfig
```
This will display IP information and confirm that IP changes are occurring as expected with MTD.

Testing: 
open another Terminal and get into the runing conatiner and use ping command to see the ip changing
```
ping <ip address> -s 6500
```
install nmap 
and get into the nmap locationa and open a terminal where nmap is setup in the system and try for it otherwise it will give error
try to scan using nmap and see the result 
```
nmap <ip address> 
```
