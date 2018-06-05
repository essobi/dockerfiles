FROM php:5.6.16-fpm  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev \  
libc-client-dev \  
libkrb5-dev \  
nodejs \  
npm \  
git \  
  
&& printf "\n" | pecl install memcache \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-configure imap --with-imap-ssl --with-kerberos \  
&& docker-php-ext-install mbstring iconv mcrypt gd zip opcache imap  
  
# Install mongo  
RUN pecl install mongo  
RUN echo "extension=mongo.so" > /usr/local/etc/php/conf.d/mongo.ini  
CMD ["php-fpm"]

