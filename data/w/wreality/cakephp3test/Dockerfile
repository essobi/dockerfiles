FROM php:7.0-apache  
MAINTAINER Brian Adams <wreality@gmail.com>  
  
#update apt-get  
RUN apt-get update  
#install the required components  
RUN apt-get install -y \  
libmcrypt-dev \  
g++ \  
libicu-dev \  
libmcrypt4 \  
libicu52 \  
zlib1g-dev \  
git \  
libxml2-dev \  
openssh-client \  
mysql-client \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev  
#install the PHP extensions we need  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install mcrypt  
RUN docker-php-ext-install mbstring  
RUN docker-php-ext-install intl  
RUN docker-php-ext-install zip  
RUN docker-php-ext-install soap  
RUN docker-php-ext-install gd  
  
#####ADD ADDITIONAL INSTALLS OR MODULES BELOW#########  
#####ADD ADDITIONAL INSTALLS OR MODULES ABOVE#########  
#cleanup after the installations  
RUN apt-get purge --auto-remove -y libmcrypt-dev g++ libicu-dev zlib1g-dev  
#delete the lists for apt-get as the take up space we do not need.  
RUN rm -rf /var/lib/apt/lists/*  
  
#install composer globally so that you can call composer directly  
RUN curl -sSL https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# install xdebug for code coverage  
RUN curl -L -o /tmp/xdebug-2.4.1.tgz http://xdebug.org/files/xdebug-2.4.1.tgz
\  
&& tar xfz /tmp/xdebug-2.4.1.tgz \  
&& rm -r /tmp/xdebug-2.4.1.tgz \  
&& docker-php-source extract \  
&& mv xdebug-2.4.1 /usr/src/php/ext/xdebug \  
&& docker-php-ext-install xdebug \  
&& docker-php-source delete  
  
# enable apache rewrite  
RUN a2enmod rewrite  
  
# set www permissions  
RUN usermod -u 1000 www-data  
  

