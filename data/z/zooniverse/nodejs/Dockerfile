FROM ubuntu:14.04  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y nodejs npm coffeescript && \  
ln -s /usr/bin/nodejs /usr/local/bin/node  

