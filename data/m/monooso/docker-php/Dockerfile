FROM php:7.1-fpm  
  
# Install system packages.  
RUN apt-get update && apt-get install -y --fix-missing --no-install-recommends
\  
libcurl4-openssl-dev \  
libmagickwand-dev \  
libmcrypt-dev \  
libmemcached-dev \  
openssl  
  
# Install Composer. Ideally we'd run all Composer commands in a separate.  
# container, but Laravel makes this very difficult, because of the post-*  
# scripts.  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install Git.  
RUN apt-get install -y git  
  
# Install the required PHP extensions.  
# @see https://laravel.com/docs/5.4/installation#server-requirements  
RUN docker-php-ext-install \  
bcmath \  
gd \  
mbstring \  
mcrypt \  
mysqli \  
pcntl \  
pdo \  
pdo_mysql \  
zip  
  
# Install ImageMagick.  
RUN pecl install imagick && docker-php-ext-enable imagick  
  
# Install memcached.  
RUN pecl install memcached && docker-php-ext-enable memcached  
  
# Install xdebug.  
RUN pecl install xdebug && docker-php-ext-enable xdebug  
  
# Customise the PHP configuration.  
COPY ./log.ini /usr/local/etc/php/conf.d/log.ini  
COPY ./upload.ini /usr/local/etc/php/conf.d/upload.ini  
COPY ./xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini  
  
# Tidy up.  
RUN apt-get clean  
  
# Copy the .bashrc.  
COPY ./bashrc /root/.bashrc  
  
VOLUME ["/var/code"]  

