FROM mhart/alpine-node  
MAINTAINER Teruyuki Kobayashi <koba1014@gmail.com>  
  
WORKDIR /src  
ADD . .  
  
ENV HUGO_VERSION 0.17  
ENV HUGO_BINARY hugo_${HUGO_VERSION}_Linux-64bit  
  
RUN apk update && apk upgrade && \  
apk add --no-cache --virtual .build-deps make gcc g++ python && \  
npm i html-minifier -g && \  
npm cache clean && \  
apk del .build-deps && \  
apk add --no-cache py-pygments git bash openssh-client curl  
  
ADD
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz
/tmp/  
  
# RUN tar -xvzf /tmp/${HUGO_BINARY}.tar.gz -C /tmp/ && mv /tmp/hugo
/usr/bin/hugo && rm -rf /tmp/*  
RUN tar -xvzf /tmp/${HUGO_BINARY}.tar.gz -C /tmp/ && mv
/tmp/hugo_${HUGO_VERSION}_linux_amd64/hugo_${HUGO_VERSION}_linux_amd64
/usr/bin/hugo && rm -rf /tmp/*  

