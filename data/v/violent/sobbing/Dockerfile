FROM alpine:latest  
MAINTAINER Caleb Case  
  
RUN apk add sl --update-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ && rm -rf /var/cache/apk/*  
COPY sobbing /usr/local/bin/sobbing  
  
ENTRYPOINT ["/usr/local/bin/sobbing"]  

