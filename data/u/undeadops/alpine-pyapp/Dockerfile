FROM undeadops/alpine-python  
  
MAINTAINER Mitch Anderson <@undeadops>  
  
RUN apk add --update \  
nginx \  
&& mkdir -p /etc/nginx/sites-enabled \  
&& mkdir -p /etc/nginx/ssl \  
&& mkdir /www \  
&& mkdir -p /var/log/nginx \  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 80 443  
  

