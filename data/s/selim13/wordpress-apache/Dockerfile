FROM php:7.1-apache  
  
MAINTAINER Dmitry Seleznyov <selim013@gmail.com>  
  
RUN a2enmod rewrite expires  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y msmtp libpng12-dev libjpeg-dev && rm
-rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mysqli opcache  
  
COPY php/opcache-recomended.ini /usr/local/etc/php/conf.d/  
COPY php/msmtp.ini /usr/local/etc/php/conf.d/  
COPY php/upload.ini /usr/local/etc/php/conf.d/  
  
RUN mkdir -p /tmp/opcache \  
&& chown -R www-data:www-data /tmp/opcache \  
&& chown www-data:www-data /var/www/html  
  
### WP-CLI  
RUN curl -SL https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar -o /usr/local/bin/wp-cli \  
&& chmod +x /usr/local/bin/wp-cli  
  
# Force wp-cli not to run less  
ENV PAGER=cat  
  
VOLUME /var/www/html  
  
CMD ["apache2-foreground"]  

