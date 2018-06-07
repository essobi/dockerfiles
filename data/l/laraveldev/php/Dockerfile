FROM php:fpm  
  
RUN apt-get update \  
# gd  
&& apt-get install -y --no-install-recommends libfreetype6-dev libjpeg-dev
libpng-dev libwebp-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \--with-png-dir=/usr/inclue/ \--with-webp-dir=/usr/include/
\  
&& docker-php-ext-install gd \  
# gmp  
&& apt-get install -y --no-install-recommends libgmp-dev \  
&& docker-php-ext-install gmp \  
# pdo_mysql  
&& docker-php-ext-install pdo_mysql \  
# opcache  
&& docker-php-ext-enable opcache \  
# zip  
&& docker-php-ext-install zip \  
# clean up  
&& apt-get autoclean -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/pear/  

