FROM ubuntu:12.04  
  
MAINTAINER Keyvan Fatehi <keyvanfatehi@gmail.com>  
  
RUN apt-get -y update && apt-get -y -q install curl && apt-get -y -q clean  
RUN curl -o ~/node.tar.gz
http://nodejs.org/dist/v0.10.24/node-v0.10.24-linux-x64.tar.gz  
RUN cd /usr/local && tar --strip-components 1 -xzf ~/node.tar.gz && rm
~/node.tar.gz  

