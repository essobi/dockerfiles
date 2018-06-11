FROM debian:jessie  
MAINTAINER Pavel Mironov <wanderermg@gmail.com>  
  
ADD nginx.list /etc/apt/sources.list.d/nginx.list  
ADD http://nginx.org/keys/nginx_signing.key nginx_signing.key  
RUN apt-key add nginx_signing.key && rm nginx_signing.key && apt-get update -y
&& apt-get dist-upgrade -y && apt-get install nginx -y  
ADD nginx/nginx.conf /etc/nginx/nginx.conf  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 80 443  
VOLUME ["/etc/nginx/conf.d"]  
  
CMD ["nginx"]  

