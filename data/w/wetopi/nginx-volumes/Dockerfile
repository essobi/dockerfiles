FROM debian:jessie  
  
MAINTAINER joan joan@inte.es  
  
RUN mkdir /etc/nginx \  
&& mkdir /etc/nginx/conf.d \  
&& mkdir /etc/nginx/certs \  
&& mkdir /etc/nginx/vhost.d \  
&& mkdir /usr/share/nginx \  
&& mkdir /usr/share/nginx/html  
  
VOLUME
["/etc/nginx/conf.d","/etc/nginx/certs","/etc/nginx/vhost.d","/usr/share/nginx/html"]  
  
COPY html /usr/share/nginx/html  
  
CMD ["echo", "'Data-only'"]  

