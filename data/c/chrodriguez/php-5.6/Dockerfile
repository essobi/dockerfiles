FROM php:5.6-apache  
COPY ./envvars /etc/apache2/  
COPY ./000-default.conf /etc/apache2/sites-available/  
RUN a2enmod rewrite && apt-get update && apt-get install -y libmysqlclient-dev
\  
libmemcached-dev \  
libxml2-dev \  
libxslt1-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& pecl install apcu-4.0.11 \  
&& docker-php-ext-enable apcu \  
&& pecl install memcached-2.2.0 \  
&& docker-php-ext-enable memcached \  
&& pecl install memcache-2.2.7 \  
&& docker-php-ext-enable memcache \  
&& docker-php-ext-install mysql \  
&& docker-php-ext-install bcmath \  
&& docker-php-ext-install soap \  
&& docker-php-ext-install xsl \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-
dir=/usr/include \  
&& docker-php-ext-install gd mbstring pdo pdo_mysql zip  
  

