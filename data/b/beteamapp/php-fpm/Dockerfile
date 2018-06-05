FROM php:fpm  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libbz2-dev \  
libicu52 \  
libicu-dev \  
libldap2-dev \  
libmcrypt4 \  
libmcrypt-dev \  
zlib1g-dev \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \  
&& docker-php-ext-install \  
bz2 \  
exif \  
intl \  
ldap \  
mbstring \  
mcrypt \  
mysqli \  
pdo_mysql \  
zip \  
&& apt-get purge -y --auto-remove \  
libbz2-dev \  
libicu-dev \  
libldap2-dev \  
libmcrypt-dev \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& cd /usr/src/php && make clean  
  
RUN cp /usr/src/php/php.ini-production /usr/local/etc/php/php.ini \  
# Setup timezone to Etc/UTC  
&& sed -i 's/^;\\(date.timezone\\) =/\1 = Europe\/Paris/'
/usr/local/etc/php/php.ini \  
# Setup INTL default locale  
&& sed -i 's/^;\\(intl.default_locale\\) =/\1 = fr_BE/'
/usr/local/etc/php/php.ini  
  
CMD ["php-fpm"]  

