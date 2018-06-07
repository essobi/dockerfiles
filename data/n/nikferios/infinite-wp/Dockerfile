FROM php:7.0-apache  
  
# install the PHP extensions  
RUN set -ex; \  
\  
apt-get update && \  
apt-get install -y \  
libpng12-dev \  
libjpeg-dev \  
libicu-dev \  
libmcrypt-dev \  
libpspell-dev \  
&& rm -rf /var/lib/apt/lists/* \  
\  
&& docker-php-ext-configure \  
gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install \  
gd mysqli opcache intl mcrypt pspell  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=2'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
RUN { \  
echo 'file_uploads = On'; \  
echo 'memory_limit = 256M'; \  
echo 'upload_max_filesize = 32M'; \  
echo 'post_max_size = 32M'; \  
echo 'max_execution_time = 600'; \  
echo 'max_input_vars = 3000'; \  
} > /usr/local/etc/php/conf.d/infinitewp.ini  
  
RUN a2enmod rewrite expires  
  
VOLUME /var/www/html  
  
COPY iwpap.tar.gz /usr/src/  
  
RUN set -ex \  
&& tar -xzf /usr/src/iwpap.tar.gz -C /usr/src/ \  
&& rm /usr/src/iwpap.tar.gz \  
&& chown -R www-data:www-data /usr/src/iwpap/  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["apache2-foreground"]  

