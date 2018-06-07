FROM ubuntu:16.04  
MAINTAINER German Sanchez <german@hackn.beer>  
  
RUN apt-get update && apt-get install -y -q curl wget  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
  
RUN apt-get update && \  
apt-get install -y -q \  
nodejs \  
default-jre \  
&& apt-get -y autoclean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN npm config set unsafe-perm true \--global  
  
RUN npm install -g -y ionic@beta  
RUN npm install -g -y cordova  
RUN npm install -g -y gulp  
  
WORKDIR /public  

