FROM php:7.1-fpm  
  
ENV XDEBUG_ENABLED 0  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
gettext-base \  
mysql-client \  
libmemcached-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libmemcached-dev \  
libpng-dev \  
libxml2-dev \  
curl \  
git-core \  
&& rm -r /var/lib/apt/lists/* \  
&& pecl install memcached \  
&& pecl install xdebug \  
&& docker-php-ext-install -j$(nproc) mbstring \  
&& docker-php-ext-install -j$(nproc) pdo_mysql \  
&& docker-php-ext-install -j$(nproc) zip \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-enable memcached \  
&& docker-php-ext-install soap \  
&& docker-php-ext-install mcrypt  
  
RUN curl -Ss https://getcomposer.org/composer.phar > /usr/local/bin/composer
&& chmod +x /usr/local/bin/composer  
  
RUN composer global require hirak/prestissimo  
  
ADD conf/php.ini /usr/local/etc/php/conf.d/php.ini  
ADD conf/www.conf /usr/local/etc/php-fpm.d/www.conf  
  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
WORKDIR /var/www  
  
EXPOSE 9000  
CMD ["php-fpm"]  

