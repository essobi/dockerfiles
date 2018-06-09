# jdash/supervisor Docker File  
# Built on ubuntu:latest  
# Version 1.0  
# Define the initial base image  
FROM ubuntu:latest  
  
# Maintainer Informaion  
MAINTAINER @jdash  
  
# Update the base image  
RUN sed -i.bak 's/main$/main universe/' /etc/apt/sources.list  
RUN apt-get update && apt-get upgrade -qq  
  
# Install Supervisord  
RUN apt-get install -qq supervisor  
  
# Make the necessary folders for Supervisord  
RUN mkdir -p /var/log/supervisor /etc/supervisor/conf.d  
  
# Add the base configuration file for Supervisord  
ADD supervisor.conf /etc/supervisor.conf  

