#use latest armv7hf compatible debian OS version from group resin.io as base
image  
FROM resin/armv7hf-debian:jessie  
  
#enable building ARM container on x86 machinery on the web (comment out next
line if built on Raspberry)  
RUN [ "cross-build-start" ]  
  
#labeling  
LABEL maintainer="netpi@hilscher.com" \  
version="V0.9.2" \  
description="Node-RED with npix leds node to control LEDs of LED supporting
NPIX modules"  
#version  
ENV HILSCHERNETPI_NODERED_NPIX_LEDS_VERSION 0.9.2  
#copy files  
COPY "./init.d/*" /etc/init.d/  
COPY "./node-red-contrib-npix-leds/*" /tmp/  
  
#do installation  
RUN apt-get update \  
&& apt-get install curl build-essential \  
#install node.js  
&& curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - \  
&& apt-get install -y nodejs \  
#install Node-RED  
&& npm install -g --unsafe-perm node-red \  
#install node  
&& mkdir /usr/lib/node_modules/node-red-contrib-npix-leds \  
&& mv /tmp/npixleds.js /tmp/npixleds.html /tmp/package.json -t
/usr/lib/node_modules/node-red-contrib-npix-leds \  
&& cd /usr/lib/node_modules/node-red-contrib-npix-leds \  
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

