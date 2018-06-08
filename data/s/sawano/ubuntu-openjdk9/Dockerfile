####################################################################################  
# Creates a container with OpenJDK 8  
####################################################################################  
  
# Command reference:  
# docker build -t sawano/ubuntu-openjdk9:0.0.1 -t sawano/ubuntu-
openjdk9:latest .  
# docker run -it --rm sawano/ubuntu-openjdk9 /bin/bash  
  
  
# 17.10/artful  
FROM ubuntu:17.10  
  
ENV LANG C.UTF-8  
  
RUN apt-get update && apt-get install -y \  
openjdk-9-jdk-headless=9~b181-4 && \  
rm -rf /var/lib/apt/lists  
  
WORKDIR /opt  

