FROM ubuntu:14.04  
MAINTAINER Tomás Godoi <tomas.godoi@stf.jus.br>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
git \  
mono-complete \  
nodejs \  
curl \  
build-essential  
  
RUN ln -s "$(which nodejs)" /usr/bin/node  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
npm  
  
RUN curl -sS https://registry.npmjs.org/npm/-/npm-1.4.28.tgz > npm-1.4.28.tgz
&& \  
tar -xvf npm-1.4.28.tgz && \  
cd package && \  
./configure && \  
make install && \  
cd / && \  
rm -rf npm-1.4.28.tgz /package  
  
RUN npm install -g grunt-cli

