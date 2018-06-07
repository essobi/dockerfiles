FROM php:5.6-fpm  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxml2-dev \  
libicu-dev \  
libxslt1-dev \  
libexif-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) exif iconv mcrypt gd mbstring pdo_mysql
soap zip intl pcntl xsl opcache  
  
# Memory Limit  
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini  
  
# Time Zone  
RUN echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
$PHP_INI_DIR/conf.d/date_timezone.ini  
  
RUN curl --remote-name
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz  
RUN tar xvfz ioncube_loaders_lin_x86-64.tar.gz  
RUN cp ioncube/ioncube_loader_lin_5.6.so /usr/local/lib/php/extensions/no-
debug-non-zts-20131226  
RUN echo zend_extension = ioncube_loader_lin_5.6.so >
$PHP_INI_DIR/conf.d/00-ioncube.ini  
  
WORKDIR /var/www  

