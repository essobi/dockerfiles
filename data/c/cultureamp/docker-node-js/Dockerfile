FROM ubuntu:16.04  
MAINTAINER Erlangga Tjhie <erlanggatjhie@cultureamp.com>  
  
RUN apt-get update \  
&& apt-get install -y build-essential wget curl ocaml libelf-dev libelf1 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV NODE_VERSION 8.9.4  
  
RUN wget
https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.xz
\  
&& tar -xJf node-v${NODE_VERSION}-linux-x64.tar.xz \  
&& chown -R root:root node-v${NODE_VERSION}-linux-x64 \  
&& mv node-v${NODE_VERSION}-linux-x64/bin/node /usr/bin \  
&& make install -C node-v${NODE_VERSION}-linux-x64/lib/node_modules/npm \  
&& rm -rf node-v${NODE_VERSION}-linux-x64.tar.xz
node-v${NODE_VERSION}-linux-x64  
  
RUN npm install -g yarn  

