#  
# Ubuntu Dockerfile  
#  
# https://github.com/mullnerz/docker-images/  
# https://github.com/mullnerz/docker-images/tree/master/ubuntu  
#  
FROM ubuntu:14.04  
MAINTAINER Zoltán Müllner <mullner.zoltan@gmail.com>  
  
# Install  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install \  
software-properties-common \  
bsdtar curl zip unzip wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Set environment variables  
ENV HOME /root  
  
# Define working directory  
WORKDIR /root  
  
# Define default command  
CMD ["bash"]  

