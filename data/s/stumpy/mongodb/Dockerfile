# DOCKER-VERSION 1.0.0  
# MAINTAINER Niels Freier  
FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get install -y wget  
  
RUN wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-2.6.2.tgz  
RUN tar zxvf mongodb-linux-x86_64-2.6.2.tgz  
RUN mkdir -p /data/db  
  
# Define mountable directories.  
VOLUME ["/data"]  
  
EXPOSE 27017  
CMD ["/mongodb-linux-x86_64-2.6.2/bin/mongod"]  
  

