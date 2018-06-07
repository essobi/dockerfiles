FROM php:latest  
MAINTAINER Toby <t.post@hotmail.com>  
  
RUN apt-get update -yqq  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get install git \  
nodejs \  
libcurl4-gnutls-dev \  
libicu-dev \  
libmcrypt-dev \  
libvpx-dev \  
libjpeg-dev \  
libpng-dev \  
libxpm-dev \  
zlib1g-dev \  
libfreetype6-dev \  
libxml2-dev \  
libexpat1-dev \  
libbz2-dev \  
libgmp3-dev \  
libldap2-dev \  
unixodbc-dev \  
libpq-dev \  
libsqlite3-dev \  
libaspell-dev \  
libsnmp-dev \  
libpcre3-dev \  
libtidy-dev \  
-yqq  
RUN apt-get update && apt-get install -y curl apt-transport-https && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && apt-get install -y yarn  
RUN docker-php-ext-install mbstring \  
mcrypt \  
pdo_mysql \  
curl \  
json \  
intl \  
gd \  
xml \  
zip \  
bz2 \  
opcache  
RUN curl --silent --show-error https://getcomposer.org/installer | php --
--install-dir=/usr/local/bin --filename=composer  
RUN composer global require laravel/envoy -vvv  
  

