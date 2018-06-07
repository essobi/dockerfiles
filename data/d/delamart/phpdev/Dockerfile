FROM php:7.0  
MAINTAINER Erik DeLamarter <erik@delamarter.ch>  
  
RUN apt-get update && apt-get install -y \  
git \  
libsqlite3-dev \  
libzip-dev \  
unzip \  
&& pecl install xdebug \  
&& docker-php-ext-install pdo pdo_sqlite zip \  
&& docker-php-ext-enable xdebug \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_DISABLE_XDEBUG_WARN 1  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN curl -L http://deployer.org/deployer.phar -o /usr/local/bin/dep && chmod
a+x /usr/local/bin/dep  

