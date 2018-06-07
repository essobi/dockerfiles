from php:7-fpm-alpine  
  
RUN apk add --no-cache \  
libjpeg-turbo-dev libpng-dev freetype-dev libmcrypt-dev bzip2-dev \  
  
&& wget https://github.com/phpredis/phpredis/archive/php7.zip \  
&& unzip php7.zip && rm php7.zip \  
&& mv phpredis-php7/ /usr/src/php/ext/redis \  
  
&& docker-php-ext-configure gd \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
\--with-freetype-dir=/usr/include/ \  
&& docker-php-ext-install gd \  
  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install redis \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install bz2 \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install opcache \  
  
&& echo "== Done =="  
  
CMD ["php-fpm"]  

