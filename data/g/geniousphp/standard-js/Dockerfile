FROM mhart/alpine-node:6.9.2  
MAINTAINER geniousphp "geniousphp@gmail.com"  
RUN npm install -g standard@10.0.3 \  
&& npm install -g standard-reporter@1.0.5 \  
&& npm cache clean \  
&& mkdir /standard  
  
WORKDIR /standard  
  
VOLUME /standard  
  

