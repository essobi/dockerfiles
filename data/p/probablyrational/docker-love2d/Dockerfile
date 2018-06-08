############################################################  
# Dockerfile to build Love2D container images  
# Based on ubuntu:16.04  
############################################################  
  
# Set the base image to ubuntu:16.04  
FROM ubuntu:16.04  
  
# File Author / Maintainer  
MAINTAINER Probably Rational Ltd.  
  
#Set the work directory  
WORKDIR /app  
  
# Update the repository sources list  
RUN apt update --fix-missing  
  
# Install essentials  
RUN apt install -y cron software-properties-common libsdl2-dev monit git curl
wget zip unzip htop nano ncdu screen sshfs sl cowsay python-minimal openssh-
server  
  
# Install Love2D  
RUN add-apt-repository -y ppa:bartbes/love-stable  
RUN apt update  
RUN apt install -y love  
  
# Installl a sweet ass profile  
RUN curl -o ~/.bashrc
https://gist.githubusercontent.com/hcaz/1f98157bd8ae8c647ffb3ab243d69fc8/raw/.bashrc  
COPY motd /etc/motd  
RUN chmod 600 /etc/motd  
  
# Setup Monit  
COPY monitrc /etc/monit/monitrc  
RUN chmod 600 /etc/monit/monitrc  
  
EXPOSE 2812  
  
ENTRYPOINT service ssh start && monit && /bin/bash  

