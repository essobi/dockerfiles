# Dockerfile  
#  
# Details:  
# - Ubuntu 14.04  
##  
# Pull base image.  
FROM ubuntu:14.04  
  
# Maintainer  
MAINTAINER Fidesio <docker@fidesio.com>  
  
### Base  
# Update Ubuntu  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
  
# Install/Upgrade basic packages  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget git gcc g++ build-
essential  
  
# Timezone  
RUN echo "Europe/Paris" | sudo tee /etc/timezone  
RUN sudo dpkg-reconfigure --frontend noninteractive tzdata  
  
### /Base  

