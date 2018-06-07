FROM php:5.6-apache  
  
RUN a2enmod rewrite expires  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev vim && rm
-rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mysqli opcache zip mbstring \  
&& a2enmod headers \  
&& a2enmod ssl \  
&& pecl install apcu-4.0.11 \  
&& echo extension=apcu.so > /usr/local/etc/php/conf.d/apcu.ini  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
echo 'file_uploads=On'; \  
echo 'memory_limit=256M'; \  
echo 'upload_max_filesize=128M'; \  
echo 'post_max_size=128M'; \  
echo 'max_execution_time=1000'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
VOLUME /var/www/html  
  
ENV WORDPRESS_VERSION 4.5.2  
ENV WORDPRESS_SHA1 bab94003a5d2285f6ae76407e7b1bbb75382c36e  
  
# upstream tarballs include ./wordpress/ so this gives us /usr/src/wordpress  
RUN curl -o wordpress.tar.gz -SL
https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz \  
&& echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c - \  
&& tar -xzf wordpress.tar.gz -C /usr/src/ \  
&& rm wordpress.tar.gz \  
&& chown -R www-data:www-data /usr/src/wordpress  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
# grr, ENTRYPOINT resets CMD now  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

