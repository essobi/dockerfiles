FROM php:7.1-fpm  
MAINTAINER Sylvain Deloux <docker@eax.fr>  
  
  
ENV DEBIAN_FRONTEND noninteractive  
  
  
# Packages  
RUN apt-get update && \  
apt-get install -y git wget zip unzip libicu-dev libmcrypt-dev libcurl3-dev
zlib1g-dev libssl-dev libmagickwand-dev jpegoptim && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# PHP exensions  
RUN docker-php-ext-install intl  
RUN docker-php-ext-install gd  
RUN docker-php-ext-install ftp  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install opcache  
RUN docker-php-ext-install mcrypt  
RUN docker-php-ext-install curl  
RUN docker-php-ext-install zip  
RUN docker-php-ext-install exif  
RUN docker-php-ext-install pcntl  
  
RUN pecl install imagick && \  
docker-php-ext-enable imagick && \  
pecl clear-cache && \  
rm -rf /tmp/*  
  
RUN pecl install mongodb && \  
docker-php-ext-enable mongodb && \  
pecl clear-cache && \  
rm -rf /tmp/*  
  
# Composer  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_PROCESS_TIMEOUT 300  
RUN curl -s https://getcomposer.org/installer | php && \  
chmod +x composer.phar && \  
mv composer.phar composer && \  
mv composer /usr/bin  
  
# Xdebug  
RUN pecl install xdebug && \  
docker-php-ext-enable xdebug && \  
pecl clear-cache && \  
rm -rf /tmp/*  
  
# Finish build  
RUN usermod -u 1000 www-data  

