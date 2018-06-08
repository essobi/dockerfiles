FROM php:7-fpm  
  
WORKDIR /data  
  
ENV FLOW_CONTEXT Production  
ENV FLOW_PATH_TEMPORARY_BASE /tmp/flow  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
wget git ssh unzip \  
imagemagick \  
libmagic-dev \  
libzip-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libjpeg-dev \  
libexif-dev \  
libpng12-dev \  
libmcrypt-dev \  
libmagickwand-dev \  
libmysqlclient-dev \  
uuid-dev \  
libyaml-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \--with-png-dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt mbstring pdo_mysql exif gd
zip \  
&& pecl install uuid \  
&& docker-php-ext-enable uuid \  
&& pecl install imagick --with-imagick \  
&& docker-php-ext-enable imagick \  
&& pecl install yaml-beta \  
&& docker-php-ext-enable yaml \  
&& wget http://getcomposer.org/composer.phar \  
&& mv composer.phar /usr/local/bin/composer \  
&& chmod +x /usr/local/bin/composer \  
&& curl -s http://beard.famelo.com/ > beard.phar \  
&& mv beard.phar /usr/local/bin/beard \  
&& chmod +x /usr/local/bin/beard \  
&& { find /usr/local/bin /usr/local/sbin -type f -executable -exec strip
--strip-all '{}' \+ || true; } \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false g++ gcc make pkg-config re2c  
  
ADD root /

