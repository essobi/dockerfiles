FROM mitcdh/caddy  
MAINTAINER Mitchell Hewes <me@mitcdh.com>  
  
# install php  
RUN apk --update add \  
php7-apcu \  
php7-bcmath \  
php7-ctype \  
php7-curl \  
php7-dom \  
php7-fpm \  
php7-gd \  
php7-iconv \  
php7-intl \  
php7-json \  
php7-mbstring \  
php7-opcache \  
php7-openssl \  
php7-pdo \  
php7-pdo_sqlite \  
php7-phar \  
php7-session \  
php7-sqlite3 \  
php7-xml \  
php7-xmlreader \  
php7-zlib \  
php7-zip \  
&& rm -rf /var/cache/apk/* \  
&& { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=2'; \  
echo 'opcache.fast_shutdown=1'; \  
} > /etc/php7/conf.d/opcache-recommended.ini \  
&& ln -s /etc/php-fpm7 /etc/php-fpm \  
&& ln -s /usr/sbin/php-fpm7 /usr/sbin/php-fpm \  
&& ln -s /usr/bin/php7 /usr/bin/php  
  
ADD files/php-fpm.conf /etc/php7/php-fpm.conf  

