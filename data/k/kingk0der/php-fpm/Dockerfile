FROM php:7.2.2-fpm  
MAINTAINER Hrishikesh <hrishikesh.raverkar@gmail.com>  
RUN echo "deb http://ftp.de.debian.org/debian stretch main" >>
/etc/apt/sources.list  
RUN apt-get update && apt-get install -y wget gnupg2  
RUN echo "deb http://repo.mysql.com/apt/debian/ stretch mysql-5.7" >
/etc/apt/sources.list.d/mysql.list  
RUN echo "deb-src http://repo.mysql.com/apt/debian/ stretch mysql-5.7" >
/etc/apt/sources.list.d/mysql.list  
RUN wget -O /tmp/RPM-GPG-KEY-mysql https://repo.mysql.com/RPM-GPG-KEY-mysql  
RUN apt-key add /tmp/RPM-GPG-KEY-mysql  
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
git \  
xvfb \  
ca-certificates --no-install-recommends  
  
# Install PHP 7 Extension Libs  
RUN apt-get update  
RUN apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
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
locate \  
libpq-dev \  
libedit-dev \  
unzip \  
iputils-ping \  
mysql-client \  
# postgresql-client \  
imagemagick \  
libmemcached-dev \  
libjudydebian1 \  
libjudy-dev \  
checkinstall  
  
RUN apt-get -y install libcurl4-gnutls-dev  
RUN apt-get -y install libpcre*  
# Create required dir  
RUN ln -s /usr/include/x86_64-linux-gnu/curl /usr/include/curl  
RUN mkdir /tmp/ext \  
&& mkdir /tmp/phpext \  
&& mkdir -p /usr/src/php/ext/  
# && mkdir -p /usr/local/include/ImageMagick-7 \  
# && mkdir -p /usr/local/lib/ImageMagick-7.0.7  
# Download Required PHP Extensions Source  
RUN \  
# wget -O /tmp/ext/ImageMagick.tar.gz
http://www.imagemagick.org/download/ImageMagick.tar.gz \  
wget -O /tmp/phpext/uploadprogres.zip
https://github.com/Jan-E/uploadprogress/archive/master.zip \  
&& wget -O /tmp/phpext/mcrypt.tgz https://pecl.php.net/get/mcrypt-1.0.1.tgz \  
&& wget -O /tmp/phpext/igbinary.tgz
https://pecl.php.net/get/igbinary-2.0.5.tgz \  
&& wget -O /tmp/phpext/msgpack.tgz https://pecl.php.net/get/msgpack-2.0.2.tgz
\  
&& wget -O /tmp/phpext/memcached.tgz
https://pecl.php.net/get/memcached-3.0.4.tgz \  
&& wget -O /tmp/phpext/redis.tgz https://pecl.php.net/get/redis-3.1.6.tgz \  
&& wget -O /tmp/phpext/imagick.tgz https://pecl.php.net/get/imagick-3.4.3.tgz
\  
&& wget -O /tmp/phpext/oauth.tgz https://pecl.php.net/get/oauth-2.0.2.tgz \  
&& wget -O /tmp/phpext/yar.tgz https://pecl.php.net/get/yar-2.0.3.tgz \  
&& wget -O /tmp/phpext/ds.tgz https://pecl.php.net/get/ds-1.2.3.tgz \  
&& wget -O /tmp/phpext/memprof.tgz https://pecl.php.net/get/memprof-2.0.0.tgz
\  
&& wget -O /tmp/phpext/opencensus.tgz
https://pecl.php.net/get/opencensus-0.0.3.tgz \  
&& wget -O /tmp/phpext/xdebug.tgz https://pecl.php.net/get/xdebug-2.6.0.tgz  
# Un-tar Required PHP Extensions  
RUN \  
# tar -xvzf /tmp/ext/ImageMagick.tar.gz -C /tmp/ext/ \  
unzip /tmp/phpext/uploadprogres.zip -d /usr/src/php/ext/ \  
&& tar -xvzf /tmp/phpext/mcrypt.tgz -C /usr/src/php/ext/ \  
&& tar -xvzf /tmp/phpext/igbinary.tgz -C /usr/src/php/ext/ \  
&& tar -xvzf /tmp/phpext/msgpack.tgz -C /usr/src/php/ext/ \  
&& tar -xvzf /tmp/phpext/memcached.tgz -C /usr/src/php/ext/ \  
&& tar -xvzf /tmp/phpext/redis.tgz -C /usr/src/php/ext/ \  
&& tar -xvzf /tmp/phpext/imagick.tgz -C /usr/src/php/ext/ \  
&& tar -xvzf /tmp/phpext/oauth.tgz -C /usr/src/php/ext/ \  
&& tar -xvzf /tmp/phpext/yar.tgz -C /usr/src/php/ext/ \  
&& tar -xvzf /tmp/phpext/ds.tgz -C /usr/src/php/ext/ \  
&& tar -xvzf /tmp/phpext/memprof.tgz -C /usr/src/php/ext/ \  
&& tar -xvzf /tmp/phpext/opencensus.tgz -C /usr/src/php/ext/ \  
&& tar -xvzf /tmp/phpext/xdebug.tgz -C /usr/src/php/ext/  
# Rename PHP Extensions  
RUN \  
# mv /tmp/ext/ImageMagick-7.0.7-7 /tmp/ext/ImageMagick \  
mv /usr/src/php/ext/uploadprogress-master /usr/src/php/ext/uploadprogress \  
&& mv /usr/src/php/ext/mcrypt-1.0.1 /usr/src/php/ext/mcrypt \  
&& mv /usr/src/php/ext/igbinary-2.0.5 /usr/src/php/ext/igbinary \  
&& mv /usr/src/php/ext/msgpack-2.0.2 /usr/src/php/ext/msgpack \  
&& mv /usr/src/php/ext/memcached-3.0.4 /usr/src/php/ext/memcached \  
&& mv /usr/src/php/ext/redis-3.1.6 /usr/src/php/ext/redis \  
&& mv /usr/src/php/ext/imagick-3.4.3 /usr/src/php/ext/imagick \  
&& mv /usr/src/php/ext/oauth-2.0.2 /usr/src/php/ext/oauth \  
&& mv /usr/src/php/ext/yar-2.0.3 /usr/src/php/ext/yar \  
&& mv /usr/src/php/ext/ds-1.2.3 /usr/src/php/ext/ds \  
&& mv /usr/src/php/ext/memprof-2.0.0 /usr/src/php/ext/memprof \  
&& mv /usr/src/php/ext/opencensus-0.0.3 /usr/src/php/ext/opencensus \  
&& mv /usr/src/php/ext/xdebug-2.6.0 /usr/src/php/ext/xdebug  
  
