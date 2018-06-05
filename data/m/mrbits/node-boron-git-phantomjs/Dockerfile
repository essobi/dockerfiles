FROM node:boron-alpine  
LABEL "Maintainer"="MrBiTs"  
LABEL "e-mail"="mrbits.dcf@gmail.com"  
LABEL "version"="0.0.2"  
  
RUN apk add --no-cache git wget  
RUN mkdir -p /tmp/phantomjs && cd /tmp/phantomjs && wget -q
https://github.com/Medium/phantomjs/releases/download/v2.1.1/phantomjs-2.1.1-linux-x86_64.tar.bz2  
  
RUN apk del wget  

