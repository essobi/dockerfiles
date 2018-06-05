FROM php:fpm-alpine  
  
#Install core extensions  
RUN apk update \  
&& apk add --no-cache libpng-dev jpeg-dev libwebp-dev libmcrypt-dev freetype-
dev zlib-dev sed \  
&& docker-php-ext-install -j2 mcrypt mysqli gd opcache pdo pdo_mysql zip ldap
json curl dom posix soap xmlrpc tokenizer tidy ftp intl imap exif  
  
#Install PHPRedis  
RUN apk update && apk add --no-cache git \  
&& cd /tmp ; git clone \--branch=php7 https://github.com/phpredis/phpredis.git
\  
&& cd phpredis ; phpize \  
&& ( ./configure && make -j2 && make install ) > /dev/null \  
&& cd / ; rm -fr /tmp/phpredis \  
&& echo "extension=redis.so" > /usr/local/etc/php/conf.d/redis.ini  
  
CMD ["php-fpm"]  

