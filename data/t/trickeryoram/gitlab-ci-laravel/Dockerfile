FROM php:7.1  
MAINTAINER Mark Wienk <mark@wienk.nl>  
MAINTAINER Yoram de Langen <yoram@brandcube.nl>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
curl \  
openssh-client \  
git-core \  
mysql-client \  
libbz2-dev \  
libcurl4-openssl-dev \  
libfreetype6-dev \  
libicu-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libpng-dev \  
libxslt1-dev \  
libxml2-dev \  
libgd2-xpm-dev \  
cmake make \  
nasm g++ gcc \  
automake autogen autoconf libtool intltool \  
&& rm -r /var/lib/apt/lists/*  
  
ENV YARN_VERSION=latest  
  
# Install NodeJS, NPM and  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash - && \  
apt-get install -y nodejs  
# Start installing Yarn - copied from mhart/alpine-node  
# @TODO fix this  
# RUN curl -sf -o yarn-latest.tar.gz https://yarnpkg.com/latest.tar.gz && \  
# mkdir -p /usr/local/share/yarn && \  
# tar -xf yarn-latest.tar.gz -C /usr/local/share/yarn --strip 1 && \  
# ln -s /usr/local/share/yarn/bin/yarn /usr/local/bin/ && \  
# ln -s /usr/local/share/yarn/bin/yarnpkg /usr/local/bin/ && \  
# rm yarn-latest.tar.gz;  
# PHP Extensions (curl, mbstring, hash, simplexml, xml, json, iconv are
already installed in php image)  
RUN docker-php-ext-configure \  
gd --with-jpeg-dir=/usr/include/  
  
RUN docker-php-ext-install \  
gd \  
bz2 \  
intl \  
mcrypt \  
pdo_mysql \  
pcntl \  
soap \  
xsl \  
zip  
  
# PHP Configuration  
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini  
RUN echo "date.timezone=Europe/Amsterdam" >
$PHP_INI_DIR/conf.d/date_timezone.ini  
  
VOLUME /root/composer  
  
# Environmental Variables  
ENV COMPOSER_HOME /root/composer  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
composer selfupdate  
  
# Goto temporary directory.  
WORKDIR /tmp  
  
RUN php --version  
RUN composer --version  

