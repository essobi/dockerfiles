FROM php:7.0-fpm  
MAINTAINER Jabsouliman <benjamin.souliman@gmail.com>  
  
# Install Tools  
RUN apt-get update && apt-get -y install build-essential \  
htop \  
libcurl3 \  
libcurl3-dev \  
librecode0 \  
libsqlite3-0 \  
libxml2 \  
curl \  
wget \  
python \  
vim \  
nano \  
cron \  
git \  
unzip \  
autoconf \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pkg-config \  
re2c \  
ca-certificates --no-install-recommends  
  
# Install PHP 7 Extension  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libsqlite3-dev \  
libssl-dev \  
libcurl3-dev \  
libxml2-dev \  
libzzip-dev \  
libldap2-dev \  
libicu-dev \  
libxslt-dev \  
libc-client-dev \  
libkrb5-dev \  
&& docker-php-ext-install calendar bcmath iconv json mcrypt mbstring phar curl
ftp intl pdo_mysql hash session simplexml tokenizer xml xmlrpc zip \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-configure imap --with-kerberos --with-imap-ssl \  
&& docker-php-ext-install gd imap  
  
# Set up composer variables  
ENV COMPOSER_BINARY=/usr/local/bin/composer \  
COMPOSER_HOME=/usr/local/composer  
ENV PATH $PATH:$COMPOSER_HOME  
  
# Install composer system-wide  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar $COMPOSER_BINARY && \  
chmod +x $COMPOSER_BINARY  
  
COPY php.fpm.ini /etc/php7/fpm/php.ini  
COPY php.cli.ini /etc/php7/cli/php.ini  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /var/www  
  
# Expose Ports & Volumes  
EXPOSE 9000  
  
CMD ["php-fpm", "-F", "-c", "/etc/php7/fpm"]  

