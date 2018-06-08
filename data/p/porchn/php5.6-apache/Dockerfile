FROM php:5.6-apache  
#MAINTAINER porchn <pichai.chin@gmail.com>  
ENV TZ=Asia/Bangkok  
# Set Server timezone.  
RUN echo $TZ > /etc/timezone \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& echo date.timezone = $TZ > /usr/local/etc/php/conf.d/docker-php-ext-
timezone.ini  
  
RUN mkdir -p /etc/apache2/ssl  
  
# Defaul config php.ini  
COPY ./config/php.ini /usr/local/etc/php/  
COPY ./index.php /var/www/html/  
  
RUN apt-get -y update \  
&& apt-get install -y --no-install-recommends \  
wget \  
unzip \  
git \  
vim \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libicu-dev \  
zlib1g-dev \  
libxml2-dev \  
libaio-dev \  
libgearman-dev \  
unixodbc-dev \  
freetds-bin \  
freetds-dev \  
freetds-common \  
libmemcached11 \  
libmemcachedutil2 \  
libmemcached-dev \  
libz-dev \  
build-essential \  
apache2-utils \  
libmagickwand-dev \  
imagemagick \  
libcurl4-openssl-dev \  
libssl-dev \  
libc-client2007e-dev \  
libkrb5-dev \  
libmcrypt-dev \  
unixodbc-dev \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
RUN mkdir /opt/oracle \  
&& cd /opt/oracle  
  
ADD oci/instantclient-basic-linux.x64-12.1.0.2.0.zip /opt/oracle  
ADD oci/instantclient-sdk-linux.x64-12.1.0.2.0.zip /opt/oracle  
  
RUN unzip /opt/oracle/instantclient-basic-linux.x64-12.1.0.2.0.zip -d
/opt/oracle \  
&& unzip /opt/oracle/instantclient-sdk-linux.x64-12.1.0.2.0.zip -d /opt/oracle
\  
&& ln -s /opt/oracle/instantclient_12_1/libclntsh.so.12.1
/opt/oracle/instantclient_12_1/libclntsh.so \  
&& ln -s /opt/oracle/instantclient_12_1/libclntshcore.so.12.1
/opt/oracle/instantclient_12_1/libclntshcore.so \  
&& ln -s /opt/oracle/instantclient_12_1/libocci.so.12.1
/opt/oracle/instantclient_12_1/libocci.so \  
&& rm -rf /opt/oracle/*.zip  
  
# Config Extension  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/lib/ --with-jpeg-
dir=/usr/lib/ \  
&& echo 'instantclient,/opt/oracle/instantclient_12_1/' | pecl install
oci8-2.0.10 \  
&& docker-php-ext-configure pdo_oci --with-pdo-
oci=instantclient,/opt/oracle/instantclient_12_1,12.1 \  
&& docker-php-ext-configure pdo_dblib --with-libdir=/lib/x86_64-linux-gnu \  
&& docker-php-ext-configure imap --with-imap-ssl --with-kerberos  
  
RUN docker-php-ext-install mysqli mysql mbstring opcache pdo_mysql gd mcrypt
zip imap soap pdo pdo_oci  
RUN docker-php-ext-enable oci8  
  
# Enable Apache mod_rewrite  
RUN a2enmod rewrite ssl headers  
  
# Memcache  
RUN pecl install memcached-2.2.0 \  
&& docker-php-ext-enable memcached  
  
# Imagick  
RUN pecl install imagick \  
&& docker-php-ext-enable imagick  
  
RUN chown -R www-data:www-data /var/www  
# Create Volume  
VOLUME ['/etc/apache2/sites-enabled','/var/www','/var/log/apache2']  
  
EXPOSE 80  
EXPOSE 443  

