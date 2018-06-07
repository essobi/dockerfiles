FROM debian:jessie  
  
MAINTAINER Embar Pasaribu <embar@pasaribu.web.id>  
  
COPY sources.list /etc/apt/  
  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install -y build-essential git curl vim sudo && \  
useradd -m jessie && \  
echo "\n# Added by Dockerfile\njessie ALL=(ALL) NOPASSWD:ALL" | (EDITOR="tee
-a" visudo)  
  
WORKDIR /home/jessie  
  
USER jessie  

