FROM richarvey/nginx-php-fpm  
MAINTAINER Pavel Malitov <pavelmalitov@gmail.com>  
  
COPY ./application /var/www/html  
WORKDIR /var/www/html  
RUN composer install  
  
CMD ["/start.sh"]  

