FROM php:7.1-fpm  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
git\  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd  
RUN docker-php-ext-install mbstring mysqli zip exif  
RUN pecl install apcu  
RUN apt-get install -y locales  
RUN dpkg-reconfigure locales && \  
locale-gen C.UTF-8 && \  
/usr/sbin/update-locale LANG=C.UTF-8  
  
RUN echo 'de_DE.UTF-8 UTF-8' >> /etc/locale.gen && \  
locale-gen  
  
COPY uploads.ini /usr/local/etc/php/conf.d/  
COPY disfuncs.ini /usr/local/etc/php/conf.d/  
COPY apcu.ini /usr/local/etc/php/conf.d/  
COPY sessions.ini /usr/local/etc/php/conf.d/  

