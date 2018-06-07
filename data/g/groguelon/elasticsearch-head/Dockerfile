FROM nginx:1.11-alpine  
  
MAINTAINER Geoffrey ROGUELON <geoffrey.roguelon@gmail.com>  
  
RUN mkdir -p /tmp/head  
  
WORKDIR /tmp/head  
  
COPY . .  
  
RUN apk add --no-cache --virtual build-deps nodejs && \  
npm install -g grunt jasmine && \  
npm install && \  
grunt concat copy && \  
npm uninstall -g grunt jasmine && \  
apk del --purge build-deps && \  
rm -rf /usr/share/nginx/html /root/.npm && \  
mv _site /usr/share/nginx/html && \  
rm -rf /tmp/*  
  
WORKDIR /usr/share/nginx/html  

