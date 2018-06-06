FROM ubuntu:16.04  
#MAINTAINER Advantech  
# update and install dev-tools  
RUN apt-get update  
RUN apt-get update  
RUN apt-get install -y gawk git-core diffstat gcc-multilib build-essential  
RUN apt-get install -y sed coreutils autoconf automake curl libtool libssl-dev  
RUN apt-get install -y vim net-tools iputils-ping subversion  
RUN apt-get install -y sudo  
  
# networking  
#RUN apt-get install -y ping net-tools  
# adv account  
RUN useradd -m -k /home/adv adv -p adv -s /bin/bash -G sudo  
  
# set up adv as sudo  
RUN echo "adv ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
WORKDIR /home/adv  
USER adv  
  
#install wisesnail lib and sample code  
RUN git clone \--branch wisesnail-lib-v2.0.3 https://github.com/ADVANTECH-
Corp/docker-igw-app-x86.git .  
RUN mkdir workspace  
RUN ./install_wisesnaillib.sh  
RUN rm -rf lib inc install_wisesnaillib.sh README.md  
  

