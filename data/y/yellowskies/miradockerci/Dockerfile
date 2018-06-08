FROM php:7.2-fpm  
  
#Install "curl", "libmemcached-dev", "libpq-dev", "libjpeg-
dev","libpng12-dev", "libfreetype6-dev", "libssl-dev", "libmcrypt-dev"  
RUN apt-get update && \  
apt-get install -y \  
git \  
curl \  
zlib1g-dev\  
libmemcached-dev \  
libzip-dev\  
libz-dev \  
libpq-dev \  
libjpeg-dev \  
libfreetype6-dev \  
libssl-dev \  
libicu-dev\  
libxslt-dev\  
libc-client-dev\  
libkrb5-dev\  
mysql-client  
  
# Install unzip  
RUN apt-get install -y unzip  
# Install unzip  
RUN apt-get install -y wget  
  
RUN echo "file_uploads = On\n" \  
"memory_limit = 500M\n" \  
"upload_max_filesize = 500M\n" \  
"post_max_size = 500M\n" \  
"max_execution_time = 600\n" \  
> /usr/local/etc/php/conf.d/uploads.ini  
  
# Install the PHP mcrypt extention  
# mcryp kapout depuis php 7.2 RUN docker-php-ext-install mcrypt  
# Install the PHP imap extention  
RUN docker-php-ext-configure imap --with-kerberos --with-imap-ssl  
RUN docker-php-ext-install imap  
  
# Install the PHP pdo_mysql extention  
RUN docker-php-ext-install pdo_mysql  
  
# Install the INTL  
RUN docker-php-ext-install intl  
  
# Install the PHP gd library  
RUN docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-jpeg-dir=/usr/lib \  
\--with-freetype-dir=/usr/include/freetype2 && \  
docker-php-ext-install gd  
  
RUN docker-php-ext-install soap  
  
# Install ZIP  
RUN pecl install zip && docker-php-ext-enable zip  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# Install Xdebug  
RUN pecl install xdebug && docker-php-ext-enable xdebug  
COPY ./xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini  

