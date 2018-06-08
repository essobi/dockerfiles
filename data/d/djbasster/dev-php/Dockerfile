FROM debian:stretch-slim  
  
MAINTAINER Ole Rößner <o.roessner@neusta.de>  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
wget \  
lsb-release \  
apt-transport-https \  
ca-certificates  
  
RUN wget -O /etc/apt/trusted.gpg.d/php.gpg
https://packages.sury.org/php/apt.gpg \  
&& sh -c 'echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list'  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
php7.1-apcu \  
php7.1-common \  
php7.1-readline \  
php7.1-fpm \  
php7.1-cli \  
php7.1-mysql \  
php7.1-curl \  
php7.1-intl \  
php7.1-mbstring \  
php7.1-opcache \  
php7.1-json \  
php7.1-pdo \  
php7.1-memcached \  
php7.1-zip \  
php7.1-xsl \  
php7.1-gmagick \  
php7.1-xdebug  

