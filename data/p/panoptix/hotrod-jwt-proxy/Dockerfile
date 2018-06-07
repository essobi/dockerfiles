FROM node:0.10-onbuild  
MAINTAINER Stephan Buys <stephan.buys@panoptix.co.za>  
  
RUN npm install -g bower  
RUN bower --allow-root install  
  
EXPOSE 4000  
#ADD local.yml /usr/src/app/src/config/local.yml  
#Your configured configuration directory  
#ADD config /opt/hotrod/config  
# To build (from this folder):  
# docker build -t hotrod-jwt-proxy .  
# docker run -p 4000:4000 -d --name hotrod-jwt-proxy-test hotrod-jwt-proxy  

