FROM php:5.6-apache  
  
LABEL maintainer "Gary Kramlich <grim@reaperworld.com>"  
  
COPY . /var/www  
  
RUN mv /var/www/html /var/www/html.old; ln -s /var/www/htdocs /var/www/html  
  

