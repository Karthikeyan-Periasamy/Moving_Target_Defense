# Moving Target Defense

A project implementing Moving Target Defense (MTD) strategies using Docker and Python to enhance network security. This setup allows for dynamic IP changing, simulating an environment with improved resilience against attacks.

## Installation

### Prerequisites
Ensure you have **Python** and **Docker** installed.

#### Python
Install Python:
```bash
pip install python
Docker
Install Docker by following instructions at Docker's official site.

Download the Files
Clone or download this repository.
Open a terminal and navigate to the folder containing the files.
Docker Setup
Build the Docker Image
Run the following command to build the Docker image:

bash
Copy code
docker build -t "your_image_name" .
Verify the image build:

bash
Copy code
docker images
Run the Docker Image
To start the Docker container, use:

bash
Copy code
docker run "your_image_name"
If the above command doesn’t work, try running it with elevated privileges:

bash
Copy code
docker run --privileged -it "your_image_name"
Access the Running Container
Open another terminal.

List running containers to find the container ID and port:

bash
Copy code
docker ps
Use the container port to enter the container:

bash
Copy code
docker exec -it "container_id" /bin/bash
Once inside, you can check for files with:

bash
Copy code
ls
Look for the MTD.py file.

Check IP Changing
To verify IP changes within the container:

While still inside the container, use:
bash
Copy code
ip addr
or
bash
Copy code
ifconfig
This will display IP information and confirm that IP changes are occurring as expected with MTD.

# Moving_Target_Defense

## Installation 
### python
pip install python 
### Docker 
install Docker 

## Download the files from github 
Download the Files 
Open the Terminal & Naviagte to Folder 
run the Docker Commands
## Docker Commands
docker build -t "name" .

Check For the image build 
docker images 

## Run the image
docker run "name" 

if it not runing try the other command 
docker run --privileged -it "name"

## open other Terminal 
run - docker ps  
  you will see the running conatainer , take the conatiner port number & enter into the conatiner using the command
   docker exec -it "ports number" /bin/bash 

   once you done you can check with " ls " , you can see the MTD.py file there 
### check ip changing
in the same terminal after entering the container using port number use the command 
ip addr 
ifconfig 

Check the ip and cross check with docker image runing you will find the ip changing 
