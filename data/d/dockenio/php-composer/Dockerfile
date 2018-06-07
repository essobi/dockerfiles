FROM ubuntu:16.04  
  
MAINTAINER "Florian Wartner <f.wartner@docken.io>"  
  
RUN apt-get update \  
&& apt-get install -y curl zip unzip git software-properties-common \  
&& add-apt-repository -y ppa:ondrej/php \  
&& apt-get update \  
&& apt-get install -y php7.2-fpm php7.2-cli php7.2-mcrypt php7.2-gd
php7.2-mysql \  
php7.2-pgsql php7.2-imap php-memcached php7.2-mbstring php7.2-xml php7.2-curl
\  
&& php -r "readfile('http://getcomposer.org/installer');" | php -- --install-
dir=/usr/bin/ --filename=composer \  
&& mkdir /run/php \  
&& apt-get remove -y --purge software-properties-common \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

