FROM php:7.1-cli  
  
RUN apt-get update --fix-missing  
  
RUN apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
zip \  
mysql-client \  
supervisor \  
cron \  
sox \  
libmagickwand-dev  
  
RUN docker-php-ext-install gettext pdo pdo_mysql  
RUN docker-php-ext-install mbstring  
RUN docker-php-ext-install -j$(nproc) iconv  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install -j$(nproc) gd  
  
RUN pecl install imagick  
RUN docker-php-ext-enable imagick  
  
RUN docker-php-ext-configure bcmath  
RUN docker-php-ext-install bcmath  
  
RUN pecl install redis  
RUN docker-php-ext-enable redis  
  

