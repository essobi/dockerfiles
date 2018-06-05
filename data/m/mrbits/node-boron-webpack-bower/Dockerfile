FROM node:6-slim  
LABEL "Maintainer"="MrBiTs"  
LABEL "e-mail"="mrbits.dcf@gmail.com"  
LABEL "version"="0.0.4"  
  
RUN npm install webpack -g  
RUN npm install bower -g  
RUN apt-get update && apt-get install -y wget git bzip2  
RUN mkdir -p /tmp/phantomjs && cd /tmp/phantomjs && wget -q
https://github.com/Medium/phantomjs/releases/download/v2.1.1/phantomjs-2.1.1-linux-x86_64.tar.bz2  
RUN apt-get -y remove wget  

