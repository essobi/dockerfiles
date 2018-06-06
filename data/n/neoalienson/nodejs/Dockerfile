FROM ubuntu:14.04.4  
MAINTAINER neo [at] orz [dot] hk  
  
ENV DEBIAN_FRONTEND=noninteractive \  
NODE_VERSION=5.6.0 \  
NPM_VERSION=3.7.4 \  
BOWER_VERSION=1.7.7 \  
GRUNT_VERSION=0.1.13 \  
GULP_VERSION=3.9.1  
  
# Install nodejs, npm and common tools  
RUN apt-get update && \  
apt-get install -y git wget curl unzip ruby && \  
curl --retry 3 -SLO
"http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz"
&& \  
tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 && \  
rm "node-v$NODE_VERSION-linux-x64.tar.gz" && \  
npm install -g npm@"$NPM_VERSION" && \  
npm install -g gulp@"$GULP_VERSION" grunt-cli@"$GRUNT_VERSION"
bower@"$BOWER_VERSION" && \  
npm cache clear  
  

