# from https://www.drupal.org/requirements/php#drupalversions  
FROM php:7.1-fpm  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev libpq-dev
nano \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mbstring pdo pdo_mysql pdo_pgsql zip opcache
bcmath  
  
# install phpredis extension  
ENV PHPREDIS_VERSION 3.1.4  
RUN curl -L -o /tmp/redis.tar.gz
https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz \  
&& tar xfz /tmp/redis.tar.gz \  
&& rm -r /tmp/redis.tar.gz \  
&& mkdir /usr/src/php/ext -p \  
&& mv phpredis-$PHPREDIS_VERSION /usr/src/php/ext/redis \  
&& docker-php-ext-install redis  
  
COPY config/php.ini /usr/local/etc/php/  

