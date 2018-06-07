FROM php:fpm  
  
MAINTAINER Mohamed-Touhami MAHDI <mohamed.touhamimahdi@jacobs-esa.com>  
  
RUN apt-get update && apt-get install -y wkhtmltopdf \  
libldap2-dev libicu-dev libxml2-dev zlib1g-dev \  
libfreetype6-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& pecl install apcu \  
&& pecl install redis \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \  
&& docker-php-ext-install -j$(nproc) bcmath pdo_mysql soap ldap intl mbstring
iconv xml opcache zip gd \  
&& docker-php-ext-enable apcu redis  
  
RUN apt-get -y autoremove libldap2-dev libicu-dev libxml2-dev zlib1g-dev  
  
RUN echo "memory_limit=4G" > /usr/local/etc/php/conf.d/docker-php-ext-
memory.ini \  
&& echo "upload_max_filesize = 40M" > /usr/local/etc/php/conf.d/docker-php-
ext-uplodad.ini \  
&& echo "post_max_size = 40M" >> /usr/local/etc/php/conf.d/docker-php-ext-
uplodad.ini \  
&& echo "expose_php = Off" > /usr/local/etc/php/conf.d/docker-php-ext-
config.ini  

