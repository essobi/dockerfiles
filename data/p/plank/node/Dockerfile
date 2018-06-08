#################################################################  
# Image: plank/node  
# Plank node distribution with supervisord & node-gyp installed  
#################################################################  
FROM node:7  
MAINTAINER rajesh@getplank.com  
  
RUN chown -R root /usr/local && chgrp -R root /usr/local  
  
RUN apt-get update && \  
npm install -g node-gyp && \  
apt-get install -y supervisor  
  
CMD [ "node" ]  

