FROM php:7.1-fpm-alpine  
  
RUN apk add --no-cache postgresql-dev wget autoconf g++ libc-dev make pcre-dev
\  
&& mkdir -p /app/src \  
&& docker-php-ext-install pdo_pgsql \  
&& pecl install apcu \  
&& docker-php-ext-enable apcu \  
&& apk del autoconf g++ libc-dev make pcre-dev \  
&& sed -i -- 's/www-data/nobody/g' /usr/local/etc/php-fpm.d/www.conf  
  
COPY composer.json /app  
COPY src /app/src  
  
RUN wget https://getcomposer.org/composer.phar \  
&& php composer.phar --working-dir=/app install --no-dev --no-interaction
--ignore-platform-reqs \  
&& rm composer.phar  
  
RUN echo "clear_env = no" >> /usr/local/etc/php/php-fpm.conf \  
&& echo "post_max_size = 100M" >> /usr/local/etc/php/php.ini \  
&& echo "upload_max_filesize = 100M" >> /usr/local/etc/php/php.ini  

