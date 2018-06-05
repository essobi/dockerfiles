FROM ubuntu:14.04  
MAINTAINER Dennis Hazelett "dennis.hazelett@csmc.edu"  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN apt-get install -y zip unzip aria2 git  
  
RUN useradd -m user1  
RUN chown -R user1:staff /home/user1  
  
RUN apt-get install -y wget python-pip bedtools samtools python-dev libpython-
dev libevent-dev  
RUN pip install numpy  
RUN pip install macs2  

