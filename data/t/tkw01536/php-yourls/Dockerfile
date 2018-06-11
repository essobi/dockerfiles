FROM php:7-apache-stretch  
  
ADD errorlevel.ini /usr/local/etc/php/conf.d  
  
RUN docker-php-ext-install pdo pdo_mysql \  
&& a2enmod rewrite  
  
# We are serving our website under port 80  
EXPOSE 80  
VOLUME /var/www/html  

