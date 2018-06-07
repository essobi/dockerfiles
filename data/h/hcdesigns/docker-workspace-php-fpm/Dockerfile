FROM php:7.0-fpm  
  
LABEL maintainer="Harvey Chow <harvey@hcdesigns.nl>"  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
curl \  
libmemcached-dev \  
libz-dev \  
libpq-dev \  
libjpeg-dev \  
libpng12-dev \  
libfreetype6-dev \  
libssl-dev \  
libmcrypt-dev \  
libxml2-dev \  
zlib1g-dev \  
libicu-dev \  
g++  
  
RUN docker-php-ext-install soap  
RUN docker-php-ext-install mcrypt  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install mysqli  
  
#####################################  
# gd:  
#####################################  
  
# Install the PHP gd library  
RUN docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-jpeg-dir=/usr/lib \  
\--with-freetype-dir=/usr/include/freetype2 && \  
docker-php-ext-install gd  
  
#####################################  
# xDebug:  
#####################################  
  
RUN pecl install xdebug && \  
docker-php-ext-enable xdebug  
  
COPY ./xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini  
  
#####################################  
# Opcache:  
#####################################  
  
RUN docker-php-ext-install opcache  
COPY ./opcache.ini /usr/local/etc/php/conf.d/opcache.ini  
  
#####################################  
# PHP REDIS  
#####################################  
  
RUN pecl install -o -f redis \  
&& rm -rf /tmp/pear \  
&& docker-php-ext-enable redis  
  
#####################################  
# Human Language and Character Encoding Support:  
#####################################  
  
RUN docker-php-ext-configure intl && \  
docker-php-ext-install intl  
  
RUN usermod -u 1000 www-data  
  
WORKDIR /var/www  
  
EXPOSE 9000  
CMD ["php-fpm"]  

