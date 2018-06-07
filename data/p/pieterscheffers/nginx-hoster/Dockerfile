FROM node:alpine  
  
# Install docker 17.05.0  
# TODO: download latest from github  
COPY ./bin/* /usr/bin/  
  
RUN mkdir -p /usr/app \  
&& mkdir -p /etc/nginx/conf.d \  
&& mkdir -p /etc/nginx/certs \  
&& mkdir -p /usr/share/nginx/html \  
&& chmod +x /usr/bin/docker  
  
# http://blog.zot24.com/tips-tricks-with-alpine-docker/  
RUN apk --no-cache add openssl  
  
WORKDIR /usr/app  
  
ENTRYPOINT node --trace-warnings /usr/app/index.js  
  
COPY ./package.json /usr/app  
  
RUN [ "npm", "install" ]  
  
ENV PATH /usr/app/node_modules/.bin:$PATH  
  
COPY ./src /usr/app  

