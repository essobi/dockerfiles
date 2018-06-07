FROM ubuntu:16.04  
MAINTAINER grisha85  
  
RUN apt-get update -y  
RUN apt-get install -y python build-essential python-pip libnanomsg-dev  
RUN pip install nanomsg tabulate pandas # xraycli deps  
ADD . /libxray  
WORKDIR /libxray  

