# Mongod service  
# VERSION 0.1  
FROM stackbrew/ubuntu:saucy  
RUN apt-get -y update  
  
# Add MongoDB repository  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist
10gen' > /etc/apt/sources.list.d/mongodb.list  
RUN apt-get -y update  
  
# Install MongoDB  
RUN apt-get -y install apt-utils  
RUN apt-get -y install adduser  
RUN apt-get -y install mongodb-10gen  
  
# Database storage volume  
VOLUME ["/data"]  
  
# Expose default MongoDB port  
# 27017 - Default mongod, mongos  
# 27018 - shardsvr default  
# 27019 - configsvr default  
# 28017 - webstatus default  
EXPOSE 27017  
ENTRYPOINT ["/usr/bin/mongod","--dbpath","/data","--journal"]  

