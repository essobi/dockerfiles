FROM php:7.1-fpm  
  
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
  
# Install from PECL - disabled for PHP 7.1RC  
#RUN pecl install xdebug  
#RUN docker-php-ext-enable xdebug  
# Installing xdebug from src  
#RUN curl -L -o /tmp/xdebug.zip
https://codeload.github.com/xdebug/xdebug/zip/master  
#RUN unzip /tmp/xdebug.zip -d /tmp  
#RUN ls -la /tmp  
#RUN rm -r /tmp/xdebug.zip  
#RUN ( \  
# cd /tmp/xdebug-master \  
# && phpize \  
# && ./configure --enable-xdebug \  
# && make -j$(nproc) \  
# && make install \  
# )  
#RUN docker-php-ext-enable xdebug  

