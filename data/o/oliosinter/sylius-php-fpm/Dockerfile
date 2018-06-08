FROM php:7.1-fpm  
  
# Installing necessary extensions  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
curl \  
wget \  
git \  
vim \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libicu-dev \  
libicu52 \  
libmagickwand-dev && \  
pecl install imagick && \  
docker-php-ext-enable imagick && \  
docker-php-ext-install iconv && \  
docker-php-ext-install exif && \  
docker-php-ext-install mbstring && \  
docker-php-ext-install pdo_mysql && \  
docker-php-ext-install pdo && \  
docker-php-ext-install intl && \  
docker-php-ext-install opcache && \  
docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ && \  
docker-php-ext-install gd && \  
docker-php-ext-install zip  
  
# Installing composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php composer-setup.php --install-dir=/usr/local/bin --filename=composer && \  
php -r "unlink('composer-setup.php');"  
# Memcached Setup  
# Required libraries  
RUN apt-get update && \  
apt-get install libmemcached-dev libmsgpack-dev libmsgpackc2 -y  
  
# Cloninig and building  
RUN cd /tmp && \  
git clone --depth 1 https://github.com/php-memcached-dev/php-memcached.git &&
\  
cd php-memcached && \  
phpize && \  
./configure && \  
make && \  
mv modules/ /usr/local/memcached/  
  
RUN echo 'extension=/usr/local/memcached/memcached.so' | \  
tee /usr/local/etc/php/conf.d/memcached.ini  
  
# Sylius PHP configuration  
COPY sylius.ini /usr/local/etc/php/sylius.ini  
  
# Seting cache directory  
ENV XDG_CACHE_HOME=/cache  
  
# Explicitly setting working dir  
WORKDIR /var/www/html  
  
EXPOSE 9000

