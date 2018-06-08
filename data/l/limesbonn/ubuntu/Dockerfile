#################################################################  
# Dockerfile to build ubuntu container  
# images  
# Based on Ubuntu  
##################################################################  
# Set the base image to Ubuntu  
FROM ubuntu:14.04  
# File/Author / Maintainer  
MAINTAINER Hartmut Schultze <limesbonn@schua.33mail.com>  
# Update the repository sources list, install wget, unzip, python  
RUN apt-get update && apt-get install --yes wget unzip python  
# Working directory in /bin  
WORKDIR /bin  
# Remove wget and unzip  
RUN apt-get purge --yes wget unzip  
# Working directory  
WORKDIR /  

