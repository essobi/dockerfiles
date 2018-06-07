FROM ubuntu:16.04  
ENV MONGODB_VERSION 3.2.7  
ENV NODE_VERSION v6.5.0  
MAINTAINER Le Duc <lee.duc55@gmail.com>  
  
# NodeJs install instructions:  
# - https://www.digitalocean.com/community/tutorials/how-to-install-node-js-
on-ubuntu-16-04  
# Reload local package database  
RUN apt-get update && \  
apt-get install -y build-essential tcl && \  
apt-get install -y apt-utils  
  
# Install NodeJs  
run apt-get install -y python  
add http://nodejs.org/dist/$NODE_VERSION/node-$NODE_VERSION-linux-x64.tar.gz
/tmp/node/  
run tar -C /tmp/node -zxvf /tmp/node/node* && rm /tmp/node/*.tar.gz  
run cp -R -n /tmp/node/*/* /usr/local  
run rm -Rf /tmp/node.tar.gz  
run node -v  
  
RUN apt-get install -y npm  
  
# Mongodb install instructions:  
# - https://docs.docker.com/engine/examples/mongodb/  
# - https://docs.mongodb.com/v2.6/tutorial/install-mongodb-on-debian/  
# Improvement inspiration:  
# - https://github.com/docker-library/mongo/blob/master/3.0/Dockerfile  
# Install mongoDb  
RUN apt-get update > /dev/null && \  
apt-get install -y curl && \  
curl -O https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.2.9.tgz && \  
tar -zxvf mongodb-linux-x86_64-3.2.9.tgz && \  
mv mongodb-linux-x86_64-3.2.9 mongodb && \  
rm -rf mongodb-linux-x86_64-3.2.9.tgz  
  
# Create the MongoDB data directory  
RUN mkdir -p /data/db  
  
# Install Redis  
RUN apt-get install -y redis-server  

