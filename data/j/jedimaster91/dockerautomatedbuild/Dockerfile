##################################################################  
# Dockerfile to demonstrate the behavior of automated docker build  
##################################################################  
# Build from base image ubuntu  
FROM ubuntu:17.10  
# Author: Anna Lissa Saupan  
MAINTAINER Anna Lissa Saupan <annalissa.saupan@gmail.com>  
# create 'mynewdir' and 'mynewfile'  
RUN mkdir mynewdir  
RUN touch /mynewdir/mynewfile  
# Write the message in file  
RUN echo 'this is my new container to make image and then push to hub
automatically via Github' >/mynewdir/mynewfile  

