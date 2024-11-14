# Use Ubuntu as the base image
FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip tcpdump iproute2 iputils-ping net-tools curl wget nano

# Set the working directory
WORKDIR /app
# Copy the Python scripts into the container
COPY MTD.py /app/MTD.py

# Install any Python dependencies if required
# RUN pip3 install -r requirements.txt   # Uncomment if you have requirements

# Specify the entry point to run the main script
CMD ["python3", "MTD.py"]
