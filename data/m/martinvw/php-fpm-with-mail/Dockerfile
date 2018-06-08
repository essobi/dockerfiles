FROM php:7-fpm-alpine  
  
RUN apk --no-cache add msmtp  
RUN touch /var/log/msmtp.log && chown www-data: /var/log/msmtp.log  
  
COPY php.ini /usr/local/etc/php/php.ini  

