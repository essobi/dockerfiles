FROM php:fpm  
MAINTAINER Vincent DAVENEL <vincent@aiglecom.com>  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
ssh \  
vim \  
git \  
wget \  
curl \  
libmemcached-dev \  
libz-dev \  
libpq-dev \  
libjpeg-dev \  
libpng12-dev \  
libfreetype6-dev \  
libssl-dev \  
libmcrypt-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install mcrypt \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-jpeg-dir=/usr/lib \  
\--with-freetype-dir=/usr/include/freetype2 && \  
docker-php-ext-install gd  
  
  
# Install Xdebug  
RUN pecl install xdebug && docker-php-ext-enable xdebug  
COPY ./xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini  
  
# Install ZIP  
RUN pecl install zip && docker-php-ext-enable zip  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  

