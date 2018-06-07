FROM node:slim  
  
MAINTAINER Ingo Reinhart <ingo.reinhart@gmail.com>  
  
USER root  
  
RUN apt-get update && apt-get -y upgrade && apt-get -y install netcat && apt-
get -y --PURGE autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/*  
  
ADD . /install  
WORKDIR /install  
RUN npm install -g $(cat packages) && rm -rf npm_cache /tmp/*  
ENV NODE_PATH /usr/local/lib/node_modules/  
  
RUN mkdir /app  
WORKDIR /app  
VOLUME ["/app"]  

