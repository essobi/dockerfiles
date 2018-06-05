FROM php:7.1-fpm-alpine3.4  
MAINTAINER FADIS | MWH <info@ifadis.com>  
  
# General: bash, curl  
# Composer: php-cli, php-json, php-openssl, php-phar  
# Bower: nodejs (node and npm), git  
# Grunt: nodejs (node and npm)  
# Fadis composer deps: php-curl, php-ctype, php-dom, php-iconv, php-mcrypt  
# Postgres: postgresql  
# Suggested (not activated): php-intl, php-gd, php-soap, php-xdebug  
RUN apk add --no-cache \  
bash \  
curl \  
git \  
libpng-dev \  
libmcrypt-dev \  
openssh \  
nodejs \  
postgresql \  
&& apk add --no-cache --virtual .redis-deps \  
autoconf \  
g++ \  
make \  
&& pecl install redis \  
&& docker-php-ext-enable redis \  
&& apk add --no-cache --virtual .php-deps \  
postgresql-dev \  
&& docker-php-ext-install mcrypt pdo_pgsql gd zip \  
&& apk del tzdata .php-deps .redis-deps \  
rm -rf /var/cache/apk/* \  
&& mkdir /www  
  
WORKDIR /tmp  
  
COPY php.ini /usr/local/etc/php/  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
RUN composer global require hirak/prestissimo  
  
# Install bower  
RUN npm install bower -g  
  
# Install grunt  
RUN npm install grunt-cli -g  
  
# Install gitbook-cli  
RUN npm install gitbook-cli -g  
  
WORKDIR /www  
  
VOLUME ["/www"]  
  
CMD ["/bin/bash"]  

