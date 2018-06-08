FROM php:7.2-fpm-alpine3.7  
  
MAINTAINER Will Riches <will@rich.es>  
  
RUN apk update \  
&& apk add --update --no-cache --virtual .build-deps autoconf make g++ \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& ln -snf /usr/share/zoneinfo/Europe/London /etc/localtime && echo
Europe/London > /etc/timezone \  
&& printf '[PHP]\ndate.timezone = "%s"\n', Europe/London >
/usr/local/etc/php/conf.d/tzone.ini \  
&& docker-php-ext-install pdo pdo_mysql opcache mysqli exif \  
&& pecl install -o -f redis \  
&& rm -rf /tmp/pear \  
&& docker-php-ext-enable redis \  
&& pecl install xdebug-2.6.0beta1 \  
&& docker-php-ext-enable xdebug \  
&& echo "error_reporting = E_ALL" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "display_startup_errors = On" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "display_errors = On" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.remote_enable=1" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.remote_connect_back=1" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& echo "xdebug.idekey=\"PHPSTORM\"" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "xdebug.remote_port=9001" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "php_admin_flag[log_errors] = on">>/usr/local/etc/php-fpm.d/www.conf \  
&& echo "php_admin_value[error_reporting] = E_ALL">>/usr/local/etc/php-
fpm.d/www.conf \  
&& rm -r /usr/src/ \  
&& rm /usr/local/bin/phpdbg \  
&& apk del .build-deps  

