# Php Image Dockerfile  
FROM php:5.6-apache  
MAINTAINER Xiaowen Zhang <sean@evestemptatiion.com>  
COPY ./php.ini /usr/local/etc/php/php.ini  
COPY ./configure.sh /bin/configure.sh  
RUN mkdir -p /dockers/scripts \  
&& mkdir -p /dockers/data \  
&& mkdir -p /dockers/packages  
ADD ./vars.sh /dockers/scripts/vars.sh  
ADD ./res /dockers/res  
  
# User variables  
ENV PATH /usr/local/bin:$PATH  
  
  
# install pdo, pdo_mysql, mysql  
RUN docker-php-ext-install pdo pdo_mysql \  
&& docker-php-ext-enable pdo pdo_mysql \  
&& apt-get update\  
&& apt-get install -y php5-mysql apt-utils\  
&& sed -i '/\\[MySQL\\]/a extension=/usr/lib/php5/20131226/mysql.so'
/usr/local/etc/php/php.ini  
  
# install mcrypt module  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
vim \  
wget \  
htop \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-enable iconv mcrypt  
  
# install memcached module  
Run apt-get install -y libmemcached-dev \  
&& pecl install memcached \  
&& docker-php-ext-enable memcached  
  
# configuration for Apache 2  
RUN a2enmod rewrite \  
&& a2enmod headers \  
&& a2enmod expires  
  
# install xdebug  
RUN pecl install xdebug \  
&& docker-php-ext-enable xdebug  
  
# install operating tools  
RUN apt-get update \  
&& apt-get install -y vim \  
&& apt-get install -y htop \  
&& apt-get install -y git \  
&& apt-get install -y pv \  
&& apt-get install -y tcl8.6 \  
&& apt-get install -y wget \  
&& apt-get install -y zip \  
&& apt-get install -y npm \  
&& apt-get install -y mysql-client \  
&& apt-get install -y redis-tools \  
&& apt-get install -y automake autotools-dev g++ git libcurl4-gnutls-dev
libfuse-dev libssl-dev libxml2-dev make pkg-config  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - \  
&& apt-get update \  
&& apt-get install -y nodejs \  
&& apt-get install -y openssh-server  
  
# Make sure the volume mount point is empty  
RUN rm -rf /var/www/etus  
RUN rm -rf /var/www/html/*  
RUN mkdir -p /var/www/html  
  
ENTRYPOINT /bin/configure.sh  

