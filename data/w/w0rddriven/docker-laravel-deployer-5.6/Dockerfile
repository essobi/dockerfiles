FROM php:5.6-fpm  
  
MAINTAINER Jeremy Brayton <jeremy@braytonium.com>  
  
# apt-get required packages  
RUN apt-get update -yqq && apt-get install -yqq git openssh-client zlib1g-dev  
  
# PHP extension installation  
RUN docker-php-ext-install pdo_mysql zip  
  
# Install ssh2  
#RUN apt-get install -yqq libssh2-1 libssh2-1-dev \  
# && pecl install ssh2 \  
# && docker-php-ext-enable ssh2  
# Install xdebug  
#RUN pecl install xdebug \  
# && docker-php-ext-enable xdebug  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Environmental variables  
ENV COMPOSER_HOME /root/.composer  
ENV COMPOSER_CACHE_DIR /cache  
ENV PATH /root/.composer/vendor/bin:$PATH  
  
# Install composer parallel downloads  
RUN composer global require "hirak/prestissimo:^0.3"  
  
# Install deployer  
RUN composer global require "deployer/deployer:~3.3"  
RUN composer global require "deployphp/recipes:~3.1"  
  
# Install PHP SSH2 extension  
#RUN composer global require "herzult/php-ssh:~1.1"  

