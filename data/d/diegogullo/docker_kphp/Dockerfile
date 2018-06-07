FROM php:fpm  
MAINTAINER Diego Gullo <diego_gullo@bizmate.biz>  
  
RUN apt-get update && apt-get install -y zlib1g-dev \  
&& pecl install xdebug \  
&& docker-php-ext-install opcache \  
&& docker-php-ext-enable xdebug \  
&& docker-php-ext-install zip hash \  
&& apt-get clean  
  
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so

