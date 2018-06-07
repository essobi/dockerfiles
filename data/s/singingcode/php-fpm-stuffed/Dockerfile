FROM php:7.0-fpm  
  
MAINTAINER Singingcode <singingcode@gmail.com>  
  
#  
#--------------------------------------------------------------------------  
# Software's Installation  
#--------------------------------------------------------------------------  
#  
# Installing tools and PHP extentions using "apt", "docker-php", "pecl",  
#  
# Install "curl", "libmemcached-dev", "libpq-dev", "libjpeg-dev",  
# "libpng12-dev", "libfreetype6-dev", "libssl-dev", "libmcrypt-dev",  
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
libmcrypt-dev  
  
# Install the PHP mcrypt extention  
RUN docker-php-ext-install mcrypt  
  
# Install the PHP pdo_mysql extention  
RUN docker-php-ext-install pdo_mysql  
  
# Install the PHP pdo_pgsql extention  
RUN docker-php-ext-install pdo_pgsql  
  
#####################################  
# gd:  
#####################################  
# Install the PHP gd library  
RUN docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-jpeg-dir=/usr/lib \  
\--with-freetype-dir=/usr/include/freetype2 && \  
docker-php-ext-install gd  
  
####### Additions to install composer and git  
RUN curl -s http://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
ln -s /usr/local/bin/composer /usr/bin/composer  
  
RUN apt-get install -y --no-install-recommends \  
git  
  
####### Original 2 files were split here  
ADD ./php.ini /usr/local/etc/php/conf.d  
ADD ./php.pool.conf /usr/local/etc/php-fpm.d/  
  
RUN rm -r /var/lib/apt/lists/*  
  
RUN usermod -u 1000 www-data  
  
WORKDIR /var/www  
  
CMD ["php-fpm"]  
  
EXPOSE 9000  

