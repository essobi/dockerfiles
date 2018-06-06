FROM php:5.6-apache  
MAINTAINER Tobias Sette <contato@tobias.ws>  
LABEL version="0.1"  
LABEL description="My image for PHP with some extensions and configurations"  
  
ENV XDEBUG_VERSION 2.3.3  
# Configure timezone  
# TODO to use ENV var  
RUN ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime &&\  
cat /usr/src/php/php.ini-production | sed 's/^;\\(date.timezone.*\\)/\1
\"America\/Sao_Paulo\"/' > /usr/local/etc/php/php.ini  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin -- --filename=composer  
  
# Install and configure PHP extensions  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mysql \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install zip  
  
# Intall Xdebug  
# https://xdebug.org/docs/install  
RUN cd /usr/src/php/ext/ \  
; mkdir xdebug-$XDEBUG_VERSION \  
; curl -sS -L "http://xdebug.org/files/xdebug-$XDEBUG_VERSION.tgz" | tar -zxf
- -C "xdebug-$XDEBUG_VERSION" \  
&& mv "xdebug-$XDEBUG_VERSION/xdebug-$XDEBUG_VERSION" xdebug \  
&& docker-php-ext-install xdebug  
  
# Enable apache modules  
RUN a2enmod rewrite  
  

