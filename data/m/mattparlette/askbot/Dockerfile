FROM ubuntu  
MAINTAINER matthew.parlette@gmail.com  
  
# use the precise (12.04) repository  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -q -y python python-dev python-pip build-essential  
RUN pip install django  
RUN pip install askbot

