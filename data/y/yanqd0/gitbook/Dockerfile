FROM node:8.4.0-alpine  
  
MAINTAINER Yan QiDong <yanqd0@outlook.com>  
  
ARG VERSION=3.2.3  
LABEL version=$VERSION  
  
RUN npm install --global gitbook-cli \  
&& gitbook fetch ${VERSION} \  
&& npm cache verify \  
&& rm -rf /tmp/*  
  
WORKDIR /srv/gitbook  
  
VOLUME /srv/gitbook  
  
EXPOSE 4000 35729  
CMD gitbook install && gitbook serve  

