#################################  
# Dockerfile to build a new image  
#################################  
# Base image is Ubuntu  
FROM ubuntu:14.04  
# Author: Tim Caudrey  
MAINTAINER Tim Caudrey <tim.caudrey@gmail.com>  
# Create 'mynewdir' and 'mynewfile'  
RUN mkdir mynewdir  
RUN touch /mynewdir/mynewfile  
# Write the message in mynewfile  
RUN echo 'this is my new container to make into an image and the push to the
docker hub'>/mynewdir/mynewfile  

