# Nginx  
#  
# VERSION 0.0.1  
FROM ubuntu  
MAINTAINER Guillaume J. Charmes "guillaume@dotcloud.com"  
# make sure the package repository is up to date  
#RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update  
  
RUN apt-get install -y curl  
# INSERT https://raw.github.com/creack/docker-vps/master/nginx-wrapper.sh
/usr/sbin/nginx-wrapper  

