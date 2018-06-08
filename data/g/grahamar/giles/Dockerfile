# Giles The Librarian  
#  
# VERSION 1.0  
FROM ubuntu:latest  
  
MAINTAINER Graham Rhodes <graham.a.r@gmail.com>  
  
# Add 10gen official apt source to the sources list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist
10gen' | tee /etc/apt/sources.list.d/10gen.list  
  
# Install MongoDB  
RUN apt-get update  
RUN apt-get install -y -q mongodb-org  
  
# Create the MongoDB data directory  
RUN mkdir -p /data/db  
RUN mkdir /data/.index  
RUN mkdir /data/.git_checkouts  
  
# Install Java 6  
RUN apt-get -y install openjdk-6-jdk && apt-get clean  
  
# Install Git  
RUN apt-get install -y git  
  
ADD
https://github.com/grahamar/Giles/releases/download/v0.0.10/giles-0.0.10.tgz
/opt/  
RUN tar xzf /opt/giles-0.0.10.tgz -C /opt  
  
EXPOSE 27017 1717  
ENTRYPOINT /usr/bin/mongod --fork --syslog & /opt/giles-0.0.10/bin/giles
-Dhttp.port=1717
-Dconfig.file=/opt/giles-0.0.10/conf/production.application.conf  

