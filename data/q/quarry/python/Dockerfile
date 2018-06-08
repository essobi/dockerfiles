FROM ubuntu:12.04  
# Update package repository  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe
multiverse" > /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y curl software-properties-common python-software-
properties make  
  
# install python and pip  
RUN curl -O http://python-distribute.org/distribute_setup.py  
RUN python distribute_setup.py  
RUN curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py  
RUN python get-pip.py

