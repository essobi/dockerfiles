FROM php:7.1.16-fpm  
  
ARG ENVIRONMENT=local  
  
WORKDIR /tmp  
  
# Needs for composer  
RUN apt-get update && \  
apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
sendmail \  
git -y  
# allow root for php-fpm  
# Some basic extensions  
RUN docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) json mbstring zip pdo pdo_mysql mysqli
iconv mcrypt gd exif  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
composer self-update && \  
composer global require "hirak/prestissimo:^0.3" && \  
apt-get remove --purge curl -y && \  
apt-get clean

