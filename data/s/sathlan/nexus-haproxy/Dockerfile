FROM haproxy:1.6-alpine  
LABEL date="Thu Aug 11 18:06:39 CEST 2016"  
  
MAINTAINER <sofer@sathlan.org>  
# For testing.  
RUN apk add --update procps && rm -rf /var/cache/apk/*  
  
COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg  

