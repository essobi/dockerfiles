FROM ubuntu:14.04.3  
  
MAINTAINER Raseel Bhagat <raseelbhagat@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y build-essential git openssh-server unzip wget && \  
apt-get clean && \  
useradd -m -p saOW3jh0UuXiQ user && \  
echo "user ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
EXPOSE 22  
  
ENTRYPOINT service ssh start && /bin/bash  

