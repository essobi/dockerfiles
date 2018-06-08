# Chahasy on Mosca on Alpine  
#  
# VERSION 0.4.0  
FROM mhart/alpine-node:8  
MAINTAINER Hans Klunder <hans.klunder@bigfoot.com>  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app/  
  
COPY ./ /usr/src/app/  
  
RUN apk update && \  
apk add make gcc g++ python git && \  
npm install --unsafe-perm --production && \  
apk del make gcc g++ python git  
  
EXPOSE 8080  
EXPOSE 1883  
ENTRYPOINT ["/bin/sh","/usr/src/app/docker/startup.sh"]  

