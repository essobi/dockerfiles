FROM ubuntu:14.04  
MAINTAINER "Shadow Robot's Software Team <software@shadowrobot.com>"  
LABEL Description="Deployment Test Image" Version="1.0"  
  
# Setting up bash as default shell  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Installing needed libraries for Ansible  
RUN apt-get update  
RUN apt-get install -y python2.7 python  
  
# Creation sudo user for testing  
RUN useradd -m testuser && echo "testuser:testpassword" | chpasswd && adduser
testuser sudo  
  
# Setting up SSH access  
RUN apt-get install -y openssh-server  
  
# Required to not get a 'Missing privilege separation directory' error  
RUN mkdir /var/run/sshd  
  
# Removing cache  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

