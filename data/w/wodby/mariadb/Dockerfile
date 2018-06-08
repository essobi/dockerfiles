FROM wodby/base:0.1  
MAINTAINER Wodby <hello@wodby.com>  
  
COPY rootfs /  
  
RUN apk add --update mariadb \  
mariadb-client \  
pwgen \  
nmap \  
&& mkdir -p /var/lib/mysql \  
&& rm -rf /var/cache/apk/*

