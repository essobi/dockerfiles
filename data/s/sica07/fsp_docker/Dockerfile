FROM php:5.6-fpm  
  
RUN apt-get update --no-install-recommends \  
&& apt-get -yq upgrade --no-install-recommends \  
&& apt-get -yq install --no-install-recommends \  
mysql-client \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libmemcached-dev \  
libxml2-dev \  
libc-client2007e-dev \  
libkrb5-dev \  
libcurl4-openssl-dev \  
wget \  
unzip \  
&& docker-php-ext-configure imap --with-kerberos --with-imap-ssl \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd iconv mcrypt mbstring ctype soap imap curl pdo
pdo_mysql zip  
  
COPY php.ini /usr/local/etc/php/php.ini  
  
#EXPOSE 9000  
#ENTRYPOINT ["/usr/sbin/php5-fpm", "-F"]  

