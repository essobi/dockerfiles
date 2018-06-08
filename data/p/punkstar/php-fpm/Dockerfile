FROM php:7.1-fpm  
  
MAINTAINER Nick Jones <nick@nicksays.co.uk>  
  
RUN apt-get update \  
&& apt-get install -y libmcrypt-dev libpng12-dev libfreetype6-dev
libjpeg62-turbo-dev libxml2-dev libxslt1-dev sendmail-bin sendmail libicu-dev
git vim \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && docker-php-ext-install gd  
RUN docker-php-ext-install mbstring  
RUN docker-php-ext-install mcrypt  
RUN docker-php-ext-install pcntl  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install soap  
RUN yes | pecl install xdebug && docker-php-ext-enable xdebug  
RUN docker-php-ext-install xsl  
RUN docker-php-ext-install zip  
RUN docker-php-ext-install intl  
  
ENV PHP_EXT_APCU_VERSION "5.1.7"  
RUN yes "" | pecl install apcu-$PHP_EXT_APCU_VERSION && docker-php-ext-enable
apcu  

