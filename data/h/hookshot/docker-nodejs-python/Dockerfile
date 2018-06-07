FROM mhart/alpine-node:4.9.0  
MAINTAINER brantje <brantje@gmail.com>  
  
ENV VERSION=v9.10.0 NPM_VERSION=5  
  
RUN apk update && \  
apk add ca-certificates wget curl tar xz python python-dev py-pip util-linux
bash gawk sed grep bc coreutils openrc && \  
npm install -g newman && pip install flake8  
  

