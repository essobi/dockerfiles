FROM ubuntu:12.04  
run echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
run apt-get -y update  
  
# add mongo repo  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10  
RUN echo "deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist
10gen" | tee -a /etc/apt/sources.list.d/10gen.list  
RUN apt-get update  
  
# install mongo itself  
RUN apt-get -y install apt-utils  
RUN apt-get -y install mongodb-10gen  
  
# where the mongo data lives by default  
RUN mkdir -p /data/db  
  
# we run mongo - we should put supervisor here and configure the data
directory  
ENTRYPOINT ["/usr/bin/mongod"]

