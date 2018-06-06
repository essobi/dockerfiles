FROM php:7.1-fpm  
  
LABEL maintainer "code@socifi.com" description "SOCIFI Development Team"  
  
COPY config/php.ini /usr/local/etc/php/  
# Extensions  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
zlib1g-dev \  
libpng12-dev \  
libssl-dev \  
libmemcached-dev \  
libpq-dev \  
wget \  
git \  
libxml2-dev  
  
RUN pecl install mongodb \  
&& pecl install redis \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) \  
gd \  
iconv \  
mcrypt \  
bcmath \  
mysqli \  
pcntl \  
pdo_mysql \  
pdo_pgsql \  
zip \  
sockets \  
soap \  
&& docker-php-ext-enable \  
opcache \  
mongodb \  
redis  
  
# Composer  
RUN php -r "readfile('https://getcomposer.org/installer');" > composer-
setup.php \  
&& php composer-setup.php \  
&& php -r "unlink('composer-setup.php');" \  
&& chmod +x composer.phar \  
&& mv composer.phar /usr/bin/composer  
  
# Add global composer bin dir to PATH  
ENV PATH /root/.composer/vendor/bin:$PATH  
  
VOLUME /srv  
  
WORKDIR /srv  

