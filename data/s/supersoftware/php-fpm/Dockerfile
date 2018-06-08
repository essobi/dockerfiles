FROM php:5.6.30-fpm-alpine  
  
# install extensions for wordpress use  
RUN docker-php-ext-install mysqli mysql pdo pdo_mysql  
  
ENTRYPOINT ["docker-php-entrypoint"]  
WORKDIR /var/www/html  
EXPOSE 9000  
CMD ["php-fpm"]  

