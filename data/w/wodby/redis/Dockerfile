FROM wodby/base:0.1  
MAINTAINER Wodby <hello@wodby.com>  
  
COPY rootfs /  
  
RUN apk add --update redis nmap \  
&& rm -rf /var/cache/apk/*

