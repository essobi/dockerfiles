FROM h3nrik/nginx-ldap:latest  
  
LABEL maintainer "Feng Zhou <feng.zh@gmail.com>"  
  
ADD nginx-watch.sh /  
  
ADD nginx.conf /etc/nginx/  
  
RUN sed -i '1 i#!/bin/sh\n/nginx-watch.sh &' /run.sh  
  
CMD ["/run.sh"]  

