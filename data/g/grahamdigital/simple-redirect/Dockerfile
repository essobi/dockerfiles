FROM gliderlabs/alpine  
MAINTAINER Adam Simpson <asimpson@grahamdigital.com>  
  
RUN apk-install nginx-lua && mkdir /tmp/nginx && mkdir -p /run/nginx  
  
COPY ./nginx.conf /etc/nginx/nginx.conf  
  
ENTRYPOINT nginx  

