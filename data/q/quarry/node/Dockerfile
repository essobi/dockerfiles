FROM ubuntu:12.04  
  
# Update package repository  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe
multiverse" > /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Required packages  
RUN apt-get install -y rlwrap wget git curl software-properties-common python
python-software-properties g++ make  
  
# Init node.js  
RUN add-apt-repository -y ppa:chris-lea/node.js  
RUN apt-get update  
RUN apt-get install -y nodejs