# Configure PHP Extensions before installing from source  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ \  
&& docker-php-ext-configure imap --with-kerberos --with-imap-ssl \  
&& docker-php-ext-configure igbinary CFLAGS="-O2 -g" \--enable-igbinary  
  
# Install PHP Extension from source  
RUN docker-php-ext-install calendar \  
bcmath \  
iconv \  
json \  
mcrypt \  
mbstring \  
phar \  
curl \  
ftp \  
intl \  
pdo_mysql \  
hash \  
session \  
simplexml \  
tokenizer \  
xml \  
xmlrpc \  
zip \  
gd \  
imap \  
pdo_pgsql \  
opcache \  
posix \  
pcntl \  
uploadprogress \  
igbinary \  
msgpack \  
oauth \  
yar \  
ds \  
memprof \  
opencensus \  
xdebug  
  
# Install Memcache and Redis PHP extension  
RUN docker-php-ext-configure memcached --enable-memcached-igbinary \  
&& docker-php-ext-configure redis --enable-redis-igbinary \  
&& docker-php-ext-install memcached redis  
  
  
#RUN apt-get -y install checkinstall  
#RUN mkdir /usr/local/include/ImageMagick-7 \  
# && mkdir /usr/local/lib/ImageMagick-7.0.7 \  
# && cd /tmp/ext/ImageMagick \  
# && ./configure \  
# && make clean \  
# && make  
#RUN checkinstall --nodoc \  
# && ldconfig /usr/local/lib  
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
ENV PHPRC=/etc/php7/cli/php.ini  
WORKDIR /var/www  
  
# Expose Ports & Volumes  
EXPOSE 9000  
  
CMD ["php-fpm", "-F", "-c", "/etc/php7/fpm"]  

