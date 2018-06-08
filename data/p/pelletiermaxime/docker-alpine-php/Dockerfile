FROM alpine  
  
RUN apk add --no-cache php5-fpm  
  
COPY php-fpm.conf /etc/php5/  
  
EXPOSE 9000  
CMD ["php-fpm"]  

