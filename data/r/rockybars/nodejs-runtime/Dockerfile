# debian sid base image  
FROM debian:sid  
MAINTAINER Dhi Aurrahman <diorahman@rockybars.com>  
RUN apt-get update -y && apt-get install --no-install-recommends -y -q curl
python build-essential git ca-certificates  
RUN mkdir /nodejs && curl
http://nodejs.org/dist/v0.10.30/node-v0.10.30-linux-x64.tar.gz | tar xvzf - -C
/nodejs --strip-components=1  
PATH $PATH:/nodejs/bin  
  

