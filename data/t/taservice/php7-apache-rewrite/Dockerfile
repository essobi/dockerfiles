FROM php:7-apache-jessie  
#MAINTAINER alvin.z <alvin.z.ca@gmail.com>  
  
ENV TZ=America/Toronto  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
libmagickwand-dev \  
libmemcached-dev \  
libssl-dev \  
libmcrypt-dev \  
libz-dev \  
libicu-dev \  
libcurl4-openssl-dev \  
libc-client-dev \  
libkrb5-dev \  
libpq-dev  
  
# libpng12-dev \  
# libxml2-dev \  
# libbz2-dev  
RUN docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ \  
&& docker-php-ext-configure imap --with-imap-ssl --with-kerberos \  
&& docker-php-ext-install -j$(nproc) gd iconv mcrypt mysqli pdo pdo_mysql
shmop soap zip intl json mbstring imap curl  
  
  
# Imagick  
RUN pecl install imagick \  
&& docker-php-ext-enable imagick  
  
# Memcached  
RUN pecl install memcached \  
&& docker-php-ext-enable memcached  
  
# Enable Apache mod_rewrite ssl  
RUN a2enmod rewrite  
EXPOSE 80  

