# Dockerfile  
# The FROM directive sets the Base Image for subsequent instructions  
FROM ubuntu:14.04  
# Replace shell with bash so we can source files  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Install mongoDB  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0C49F3730359A14518585931BC711F9BA15703C6  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/testing
multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list  
  
# Run updates and install deps  
RUN apt-get update && apt-get install -y \  
mongodb-org \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get -y autoclean \  
&& rm -rf /var/lib/mongodb  
  
RUN mkdir -p /data/db  
COPY ./dump /dump  
  
# COMMANDES  
RUN mongod --fork --logpath=/tmp/mongodb.log ; \  
mongorestore --db fresh dump/fresh  
  
# Configuring the default command launched at RUN  
ENTRYPOINT mongod  
  
#Expose the port  
EXPOSE 27017  

