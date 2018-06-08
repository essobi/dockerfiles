##########################################  
# Dockerfile to build an Apache2 image  
##########################################  
# Base image is Ubuntu  
FROM ubuntu:14.04  
  
# Author  
MAINTAINER Miguel Ramirez <miccke.rmz@gmail.com>  
  
# Install apache2 package  
RUN apt-get update && \  
apt-get install -y apache2 && \  
apt-get clean  
  
# Default command  
CMD ["apachectl", "-D", "FOREGROUND"]  
  
# Ports  
EXPOSE 80  

