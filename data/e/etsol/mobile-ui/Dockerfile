# Front-End - Build - Dockerfile  
#  
# VERSION 0.0.1  
FROM node:8-alpine  
  
MAINTAINER Bruno Reato  
ADD config_properties.js /config_properties.js  
  
RUN apk update && \  
apk upgrade && \  
apk add unzip curl  
  
#Entrypoint  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

