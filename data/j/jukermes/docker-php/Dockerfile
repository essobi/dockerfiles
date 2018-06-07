FROM php:5.6-fpm  
  
MAINTAINER Julien Kermes <julien.kermes@gmail.com>  
  
RUN apt-get update -yqq  
  
RUN apt-get install -y git  
  
RUN apt-get install -y zlib1g-dev  
  
RUN apt-get install -y libicu-dev  
  
# Dependency for pecl  
RUN apt-get install -y libssl-dev  
  
RUN apt-get install -y phpunit  
  
RUN docker-php-ext-install zip  
  
# Php accelerator  
RUN docker-php-ext-install opcache  
  
RUN pecl install xdebug  
  
RUN pecl install intl  
  
# Don't use it because doctrine/mongodb composer.json relies on ext-mongo
(legacy mongo php driver)  
# see https://github.com/doctrine/mongodb/issues/239  
#RUN pecl install mongodb  
# Legacy mongodb driver  
RUN pecl install mongo  
  
# Composer install  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
RUN usermod -u 1000 www-data  

