# Dockerfile to build Database in container images  
# Based on Ubuntu  
############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:14.04  
# File Author / Maintainer  
MAINTAINER Alex lanxic@gmail.com  
# set env with noninteractive  
ENV DEBIAN_FRONTEND=noninteractive  
# Update the repository sources list  
RUN apt-get -y update  
  
# install auditional tools build-essential  
RUN apt-get install -y wget vim curl openssh-server build-essential  
  
# Create the default data directory  
RUN mkdir -p /root/.ssh && chmod 0700 /root/.ssh  
COPY files/authorized_keys /root/.ssh/authorized_keys  
  
# initialing user and group ubuntu  
RUN groupadd -g 1000 ubuntu  
RUN useradd -u 1000 -g 1000 -d /home/ubuntu -m ubuntu -s /bin/bash  
RUN mkdir -p /home/ubuntu/.ssh && chmod 0700 /home/ubuntu/.ssh  
COPY files/authorized_keys /home/ubuntu/.ssh/authorized_keys  
RUN chown -R ubuntu: /home/ubuntu/.ssh/ -f  
  
# initialing user and group git  
RUN groupadd -g 10000 git  
RUN useradd -u 10000 -g 10000 -d /home/git -m git -s /bin/bash  
RUN mkdir -p /home/git/.ssh && chmod 0700 /home/git/.ssh  
COPY files/authorized_keys /home/git/.ssh/authorized_keys  
RUN chown -R git: /home/git/.ssh/ -f  
  
# initiling group admins  
RUN groupadd admins  
RUN usermod -aG admins ubuntu  
COPY files/sudo_admins /etc/sudoers.d/admins  
  
################## BEGIN INSTALLATION ######################  
# Install Database Gotomalls Following the Instructions at Database Docs  
# Ref:  
# Add the package verification key  
RUN apt-get install -y mysql-common mysql-server mysql-client htop  
  
# configure database primary  
COPY files/my.cnf.ori /etc/mysql/my.cnf-master  
RUN ln /etc/mysql/my.cnf-master /etc/mysql/my.cnf  
  
##################### INSTALLATION END #####################  
  
# Set default container command  
COPY files/start.sh /start.sh  
ENTRYPOINT /bin/sh /start.sh  

