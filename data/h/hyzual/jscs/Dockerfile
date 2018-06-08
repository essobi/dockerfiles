## Dockerfile for jscs  
FROM leanlabs/npm-builder:latest  
MAINTAINER Hyzual "hyzual@gmail.com"  
RUN npm install -g jscs@^1.13.1 \  
&& mkdir -p /lint  
  
ENTRYPOINT ["/usr/bin/jscs"]  
WORKDIR /lint  

