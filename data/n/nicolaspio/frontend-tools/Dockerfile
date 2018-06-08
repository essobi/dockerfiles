# nicolaspio/frontend-tools  
# VERSION 0.1.0  
  
FROM debian:jessie  
MAINTAINER Nicolas Pio <nicolaspiof@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install nodejs and npm  
RUN \  
apt-get update && \  
apt-get -y install \  
git \  
nodejs \  
npm && \  
ln -s /usr/bin/nodejs /usr/bin/node && \  
npm install -g \  
gulp \  
grunt-cli \  
bower \  
browserify \  
mocha && \  
adduser --disabled-password --gecos '' frontend &&\  
apt-get clean && \  
rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  
  
WORKDIR /home/frontend  

