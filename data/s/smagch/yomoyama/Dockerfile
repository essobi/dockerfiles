FROM smagch/yomoyama:php-fpm-7.0.6  
ENV DB_NAME kumoji5  
ENV DB_PASS kumoji5  
ENV DB_PORT 3306  
ENV DB_HOST db  
  
COPY . /var/www/html  
RUN composer install  
  
VOLUME /var/www/html  

