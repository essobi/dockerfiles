FROM alpine:3.4  
MAINTAINER Geshan Manandhar (http://geshan.com.np)  
  
RUN apk add --no-cache curl rsync openssh &&\  
apk add --no-cache fabric --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted  
  
WORKDIR /app  
  
VOLUME /app  

