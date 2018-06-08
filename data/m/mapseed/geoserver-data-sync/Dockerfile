###########################################################  
# Dockerfile to build MapSeed Application Containers  
############################################################  
  
# Set the base image:  
FROM node:8-wheezy  
  
# File Author / Maintainer  
MAINTAINER Lucas Stewart <luke@mapseed.org>  
  
# # Update the sources list  
RUN apt-get update -y  
  
# # Install basic applications  
RUN apt-get install -y tar git curl wget dialog net-tools build-essential vim
python-pip python-dev  
RUN pip install awscli  
  
RUN git clone https://github.com/lukeswart/docker-geoserver.git && cd docker-
geoserver && git checkout s3-sync && cd -  
  
# Set the default directory where CMD will execute  
WORKDIR /docker-geoserver/s3-sync  
  
# Install our npm dependencies  
RUN NODE_ENV=production npm install  
  
CMD ./start.sh

