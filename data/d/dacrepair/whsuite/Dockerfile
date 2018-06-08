FROM php:5.6-apache  
ENV PHP_EXTRA_CONFIGURE_ARGS: --with-apxs2 --with-pdo-mysql=shared --with-
mcrypt  
  
RUN a2enmod rewrite  
RUN docker-php-ext-install pdo pdo_mysql  
RUN pecl install mailparse-2.1.6  
RUN echo 'extension=mailparse.so' > /usr/local/etc/php/conf.d/10-mailparse.ini  
RUN apt-get update  
RUN apt-get -y install libmcrypt-dev  
RUN rm -rf /var/lib/apt/lists/*  
  
WORKDIR /var/www/html  
  
EXPOSE 80  
CMD ["apache2-foreground"]  

