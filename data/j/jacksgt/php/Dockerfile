FROM php:7.2-fpm-stretch  
  
# Install OS dependencies  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install --no-install-recommends -y \  
imagemagick \  
imagemagick-common \  
libc-client-dev \  
libcurl4-openssl-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libkrb5-dev \  
libldap2-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libpng-dev \  
libpq-dev \  
zlib1g-dev \  
&& apt-get autoclean; apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
# Link LDAP library for PHP ldap extension  
RUN ln -fs /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/  
  
RUN docker-php-ext-configure imap --with-kerberos --with-imap-ssl  
  
# Install PHP Plugins  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ \--with-png-dir=/usr/include/ && \  
docker-php-ext-install \  
curl \  
gd \  
gettext \  
imap \  
json \  
ldap \  
mbstring \  
pdo \  
pdo_mysql \  
pdo_pgsql \  
pgsql \  
zip  
  
RUN pecl install imagick-3.4.3 && \  
docker-php-ext-enable imagick  

