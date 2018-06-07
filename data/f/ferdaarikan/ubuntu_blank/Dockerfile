FROM ubuntu:14.04  
MAINTAINER testuser  
  
# Enable EPEL for Node.js  
# RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
# Install Node...  
#RUN yum install -y npm  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get -qq update  
RUN apt-get install -y nodejs npm  
# TODO could uninstall some build dependencies  
# debian installs `node` as `nodejs`  
RUN update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10  
  
# Copy app to /src  
#COPY . /src  
# Install app and dependencies into /src  
#RUN cd /src; npm install  
#EXPOSE 8080  
#CMD cd /src && node ./hello.js  

