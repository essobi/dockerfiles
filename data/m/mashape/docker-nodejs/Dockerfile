# node.js  
#  
# VERSION latest  
# use the centos base image provided by dotCloud  
FROM centos  
MAINTAINER Marco Palladino, marco@mashape.com  
  
# Node version  
ENV NODE_VERSION 0.10.28  
# Upgrading system  
RUN yum -y clean all  
RUN yum -y distro-sync  
RUN yum -y update  
RUN yum -y upgrade  
  
# Installing node.js  
RUN yum install -y wget tar make gcc-c++ openssl openssl-devel  
RUN cd /tmp && wget
http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.gz && tar xzf
node-v$NODE_VERSION.tar.gz && cd node-v$NODE_VERSION && ./configure && make &&
make install  
  
# Installing git and ssh-agent and GraphicsMagick  
RUN yum install -y libpng libjpeg libpng-devel libjpeg-devel libpng  
RUN yum install -y git openssh-clients GraphicsMagick  
  
# Installing gulp and bower globally  
RUN npm install -g gulp  
RUN npm install -g bower  

