FROM php:7.0-fpm  
  
MAINTAINER Shapovalov Alexandr <alex_sh@kodeks.ru>  
  
ADD ./site.ini /usr/local/etc/php/conf.d  
ADD ./site.pool.conf /usr/local/etc/php-fpm.d/  
  
RUN apt-get update && apt-get install -y \  
libpq-dev \  
libmemcached-dev \  
curl \  
msmtp  
  
# Install extensions using the helper script provided by the base image  
RUN docker-php-ext-install \  
pdo_mysql \  
pdo \  
mysqli \  
pdo_pgsql  
  
# Install Memcached for php 7  
RUN curl -L -o /tmp/memcached.tar.gz "https://github.com/php-memcached-
dev/php-memcached/archive/php7.tar.gz" \  
&& mkdir -p /usr/src/php/ext/memcached \  
&& tar -C /usr/src/php/ext/memcached -zxvf /tmp/memcached.tar.gz --strip 1 \  
&& docker-php-ext-configure memcached \  
&& docker-php-ext-install memcached \  
&& rm /tmp/memcached.tar.gz  
  
RUN usermod -u 1000 www-data  
  
WORKDIR /var/www  
  
CMD ["php-fpm"]  
  
EXPOSE 9000

