###########################################  
# Dockerfile to build a New image  
###########################################  
# Base image is Ubuntu  
FROM ubuntu:14.04  
# Author: Vinod Singh  
MAINTAINER Vinod Singh <vinod.puchi@gmail.com>  
# create 'mynewdir' and 'mynewfile'  
RUN mkdir mynewdir  
RUN touch /mynewdir/mynewfile  
# Write the message in file  
RUN echo 'this is my new container to make image and then push to hub for
docker 1.12.1 TEST' \  
>/mynewdir/mynewfile  

