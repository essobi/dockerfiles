FROM php:7.1-apache  
  
# Install the deb packages and PHP extensions we need  
#  
# Notes:  
# - memcached needs manual git checkout  
RUN set -x && DEBIAN_FRONTEND=noninteractive \  
&& apt-get update && apt-get install -y --no-install-recommends lsb-release
wget \  
&& apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
git \  
libicu-dev \  
libjpeg-dev \  
libldap2-dev \  
libmemcached-dev \  
libmemcached11 \  
libpng12-dev \  
libpq-dev \  
mysql-client \  
unzip \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \  
&& docker-php-ext-install gd intl json ldap mbstring opcache pdo pdo_mysql
pdo_pgsql sockets zip \  
&& pecl install apcu igbinary \  
&& cd /tmp && git clone --branch php7 https://github.com/php-memcached-
dev/php-memcached \  
&& cd php-memcached && phpize && ./configure && make && make install \  
&& docker-php-ext-enable apcu igbinary memcached \  
&& apt-get remove --purge -y build-essential \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/php-memcached  
  
# Install a recent version of jq, Debian has an old version  
RUN curl -o /usr/local/bin/jq -Ls
https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 \  
&& chmod +x /usr/local/bin/jq  
  

