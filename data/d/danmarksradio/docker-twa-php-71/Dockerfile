FROM php:7.1-fpm  
  
LABEL Description="This docker container provides PHP binaries and
configuration"  
LABEL Vendor="Danish Broadcasting Corporation"  
LABEL Version="1.0.0"  
LABEL Team="Team Web API" \  
Team.mail="dl-TeamWebAPI@dr.dk"  
  
RUN apt-get update \  
&& apt-get install -y curl wget git zlib1g-dev libicu-dev g++ libpng12-dev
libjpeg-dev libmcrypt-dev libxml2-dev libpq-dev nano vim libbz2-dev
libfontconfig  
  
RUN echo 'date.timezone = Europe/Copenhagen' >
/usr/local/etc/php/conf.d/date.ini  
  
RUN docker-php-ext-configure intl \  
&& docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \  
&& docker-php-ext-install pdo pdo_mysql pdo_pgsql zip mysqli pcntl shmop
sysvmsg sysvsem sysvshm mcrypt soap gd mbstring gettext intl bcmath json iconv
session bz2  
  
RUN pecl install mongodb \  
&& docker-php-ext-enable mongodb  
  
ENV PHPREDIS_VERSION 3.1.6  
RUN mkdir -p /usr/src/php/ext/redis \  
&& curl -L
https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz | tar
xvz -C /usr/src/php/ext/redis --strip 1 \  
&& echo 'redis' >> /usr/src/php-available-exts \  
&& docker-php-ext-install redis  
  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
RUN usermod -u 1000 www-data  
RUN mkdir -p /var/log/php  
RUN mkdir -p /php/session  
RUN chown www-data:www-data -R /php  
RUN chown www-data:www-data -R /var/www  
  
COPY php-conf.d/php.ini /usr/local/etc/php/conf.d  
COPY php-conf.d/php-fpm.conf /usr/local/etc/php-fpm.conf  
  
USER www-data  
  
WORKDIR /var/www/application  

