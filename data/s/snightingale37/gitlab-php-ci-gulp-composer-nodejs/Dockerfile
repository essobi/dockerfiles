FROM php:7.0-fpm  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -yqq  
RUN apt-get install -yqq git libxrender1 wget curl php5-xdebug libicu-dev
libpq-dev libmcrypt-dev libmcrypt4 libgd-dev libcurl4-gnutls-dev zip unzip
php-pear python-pip rhino  
RUN docker-php-ext-install intl pgsql pdo_pgsql mcrypt gd curl opcache
mbstring bcmath  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get install -yqq nodejs  
RUN ln -s /usr/bin/nodejs /usr/local/bin/node  
RUN npm install -g gulp

