# Moving Target Defense

A project implementing Moving Target Defense (MTD) strategies using Docker and Python to enhance network security. This setup allows for dynamic IP changing, simulating an environment with improved resilience against attacks.

## Installation

### Prerequisites
Ensure you have **Python** and **Docker** installed.

#### Python
Install Python:

pip install python


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
