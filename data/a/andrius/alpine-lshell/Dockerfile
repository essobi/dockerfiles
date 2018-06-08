# vim:set ft=dockerfile:  
FROM alpine:latest  
  
MAINTAINER Andrius Kairiukstis <andrius@kairiukstis.com>  
  
RUN apk --update --allow-untrusted --repository
http://dl-4.alpinelinux.org/alpine/edge/testing/ add \  
lshell \  
&& rm -rf /var/cache/apk/* /tmp/* /var/tmp/*  

