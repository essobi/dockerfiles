FROM composer AS vendor-env  
COPY composer.* /app/  
RUN composer install --no-dev --no-suggest  
  
FROM search2d/php:7.1.9-1  
COPY docker/php/php.ini /usr/local/etc/php/php.ini  
COPY . /var/www  
COPY \--from=vendor-env /app/vendor /var/www/vendor  
RUN chown -R www-data:www-data /var/www  
WORKDIR /var/www

