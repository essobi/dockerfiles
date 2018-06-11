FROM alpine:latest  
  
MAINTAINER Olivier Pichon <op@united-asian.com>  
  
RUN apk update && apk add --update \  
curl \  
nginx \  
supervisor \  
&& adduser -D -S -h /var/www -s /sbin/nologin -G www-data www-data \  
&& rm -rf /var/www/localhost \  
&& cp -r /usr/share/nginx/html/* /var/www/  
  
COPY supervisord.conf /etc/supervisord.conf  
  
COPY supervisor.d/nginx.ini /etc/supervisor.d/nginx.ini  
  
COPY entrypoint.sh /entrypoint.sh  
  
COPY entrypoint.d /entrypoint.d  
  
COPY nginx/nginx.conf /etc/nginx/nginx.conf  
  
COPY nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf  
  
WORKDIR /var/www  
  
EXPOSE 80 443  
ONBUILD COPY nginx/conf.d /etc/nginx/conf.d  
  
ONBUILD COPY . /var/www  
  
ENTRYPOINT "/entrypoint.sh"  

