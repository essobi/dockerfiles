FROM php:7-apache  
MAINTAINER Kevin Williams (@llslim) <info@llslim.com>  
  
RUN set -ex \  
&& buildDeps=' \  
libjpeg62-turbo-dev \  
libpng-dev \  
libpq-dev \  
' \  
&& supportServices=' \  
msmtp \  
msmtp-mta \  
' \  
&& markedLibs=' \  
libjpeg62-turbo \  
libpng16-16 \  
libpq5 \  
' \  
&& apt-get update && apt-get install -y --no-install-recommends $buildDeps
$supportServices \  
&& rm -rf /var/lib/apt/lists/* \  
# build php extensions with development dependencies, and install them  
&& docker-php-ext-configure gd \  
\--with-jpeg-dir=/usr \  
\--with-png-dir=/usr \  
&& docker-php-ext-install -j "$(nproc)" gd mbstring opcache pdo pdo_mysql
pdo_pgsql zip \  
# install xdebug extension  
&& touch /usr/local/etc/php/conf.d/xdebug.ini \  
&& pecl channel-update pecl.php.net \  
&& pecl config-set php_ini /usr/local/etc/php/conf.d/xdebug.ini \  
&& pecl install xdebug-2.6.0beta1 \  
# Mark the library packages that were installed with development as manual  
# so the extensions can use them.  
# PHP will issue 'WARNING' messages without these libraries  
&& apt-mark manual $markedLibs \  
# remove unneeded development sources to reduce size of image  
&& apt-get purge -y --auto-remove $buildDeps \  
  
&& a2enmod rewrite  
  
WORKDIR /var/www/html/  

