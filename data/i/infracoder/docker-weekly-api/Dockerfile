FROM nginx:1.13-alpine  
  
MAINTAINER Ryan Blunden <ryan.blunden@gmail.com>  
  
RUN rm /etc/nginx/conf.d/default.conf  
  
RUN mkdir -p /var/www/api/v1  
WORKDIR /var/www/  
COPY ./data /var/www/api/v1  
COPY ./conf/docker-weekly-api.conf /etc/nginx/conf.d/  

