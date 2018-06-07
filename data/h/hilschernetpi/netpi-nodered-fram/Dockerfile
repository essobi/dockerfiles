#use latest armv7hf compatible debian OS version from group resin.io as base
image  
FROM resin/armv7hf-debian:stretch  
  
#enable building ARM container on x86 machinery on the web (comment out next
line if built on Raspberry)  
RUN [ "cross-build-start" ]  
  
#labeling  
LABEL maintainer="netpi@hilscher.com" \  
version="V1.1.0" \  
description="Node-RED with fram nodes for netPI RTE 3"  
#version  
ENV HILSCHERNETPI_NODERED_FRAM_VERSION 1.1.0  
#copy files  
COPY "./init.d/*" /etc/init.d/  
COPY "./node-red-contrib-fram/*" /tmp/  
  
#do installation  
RUN apt-get update \  
&& apt-get install curl build-essential python-dev \  
#install node.js  
&& curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - \  
&& apt-get install -y nodejs \  
#install Node-RED  
&& npm install -g --unsafe-perm node-red \  
#install nodes  
&& mkdir /usr/lib/node_modules/node-red-contrib-fram \  
&& mv /tmp/fram.js /tmp/fram.html /tmp/package.json -t
/usr/lib/node_modules/node-red-contrib-fram \  
&& cd /usr/lib/node_modules/node-red-contrib-fram \  
&& npm install \  
#clean up  
&& rm -rf /tmp/* \  
&& apt-get remove curl \  
&& apt-get -yqq autoremove \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/*  
#set the entrypoint  
ENTRYPOINT ["/etc/init.d/entrypoint.sh"]  
  
#Node-RED Port  
EXPOSE 1880  
#set STOPSGINAL  
STOPSIGNAL SIGTERM  
  
#stop processing ARM emulation (comment out next line if built on Raspberry)  
RUN [ "cross-build-end" ]  

