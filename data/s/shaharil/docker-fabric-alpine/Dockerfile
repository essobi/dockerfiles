FROM alpine:3.4  
MAINTAINER Geshan Manandhar (http://geshan.com.np)  
MAINTAINER Shahar Levin  
  
RUN apk add --no-cache curl rsync openssh python py-jinja2 &&\  
apk add --no-cache fabric --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted  
  
WORKDIR /app  
  
VOLUME /app  

