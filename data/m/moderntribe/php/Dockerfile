FROM php:5.6-apache  
  
MAINTAINER Modern Tribe  
  
# required libs for extensions  
RUN apt-get update && apt-get install -y \  
build-essential wget libmemcached-dev \  
zlib1g-dev libpng12-dev less \  
libssl-dev libc-client2007e-dev libkrb5-dev \  
libpng12-dev libjpeg-dev \  
re2c libmcrypt-dev \  
git \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install exif \  
&& docker-php-ext-configure gd --with-jpeg-dir=/usr/lib \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install gettext \  
&& docker-php-ext-configure imap --with-imap-ssl --with-kerberos \  
&& docker-php-ext-install imap \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install opcache \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install zip \  
&& docker-php-source delete  
  
RUN a2enmod rewrite \  
&& echo "\nInclude /etc/apache2/sites-enabled/*" >> /etc/apache2/apache2.conf
\  
&& echo "\n<Directory /srv/www/>\n\tOptions Indexes
FollowSymLinks\n\tAllowOverride All\n\tRequire all granted\n</Directory>" >>
/etc/apache2/apache2.conf  
  
# memcached extension (2.2.0 is the last to support php 5.6)  
RUN echo '' | pecl install memcached-2.2.0 \  
&& echo "extension=memcached.so" > /usr/local/etc/php/conf.d/ext-memcached.ini  
  
# xdebug extension  
RUN echo '' | pecl install xdebug \  
&& echo "zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20131226/xdebug.so" > /usr/local/etc/php/conf.d/ext-xdebug.ini \  
&& echo "xdebug.remote_enable=1" >> /usr/local/etc/php/conf.d/ext-xdebug.ini \  
&& echo "xdebug.remote_autostart=0" >> /usr/local/etc/php/conf.d/ext-
xdebug.ini \  
&& echo "xdebug.remote_connect_back=1" >> /usr/local/etc/php/conf.d/ext-
xdebug.ini \  
&& echo "xdebug.remote_port=9000" >> /usr/local/etc/php/conf.d/ext-xdebug.ini
\  
&& echo "xdebug.force_display_errors=1" >> /usr/local/etc/php/conf.d/ext-
xdebug.ini  
  
# WP CLI  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar \  
&& chmod +x wp-cli.phar \  
&& mv wp-cli.phar /usr/local/bin/wp  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Set Workdir  
WORKDIR /srv/www

