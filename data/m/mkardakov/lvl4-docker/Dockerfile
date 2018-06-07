FROM php:5.6-apache  
COPY Docker/determine.conf /etc/apache2/sites-available/determine.conf  
  
COPY Docker/ssl.b-pack.com /etc/apache2/ssl.b-pack.com  
COPY Docker/php.ini /usr/local/etc/php/  
  
RUN apt-get update && apt-get install -y \  
libmcrypt-dev \  
libz-dev \  
libmemcached-dev \  
libssl-dev \  
&& rm -r /var/lib/apt/lists/* \  
&& a2enmod rewrite \  
&& a2enmod ssl \  
&& docker-php-ext-install mcrypt mysqli pdo_mysql mysql \  
&& pecl install apcu-4.0.10 \  
&& pecl install memcache-2.2.7 \  
&& pecl install mongo \  
&& pecl install xdebug \  
&& pecl install zip \  
&& docker-php-ext-enable apcu \  
&& docker-php-ext-enable memcache \  
&& docker-php-ext-enable mongo \  
&& docker-php-ext-enable xdebug \  
&& docker-php-ext-enable zip \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /tmp/pear  
  
RUN a2ensite determine.conf  
  
WORKDIR /var/www/determine  
  
RUN chown -R www-data:www-data /var/www/determine  

