# Pull base image.  
FROM node:8.9  
MAINTAINER Incognitus LLC  
  
RUN apt-get update -y && apt-get install -y\  
ca-certificates \  
apt-transport-https \  
ttf-wqy-zenhei \  
ttf-unfonts-core  
  
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key
add -  
RUN echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list  
RUN apt-get update -y && apt-get install -y \  
google-chrome-unstable  
  
ENV CHROME_DIR=/usr/bin/google-chrome-unstable  

