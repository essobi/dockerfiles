FROM php:7.0-fpm-alpine  
  
# install the PHP extensions we need  
RUN apk add --no-cache libpng-dev libjpeg-turbo-dev bash \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mysqli opcache  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
VOLUME /var/www/html  
  
ENV WORDPRESS_VERSION 4.6.1  
# upstream tarballs include ./wordpress/ so this gives us /usr/src/wordpress  
RUN curl -o wordpress.tar.gz -SL
https://ja.wordpress.org/wordpress-${WORDPRESS_VERSION}-ja.tar.gz \  
&& tar -xzf wordpress.tar.gz -C /usr/src/ \  
&& rm wordpress.tar.gz \  
&& chown -R www-data:www-data /usr/src/wordpress  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
# grr, ENTRYPOINT resets CMD now  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["php-fpm"]

