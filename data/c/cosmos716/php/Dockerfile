# cosmos PHP 5 based-on PHP 5.5-fpm  
FROM php:5.5-fpm  
MAINTAINER z2493225@gmail.com  
ENV DEBIAN_FRONTEND noninteractive  
  
## Add uid 1000  
RUN adduser --disabled-password --gecos "" cosmos  
  
## PHP composer  
RUN php -r "readfile('https://getcomposer.org/installer');" > /tmp/composer-
setup.php \  
&& php /tmp/composer-setup.php --install-dir=/usr/local/bin
--filename=composer \  
&& rm /tmp/composer-setup.php  
  
## APT  
RUN sed -i 's/httpredir.debian.org/ftp.tw.debian.org/' /etc/apt/sources.list  
  
## PHP extensions  
RUN apt-get update -qq && apt-get install -y \  
git \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libicu-dev \  
libpspell-dev \  
libcurl4-gnutls-dev \  
libmysqlclient-dev \  
libpq-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd intl pspell curl mysql pdo_mysql
mbstring zip pdo_pgsql tokenizer pcntl  
  
## Sendmail  
RUN apt-get install -y ssmtp heirloom-mailx  
  
## Default configurations  
COPY www.conf /usr/local/etc/php-fpm.d/  
COPY sendmail.conf /usr/local/etc/php-fpm.d/  
COPY ssmtp.conf /etc/ssmtp/ssmtp.conf  

