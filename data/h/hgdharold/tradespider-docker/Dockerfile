#Dockerfile for tradespider client  
FROM python:2-onbuild  
MAINTAINER harold <wmsmoxkx@163.com>  
# Tradespider client needs the following two eggs  
RUN easy_install crypto-1.1.0-py2.7.egg  
RUN easy_install dnspython-1.11.1-py2.7.egg  
  
#install nodejs  
ENV NODE_VERSION 0.12.7  
# Build and install Node.js, upgrade NPM to the latest version and install
JPSM  
RUN \  
cd /tmp && \  
wget http://nodejs.org/dist/v0.12.7/node-v0.12.7.tar.gz && \  
tar xvzf node-v*.tar.gz && \  
rm -f node-v*.tar.gz && \  
cd node-v* && \  
./configure && \  
CXX="g++ -Wno-unused-local-typedefs" make && \  
CXX="g++ -Wno-unused-local-typedefs" make install && \  
cd /tmp && \  
rm -rf /tmp/node-v* && \  
npm install -g npm && \  
npm install -g jspm && \  
printf '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bashrc  
# Used by Beyond build scripts  
ENV NODE_BIN /usr/local/bin/node  
ENV NPM_BIN /usr/local/bin/npm  
ENV JSPM_BIN /usr/local/bin/jspm  

