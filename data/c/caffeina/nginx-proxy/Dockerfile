FROM jwilder/nginx-proxy:alpine  
MAINTAINER Fabien Herfray <herfray.fabien@gmail.com>  
  
ADD https://github.com/kreuzwerker/envplate/releases/download/v0.0.8/ep-linux
/usr/local/bin/ep  
RUN chmod u+x /usr/local/bin/ep  
  
COPY docker-entrypoint.sh /app/docker-entrypoint.sh  
COPY nginx.tmpl /app/nginx.tmpl  
COPY cors.conf /etc/nginx/cors.conf  
COPY common /etc/nginx/vhost.d/common  
COPY common_location /etc/nginx/vhost.d/common_location  
  
VOLUME /etc/nginx/vhost.d  
VOLUME /usr/share/nginx/html  

