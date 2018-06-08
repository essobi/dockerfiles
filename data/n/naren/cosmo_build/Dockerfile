############################################################  
# Dockerfile to build Python WSGI Application Containers  
# Based on Ubuntu  
############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:14.04  
  
# File Author / Maintainer  
MAINTAINER cosmolabbers  
  
# Update the sources list  
RUN apt-get update  
  
# Install basic applications  
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential  
  
# Install Python and Basic Python Tools  
RUN apt-get install -y python python-dev python-distribute python-pip python-
setuptools  
  
# Copy the application folder inside the container  
ADD /cosmo /cosmo  
  
# Get pip to download and install requirements:  
RUN pip install -e /cosmo/  
  
# Expose ports  
EXPOSE 5555  
  
# Set the default directory where CMD will execute  
WORKDIR /cosmo  
  
# Set the default command to execute  
# when creating a new container  
# i.e. using CherryPy to serve the application  
CMD development  

