FROM node:6.9.2  
MAINTAINER Vicente Pons <simpons@gmail.com>  
  
ENV EMBERCLI_VERSION=2.10.0 \  
BOWER_VERSION=1.8.0 \  
PHANTOMJS_VERSION=2.1.14 \  
WATCHMAN_VERSION=4.7.0  
RUN npm install -g \  
ember-cli@${EMBERCLI_VERSION} \  
bower@${BOWER_VERSION} \  
phantomjs-prebuilt@${PHANTOMJS_VERSION}  
  
RUN apt-get update &&\  
apt-get install -y autoconf automake build-essential python-dev &&\  
git clone https://github.com/facebook/watchman.git &&\  
cd watchman &&\  
git checkout v${WATCHMAN_VERSION} &&\  
./autogen.sh &&\  
./configure &&\  
make &&\  
make install  

