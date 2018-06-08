FROM alpine  
# Copyright (C) 2016 js <js@yoga>  
MAINTAINER js @ Generik Ltd  
  
RUN apk add --no-cache nginx && echo "pid /run/nginx.pid;" >>
/etc/nginx/nginx.conf  
  
ARG NIXY_VERSION=0.7.2  
ARG NIXY_RELEASE=nixy_${NIXY_VERSION}_linux_amd64  
  
ADD
https://github.com/martensson/nixy/releases/download/v${NIXY_VERSION}/${NIXY_RELEASE}.tar.gz
/tmp/nixy.tgz  
RUN tar -xzf /tmp/nixy.tgz -C /tmp/ && cp /tmp/${NIXY_RELEASE}/nixy
/usr/local/bin/  
  
ADD nginx.tmpl /etc/nginx/nginx.tmpl  
ADD nixy.toml /etc/nixy.toml  
ADD startup.sh /startup.sh  
  
EXPOSE 6000 7000  
CMD /startup.sh  
  
#vim: syntax=Dockerfile  

