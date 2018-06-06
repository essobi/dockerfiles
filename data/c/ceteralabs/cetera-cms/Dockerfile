FROM php:5.6-apache  
RUN apt-get update && apt-get install -y zlib1g-dev libpcre3-dev \  
libpcrecpp0 libfreetype6-dev libjpeg62-turbo-dev libpng12-dev libmcrypt-dev \  
libcurl4-openssl-dev unzip  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install -j$(nproc) zip iconv mcrypt curl mysql mysqli
pdo_mysql gd  
  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=2'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
RUN { \  
echo '[Date]'; \  
echo 'date.timezone = Europe/Moscow'; \  
} > /usr/local/etc/php/php.ini  
  
RUN a2enmod rewrite expires  
VOLUME /var/www/html  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod a+x /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  

