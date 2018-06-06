# Use ubuntu:14.04 as base image.  
FROM ubuntu:14.04  
# Install basic packages.  
RUN apt-get update &&\  
apt-get install -y build-essential software-properties-common curl wget git
htop unzip vim telnet &&\  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Create dev user  
RUN useradd dev -m -d /home/dev/ -G sudo && passwd -d -u dev  
  
# Add a script to modify dev user UID / GID  
COPY /usr/bin/change-dev-ids /usr/bin/change-dev-ids  
RUN chmod +x /usr/bin/change-dev-ids  

