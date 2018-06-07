FROM php:7.2-fpm  
# Dockerfile author / maintainer  
MAINTAINER Felix Stellmacher <docker@istsotoll.de>  
  
COPY src/php.ini /usr/local/etc/php/  
COPY src/www.conf /etc/php-fpm.d/  
COPY src/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN apt-get update && apt-get install -y \  
supervisor \  
sudo \  
sendmail \  
heirloom-mailx \  
mariadb-client \  
bzip2 \  
libcurl4-openssl-dev \  
libfreetype6-dev \  
libicu-dev \  
libjpeg-dev \  
libjpeg62-turbo-dev \  
libldap2-dev \  
libmcrypt-dev \  
libmemcached-dev \  
libpng-dev \  
libpq-dev \  
libxml2-dev \  
libpcre3-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
#
https://docs.nextcloud.com/server/9/admin_manual/installation/source_installation.html  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-png-
dir=/usr/include/ \--with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \  
&& docker-php-ext-install gd exif intl mbstring ldap opcache mysqli pdo_mysql
pdo_pgsql pgsql zip  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.save_comments=1'; \  
echo 'opcache.enable=1'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=10000'; \  
echo 'opcache.revalidate_freq=1'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
# PECL extensions  
RUN set -ex \  
&& pecl install APCu \  
&& pecl install memcached \  
&& pecl install redis \  
&& docker-php-ext-enable apcu redis memcached  
  
RUN groupadd -r ttrss && useradd -r -g ttrss ttrss  
CMD ["/usr/bin/supervisord"]  

