FROM php:alpine  
  
MAINTAINER Will Nichols <will@w-n.co>  
  
WORKDIR /var/www  
  
# Install libraries  
RUN set -ex && \  
apk \--no-cache add \  
curl-dev \  
freetype-dev \  
git \  
libjpeg-turbo-dev \  
libpng-dev \  
libwebp-dev \  
libxml2-dev \  
libzip-dev \  
postgresql-dev \  
zip \  
zlib-dev  
  
# Configure extensions  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \--with-png-dir=/usr/include/ --with-webp-dir=/usr/include/  
RUN docker-php-ext-configure zip --with-libzip  
  
# Available extensions  
# bcmath bz2 calendar ctype curl dba dom enchant exif fileinfo filter ftp gd
gettext gmp hash iconv imap interbase intl json  
# ldap mbstring mysqli oci8 odbc opcache pcntl pdo pdo_dblib pdo_firebird
pdo_mysql pdo_oci pdo_odbc pdo_pgsql pdo_sqlite pgsql  
# phar posix pspell readline recode reflection session shmop simplexml snmp
soap sockets sodium spl standard sysvmsg sysvsem sysvshm  
# tidy tokenizer wddx xml xmlreader xmlrpc xmlwriter xsl zend_test zip  
  
# Install extensions  
RUN docker-php-ext-install \  
gd \  
pdo_pgsql \  
pdo_mysql \  
zip  
  
# Install composer  
RUN wget -O - https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer  
  
ENTRYPOINT ["sh"]  
  
  
  
  
  

