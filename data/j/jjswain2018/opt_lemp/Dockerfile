FROM php:7.0-fpm  
  
#RUN service php restart  
RUN rm /usr/local/etc/php-fpm.conf  
COPY php-fpm.conf /usr/local/etc/php-fpm.conf  
COPY php.ini /usr/local/etc/php.ini  
  
CMD ["php"]  
  

