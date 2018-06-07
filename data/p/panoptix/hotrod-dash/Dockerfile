FROM node:4.4-onbuild  
MAINTAINER Stephan Buys <stephan.buys@panoptix.co.za>  
  
RUN npm install -g bower  
RUN bower --allow-root install  
  
EXPOSE 3000  
#ADD local.yml /usr/src/app/src/config/local.yml  
#Your configured configuration directory  
#ADD config /opt/hotrod/config  
# To build (from this folder):  
# docker build -t hotrod-dash .  
# docker run -p 3000:3000 -d --name hotrod-dash-test hotrod-dash  

