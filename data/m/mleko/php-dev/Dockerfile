FROM php:7.1  
MAINTAINER Daniel Król <daniel@krol.me>  
  
RUN apt-get update -yqq && apt-get install git libzip-dev zlib1g-dev openssh-
client -yqq  
  
RUN docker-php-ext-install zip calendar bcmath  
  
RUN yes | pecl install xdebug \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini  
  
# Install composer and put binary into $PATH  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/ \  
&& ln -s /usr/local/bin/composer.phar /usr/local/bin/composer  

