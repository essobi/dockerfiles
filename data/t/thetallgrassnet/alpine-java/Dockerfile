FROM alpine:3.3  
  
MAINTAINER Jesse B. Hannah <jesse@jbhannah.net>  
  
RUN apk add openjdk8-jre-base --update-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted \  
&& rm -rf /var/cache/apk/*  

