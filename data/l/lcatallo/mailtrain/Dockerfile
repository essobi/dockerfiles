FROM node:6-alpine  
MAINTAINER lcatallo <luca.catallo.293@gmail.com>  
  
ARG MAILTRAIN_VERSION=1.20.0  
RUN set -e && apk add --no-cache curl \  
&& cd /tmp \  
&& curl -L
https://github.com/andris9/mailtrain/archive/v${MAILTRAIN_VERSION}.tar.gz -o
mt.tar.gz \  
&& tar xzf mt.tar.gz \  
&& mv mailtrain-${MAILTRAIN_VERSION} /mailtrain \  
&& cd /mailtrain \  
&& npm install --production  
  
ADD ./mailtrain /mailtrain  
  
ENV NODE_ENV=production  
  
EXPOSE 3000  
WORKDIR /mailtrain  
  

