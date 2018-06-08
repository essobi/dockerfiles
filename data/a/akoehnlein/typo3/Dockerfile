FROM php:7.0-apache  
  
# Install packages  
RUN apt-get update \  
&& apt-get install -y \  
libxml2-dev libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
imagemagick \  
zlib1g-dev \  
&& apt-get clean  
  
# Configure PHP  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) mysqli soap gd zip  
# memory workaround, see https://stackoverflow.com/a/39535288/7358195  
RUN echo 'pcre.jit=0' > /usr/local/etc/php/conf.d/workaround.ini  
  
# XDebug  
RUN pecl install xdebug \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/xdebug-extension.ini  
  
# add configuration files  
COPY additional/php-* /usr/local/etc/php/conf.d/  
  
# Configure Apache as needed  
RUN a2enmod rewrite  
  
WORKDIR /var/www  

