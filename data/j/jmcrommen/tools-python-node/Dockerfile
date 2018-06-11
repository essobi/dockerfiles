FROM python:2.7.14-jessie  
MAINTAINER Jean-Marie CROMMEN  
  
RUN \  
apt-get update && \  
apt-get install -yqq apt-transport-https  
  
RUN \  
echo "deb https://deb.nodesource.com/node_8.x jessie main" >
/etc/apt/sources.list.d/nodesource.list && \  
wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
\- && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" >
/etc/apt/sources.list.d/yarn.list && \  
wget -qO- https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- && \  
apt-get update && \  
apt-get install -yqq nodejs yarn && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
npm install clean-css -g && \  
npm install uglify-js -g  
  
CMD /bin/bash

