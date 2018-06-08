###################################################################  
# Ubuntu Dockerfile  
#  
# https://github.com/vijaymohanp/ubuntu/blob/master/Dockerfile  
#  
###################################################################  
  
# Pull base image.  
FROM ubuntu:18.04  
  
MAINTAINER Vijay Mohan <vijay@ranker.com>  
  
# Install.  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip vim wget && \  
apt-get install -y iputils-ping && \  
apt-get install -y mysql-client && \  
rm -rf /var/lib/apt/lists/*  
  
# Add files.  
  
# Set environment variables.  
ENV HOME /root  
  
# Define working directory.  
WORKDIR /root  
  
# Define default command.  
CMD ["bash"]  

