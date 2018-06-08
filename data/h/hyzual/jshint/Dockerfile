## Dockerfile for jshint  
FROM leanlabs/npm-builder:latest  
MAINTAINER Hyzual "hyzual@gmail.com"  
RUN npm install -g jshint@^2.8.0 \  
&& mkdir -p /lint  
  
ENTRYPOINT ["/usr/bin/jshint"]  
WORKDIR /lint  

