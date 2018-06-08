FROM node:9-alpine  
  
ENV PHANTOMJS_VERSION='2.11'  
  
RUN apk update && apk add \--no-cache fontconfig curl curl-dev && \  
mkdir -p /usr/share && \  
cd /usr/share \  
&& curl -L https://github.com/Overbryd/docker-phantomjs-
alpine/releases/download/${PHANTOMJS_VERSION}/phantomjs-alpine-x86_64.tar.bz2
| tar xj \  
&& ln -s /usr/share/phantomjs/phantomjs /usr/bin/phantomjs \  
&& phantomjs --version  

