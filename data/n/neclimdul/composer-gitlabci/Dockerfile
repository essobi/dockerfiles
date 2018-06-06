# Composer Docker Container  
FROM composer  
MAINTAINER James Gilliland <neclimdul@gmail.com>  
  
# Install pecl but don't enable it so composer can be quick and scripts can  
# enable it as needed.  
# Install some common testing extensions  
RUN apk --no-cache --virtual .build-deps add $PHPIZE_DEPS \  
libjpeg-turbo-dev \  
libpng-dev \  
yaml-dev \  
&& apk -U add binutils patch \  
libjpeg-turbo \  
libpng \  
yaml \  
&& docker-php-ext-configure gd --with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install pdo_mysql gd \  
&& pecl install yaml-2.0.2 \  
&& docker-php-ext-enable yaml \  
&& pecl install redis \  
&& pecl install xdebug \  
&& apk del .build-deps \  
&& rm -rf /tmp/pear  
  
ENTRYPOINT []  

