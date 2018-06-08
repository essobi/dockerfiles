FROM debian:stretch-slim  
MAINTAINER phonoloop <phonoloop@spaceape.be>  
  
#  
# Update system  
#  
RUN apt-get update -y  
  
#  
# Dependencies  
#  
RUN apt-get install -y \  
unzip \  
python-pip \  
software-properties-common  
  
#  
# Install main package  
#  
RUN pip install awscli  

