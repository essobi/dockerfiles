FROM ubuntu:12.04  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update -y  
RUN apt-get install -y sudo git openssh-client bash apt-utils dialog  
RUN apt-get install -y python python-dev python-pip  
RUN apt-get install -y mysql-server mysql-client libmysqlclient-dev  
RUN echo "%admin ALL=NOPASSWD:ALL" >> /etc/sudoers

