# Dockerfile  
FROM ubuntu:14.04  
MAINTAINER Martijn van Maurik <docker@vmaurik.nl>  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist
10gen' | tee /etc/apt/sources.list.d/10gen.list  
  
RUN apt-get update  
RUN apt-get install -y -q mongodb-org  
  
RUN mkdir -p /data/db  
  
EXPOSE 27017  
VOLUME /data/db  
  
CMD /usr/bin/mongod  

