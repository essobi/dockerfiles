FROM php:7.1-apache  
  
## https://github.com/docker-
library/docs/tree/9bf4b054099b170702cfb75e3e2a910218a7cfd8/php#php-core-
extensions  
RUN apt-get update && apt-get install -y git-core cron vim \  
libjpeg-dev libmcrypt-dev libpng12-dev libpq-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
&& docker-php-ext-install -j$(nproc) iconv \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr --with-png-dir=/usr
--with-jpeg-dir=/usr \  
&& docker-php-ext-install -j$(nproc) gd mcrypt mysqli opcache pdo pdo_mysql
zip  
  
# Recommended opcache settings -
https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=2'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/docker-ci-opcache.ini  
  
RUN { \  
echo 'log_errors=on'; \  
echo 'display_errors=on'; \  
echo 'upload_max_filesize=100M'; \  
echo 'post_max_size=100M'; \  
echo 'memory_limit=128M'; \  
echo 'date.timezone="UTC"'; \  
} > /usr/local/etc/php/conf.d/docker-ci-php.ini  
  
# install Xdebug.  
RUN pecl install xdebug \  
&& docker-php-ext-enable xdebug  
  
# enable Xdebug remote debugging  
RUN { \  
echo 'xdebug.remote_enable=true'; \  
echo 'xdebug.remote_port=9001'; \  
} >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
  
RUN a2enmod rewrite  
  
COPY ./CodeIgniter-3.1.8 /usr/src/CodeIgniter-3.1.8  
  
RUN chown -R www-data:www-data /usr/src/CodeIgniter-3.1.8 && \  
mv /usr/src/CodeIgniter-3.1.8/system /var/www/codeigniter  
  
COPY docker-entrypoint /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint"]  
CMD ["apache2-foreground"]  

