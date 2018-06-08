FROM node:latest  
MAINTAINER James Ribar <james@jribar.com>  
  
RUN mkdir /tmp/phantomjs \  
&& curl -L
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
\  
| tar -xj --strip-components=1 -C /tmp/phantomjs \  
&& mv /tmp/phantomjs/bin/phantomjs /usr/bin \  
&& rm -rf /tmp/phantomjs  
  

