FROM php:5.6-apache  
  
#COPY config/php.ini /usr/local/etc/php  
RUN a2enmod rewrite  
  
# Install modules  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ \  
&& docker-php-ext-install gd  
  
RUN ln -s /var/www/html/bin/codecept.sh /usr/local/bin/codecept  
  
#CMD ["php"]

