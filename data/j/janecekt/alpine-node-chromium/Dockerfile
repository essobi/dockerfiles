FROM node:10.2.1-alpine  
  
MAINTAINER Tomas Janecek  
  
LABEL Description="Docker image containing node, yarn and chromium intended as
build environment of node-based projects"  
  
ENV CHROME_BIN=/usr/bin/chromium-browser  
  
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.7/main' >
/etc/apk/repositories \  
&& echo 'http://dl-cdn.alpinelinux.org/alpine/v3.7/community' >>
/etc/apk/repositories \  
&& apk --no-cache add chromium  

