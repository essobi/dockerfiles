# This docker file will create a container using the latest official Ubuntu
image and install Flask  
# Created by rkiles on 7-9-2016  
# Updated to clone the beeInformed git repo  
FROM ubuntu:latest  
MAINTAINER Richard Kiles <rkiles@gdt.com>  
RUN apt-get -y update && apt-get install -y \  
tar \  
git \  
curl \  
vim \  
wget \  
build-essential \  
python \  
python-dev \  
python-pip  
RUN pip install requests  
WORKDIR /tmp  
RUN git clone https://github.com/GDT-Labs/beeInformed.git  
WORKDIR beeInformed  

