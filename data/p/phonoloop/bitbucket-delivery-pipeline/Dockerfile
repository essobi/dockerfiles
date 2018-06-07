FROM debian:stretch-slim  
MAINTAINER spaceape <hi@spaceape.be>  
  
# Update system  
RUN apt-get update -y  
  
# Dependencies  
RUN apt-get install -y \  
zip \  
unzip \  
git \  
python-pip \  
software-properties-common  
  
# Install main package  
RUN pip install awscli  

