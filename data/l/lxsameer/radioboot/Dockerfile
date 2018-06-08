FROM php:5.6-apache  
  
RUN a2enmod rewrite  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev && rm -rf
/var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd  
RUN docker-php-ext-install mysqli  
  
VOLUME /var/www/html  
  
COPY ./wordpress /usr/src/wordpress  
RUN chown -R www-data:www-data /usr/src/wordpress  
  
COPY docker-entrypoint.sh /entrypoint.sh  
COPY config/apache/config /etc/apache2/sites-enabled/000-default.conf  
  
# grr, ENTRYPOINT resets CMD now  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

