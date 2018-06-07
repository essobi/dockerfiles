# MongoDB  
#  
# VERSION 0.0.1  
FROM ubuntu:14.04  
MAINTAINER Jeffery Utter "jeff@jeffutter.com"  
ENV LC_ALL C  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10 && \  
bash -c "echo deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist
10gen > /etc/apt/sources.list.d/10gen.list"  
RUN apt-get update  
RUN apt-get -y install mongodb-org  
RUN mkdir -p /data/db  
  
EXPOSE 27017  
CMD ["/usr/bin/mongod"]  

