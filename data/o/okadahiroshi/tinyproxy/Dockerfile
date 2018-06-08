FROM alpine  
  
MAINTAINER Hiroshi Okada <okadahiroshi@miobox.jp>  
  
  
RUN apk update &&\  
apk add tinyproxy  
  
COPY ./tinyproxy.conf /etc/tinyproxy/  
COPY ./entrypoint.sh /  
  
RUN chmod +x /entrypoint.sh &&\  
rm /var/cache/apk/*  
  
ENTRYPOINT /entrypoint.sh  
  

