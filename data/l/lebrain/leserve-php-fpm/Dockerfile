FROM php:5.6-fpm  
  
MAINTAINER Ilya Shtrikul <shtricul@gmail.com>  
  
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
zsh \  
curl \  
libmemcached-dev \  
libz-dev \  
libpq-dev \  
libjpeg-dev \  
libpng12-dev \  
libfreetype6-dev \  
libssl-dev \  
libmcrypt-dev \  
libldap2-dev  
  
# Install the PHP mcrypt extention  
RUN docker-php-ext-install mcrypt && \  
docker-php-ext-install pdo_mysql && \  
docker-php-ext-install mysql && \  
docker-php-ext-install pdo_pgsql && \  
docker-php-ext-install tokenizer && \  
docker-php-ext-install mysqli && \  
docker-php-ext-install opcache && \  
pecl install xdebug && \  
pecl install memcache && \  
pecl install memcached && \  
pecl install zip && \  
docker-php-ext-enable xdebug && \  
docker-php-ext-enable zip && \  
docker-php-ext-enable memcache && \  
docker-php-ext-enable memcached && \  
docker-php-ext-enable opcache  
  
  
#####################################  
# gd:  
#####################################  
# Install the PHP gd library  
RUN docker-php-ext-install gd && \  
docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-jpeg-dir=/usr/lib \  
\--with-freetype-dir=/usr/include/freetype2 && \  
docker-php-ext-install gd  
  
# Install LDAP  
RUN docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \  
docker-php-ext-install ldap  
  
#  
#--------------------------------------------------------------------------  
# Final Touch  
#--------------------------------------------------------------------------  
#  
  
ADD ./config /usr/local/etc  
  
RUN rm -r /var/lib/apt/lists/*  
  
RUN usermod -u 1000 www-data  
  
WORKDIR /var/www  
  
CMD ["php-fpm"]  
  
EXPOSE 9000  

