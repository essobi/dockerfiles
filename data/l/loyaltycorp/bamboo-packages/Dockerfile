FROM php:7  
# Update apt sources  
RUN apt-get update  
  
# Install os packages  
RUN apt-get install -y bc git  
  
# Install php extensions  
RUN pecl install xdebug \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \  
&& apt-get install -y libmemcached-dev zlib1g-dev \  
&& docker-php-ext-install zip \  
&& echo '' | pecl install memcached \  
&& echo "extension=$(find /usr/local/lib/php/extensions/ -name memcached.so)"
> /usr/local/etc/php/conf.d/memcached.ini  
  
# Install composer  
RUN php -r "readfile('http://getcomposer.org/installer');" | php -- --install-
dir=/usr/local/bin/ --filename=composer  

