  
# Docker file for Makefile  
# Nada Salem, Oct 18, 2016  
# use rocker/hadleyverse:latest as base image  
FROM rocker/hadleyverse:latest  
  
MAINTAINER Nada Salem <nsalem92@gmail.com>  
  
# get OS updates and install build tools  
RUN apt-get update  
RUN apt-get install -y build-essential  
  
# Install necessary libraries  
RUN Rscript -e "install.packages('ezknitr')"  

