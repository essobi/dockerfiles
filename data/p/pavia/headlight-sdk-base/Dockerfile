FROM ubuntu:xenial  
# FROM hypriot/rpi-node:6.5-slim  
MAINTAINER Jason Hillier <jason.hillier@paviasystems.com>  
  
# Prepare APT  
ENV DEBIAN_FRONTEND noninteractive  
# These two lines are combined so apt-get update doesn't cache in docker.  
RUN apt-get update && apt-get -y --force-yes install git curl p7zip-full vim
nano python python-pip telnet iputils-ping dnsutils  
  
# Install node.js  
RUN curl --silent --location https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install --yes nodejs  
  
# Setup NodeJS  
RUN npm install -g bunyan  
RUN npm install -g gulp  
RUN npm install -g fetch-rancher-metadata  
RUN npm install -g kongfig  
  
# Clean APT  
RUN rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8080  
ADD run.sh /run.sh  
ADD kong.json /kong.json  
ENTRYPOINT ["/run.sh"]  

