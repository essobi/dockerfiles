#  
# Python3/bottle web server Dockerfile  
#  
# https://github.com/Pablosan/bottle-py3  
#  
# Pull base image  
FROM ubuntu:14.04.1  
# Make sure we're up to date!  
RUN apt-get update && apt-get -y upgrade  
  
# Install Python3  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3-pip  
  
# Install Python packages  
RUN pip3 install -U bottle==0.12.7 configargparse==0.9.2 tornado==4.0  
# Cleanup for a smaller image  
RUN apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/*  

