FROM ubuntu:latest  
  
MAINTAINER Guillaume Charléty <guillaume.charlety@orange.com  
  
ENV PATH /usr/bin/node:$PATH  
  
RUN apt-get -y update \  
&& apt-get install -y npm graphicsmagick \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN npm install -g jasmine  
RUN npm install -g webdriverio@2.4.5  
RUN npm install -g webdrivercss  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN mkdir /testIhm  
VOLUME /testIhm  
WORKDIR /testIhm  

