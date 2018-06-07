FROM ubuntu:15.04  
MAINTAINER Markus Huggler <markus.huggler@ecologic.ch>  
  
RUN apt-get update && apt-get install curl git-core  
RUN curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash -  
RUN apt-get install nodejs  
  
RUN npm install -g bower gulp nodemon  
  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN mkdir /home/nodejs && useradd --home /home/nodejs nodejs && chown -R
nodejs:nodejs /home/nodejs  
  
RUN mkdir /app && chown -R nodejs:nodejs /app  
  
USER nodejs  

