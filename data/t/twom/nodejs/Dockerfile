FROM ubuntu:14.04  
MAINTAINER Tom Deryckere <tom.deryckere@ask.com>  
RUN echo deb http://security.ubuntu.com/ubuntu trusty-security main >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install nodejs -y --fix-missing  
# Package manager installs nodejs. Forever looks for node  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN apt-get install npm -y --fix-missing  
RUN npm install -g grunt -y  
RUN npm install -g grunt-cli -y  
RUN npm install -g forever -y  

