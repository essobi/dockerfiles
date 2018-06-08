FROM composer:1.6.5 AS composer  
  
FROM wordpress:cli-1.5.1-php7.0 AS cli  
  
FROM phusion/baseimage:0.10.1  
LABEL maintainer="nick@foobar.net.nz"  
  
RUN apt-get update -qqy \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -qqy \  
php-cli \  
php-curl \  
php-gd \  
php-http \  
php-imagick \  
php-json \  
php-log \  
php-mbstring \  
php-memcache \  
php-mysqli \  
php-oauth \  
bash-completion \  
curl \  
git \  
jq \  
less \  
mysql-client \  
zip \  
&& apt-get clean -y  
  
RUN phpenmod curl gd imagick json mbstring memcache mysqli oauth opcache  
  
COPY \--from=composer /usr/bin/composer /usr/local/bin/composer  
COPY \--from=cli /usr/local/bin/wp /usr/local/bin/wp  
  
RUN useradd -m -s /bin/bash wp \  
&& composer -V \  
&& wp --allow-root cli version  

