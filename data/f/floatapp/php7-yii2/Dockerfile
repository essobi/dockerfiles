# docker build -t floatapp/php7-yii2:latest .  
FROM php:7.1.14-apache  
LABEL maintainer="tech@float.com"  
  
# apt-get  
RUN apt-get update && apt-get -y install \  
bzip2 git nano wget zip unzip \  
libmcrypt-dev libzzip-dev zziplib-bin zlib1g-dev \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# docker-php ext-install:  
RUN docker-php-ext-install mcrypt && docker-php-ext-install zip \  
&& docker-php-ext-install pdo_mysql  
  
# opcache  
RUN docker-php-ext-install opcache  
  
# phpredis  
RUN pecl install redis-3.1.2 \  
&& docker-php-ext-enable redis  
  
# optional net & proc tools:  
# RUN apt-get -y install net-tools netcat telnet procps  
# rsyslog: (optional: for Loggly etc)  
# RUN apt-get update && apt-get -y install rsyslog && apt-get clean  
# RUN sed -i '1s/^/$MaxMessageSize 64k\n/' /etc/rsyslog.conf  
# apache mods:  
RUN a2enmod rewrite  
# if desired:  
# && a2enmod headers  
# composer:  
COPY composer-install.sh /tmp  
RUN /tmp/composer-install.sh && mv /usr/local/bin/composer.phar
/usr/local/bin/composer  
  
# copy pre-customized php ini files:  
COPY docker/php/etc-php/conf-d /usr/local/etc/php/conf.d/  
COPY docker/php/etc-php/php.ini /usr/local/etc/php/php.ini  
  
COPY ./www/html /var/www/html  
COPY ./www/composer.json /var/www/composer.json  
  
RUN chown -R www-data /var/www  
USER www-data  
WORKDIR /var/www  
RUN mkdir -p /var/www/runtime  
  
RUN /usr/local/bin/composer install --no-dev -o  
  
USER root

