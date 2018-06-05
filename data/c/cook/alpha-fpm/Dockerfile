FROM php:5.6-fpm  
  
RUN groupadd -r alpha \  
&& useradd -r -g alpha -G sudo alpha  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev
php5-memcache && rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd  
RUN docker-php-ext-install mysqli mbstring  
  
ENV PHP_EXTRA_CONFIGURE_ARGS --enable-fpm --with-fpm-user=alpha --with-fpm-
group=alpha  
  
VOLUME ["/home/alpha","/var/log/fpm"]

