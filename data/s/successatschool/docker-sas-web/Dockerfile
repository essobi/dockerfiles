FROM php:5.6-apache  
  
# System packages  
RUN apt-get update -qq \  
&& apt-get install -y build-essential cmake git-core libicu-dev libmemcached-
dev libmemcached11 libmemcachedutil2 libpng-dev libz-dev vim-tiny ssh unzip \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apk/*  
  
# Apache configuration  
COPY config/ssl.conf /etc/apache2/sites-available/  
RUN a2enmod rewrite \  
&& a2enmod ssl \  
&& a2enmod headers \  
&& a2dissite 000-default \  
&& a2ensite ssl \  
&& echo ServerName sas-local.webful.uk >> /etc/apache2/apache2.conf  
  
# PECL / extension builds and install  
RUN pecl install apcu-4.0.11 memcached-2.2.0 xdebug-2.5.5 \  
&& docker-php-ext-enable apcu memcached xdebug \  
&& docker-php-ext-install bcmath gd intl opcache pcntl pdo_mysql sockets  
  
# Enable remote debugging with xdebug  
RUN echo 'xdebug.remote_enable=on' >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo 'xdebug.remote_connect_back=on' >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& echo 'xdebug.remote_autostart=on' >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
  
# PHP configuration  
COPY config/php.ini /usr/local/etc/php/  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
# Composer parallel install plugin  
RUN composer global require hirak/prestissimo  

