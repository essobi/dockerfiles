FROM nginx  
  
MAINTAINER Dennis Clark <boomfish@gmail.com>  
  
# NGINX config  
  
COPY config/nginx/conf.d/ /etc/nginx/conf.d/  
  
# Dummy self-signed SSL certificate for local development  
RUN mkdir -p /etc/nginx/ssl/default  
RUN openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -subj
"/CN=*.localtest.me" -keyout /etc/nginx/ssl/default/server.key -out
/etc/nginx/ssl/default/server.crt  

