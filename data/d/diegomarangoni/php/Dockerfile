FROM php:5.6  
MAINTAINER "Diego Marangoni" <https://github.com/diegomarangoni>  
  
ENV APCU_VERSION 4.0.10  
ENV MEMCACHE_VERSION 3.0.8  
ENV MONGO_VERSION 1.6.12  
ENV XDEBUG_VERSION 2.3.3  
RUN buildDeps=" \  
libssl-dev \  
zlib1g-dev \  
libicu-dev \  
libmcrypt-dev \  
libxml2-dev \  
libmemcached-dev \  
libjpeg-dev \  
libpng12-dev \  
" \  
extraPkgs=" \  
git \  
nodejs \  
npm \  
"\  
&& set -x \  
&& apt-get update \  
&& apt-get install -y $buildDeps $extraPkgs \--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& { yes 'no' | pecl install mongo-$MONGO_VERSION; } \  
&& { yes '' | pecl install apcu-$APCU_VERSION; } \  
&& { yes '' | pecl install memcache-$MEMCACHE_VERSION; } \  
&& pecl install xdebug-$XDEBUG_VERSION \  
&& docker-php-ext-install intl zip pdo_mysql mcrypt soap gd mbstring \  
&& docker-php-ext-enable mongo apcu opcache memcache \  
&& echo 'date.timezone="UTC"' > /usr/local/etc/php/conf.d/date-timezone.ini \  
&& npm install -g less  
  
RUN php -r "readfile('https://getcomposer.org/installer');" > composer-
setup.php \  
&& php -r "if (hash('SHA384', file_get_contents('composer-setup.php')) !==
'781c98992e23d4a5ce559daf0170f8a9b3b91331ddc4a3fa9f7d42b6d981513cdc1411730112495fbf9d59cffbf20fb2')
{ echo 'Installer corrupt'; unlink('composer-setup.php'); }" \  
&& php composer-setup.php --install-dir=/usr/bin --filename=composer \  
&& php -r "unlink('composer-setup.php');"  

