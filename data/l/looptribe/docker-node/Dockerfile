FROM node:4.3  
  
MAINTAINER Diego Ferri <diego.ferri@looptribe.com>  
  
RUN groupadd node && useradd \--create-home -g node node  
RUN mkdir /data && chown node:node /data  
  
VOLUME /data  
WORKDIR /data

