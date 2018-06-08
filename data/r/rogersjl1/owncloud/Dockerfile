FROM php:7.0-apache  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
bzip2 \  
libcurl4-openssl-dev \  
libfreetype6-dev \  
libicu-dev \  
libjpeg-dev \  
libldap2-dev \  
libmcrypt-dev \  
libmemcached-dev \  
libpng12-dev \  
libpq-dev \  
libxml2-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
#
https://doc.owncloud.org/server/8.1/admin_manual/installation/source_installation.html#prerequisites  
RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \  
&& docker-php-ext-install exif gd intl ldap mbstring mcrypt opcache pdo
pdo_mysql pdo_pgsql pgsql zip  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
RUN a2enmod rewrite  
  
# PECL extensions  
RUN set -ex \  
&& pecl install APCu-5.1.8 \  
&& pecl install memcached-3.0.3 \  
&& pecl install redis-3.1.2 \  
&& docker-php-ext-enable apcu memcached redis  
  
VOLUME ["/var/www/html"]  
  
CMD ["apache2-foreground"]  

