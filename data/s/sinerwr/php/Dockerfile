FROM php:5.6-fpm-alpine  
  
RUN docker-php-source extract && \  
apk add --update \--no-cache autoconf g++ make libtool libxslt-dev imap-dev
libedit-dev icu-dev imagemagick-dev libmcrypt-dev bzip2-dev curl-dev
libxml2-dev enchant-dev libpng-dev gmp-dev unixodbc-dev && \  
pecl install imagick memcache redis && \  
docker-php-ext-enable imagick memcache redis && \  
docker-php-ext-install bcmath bz2 calendar ctype curl dom enchant exif gd
gettext gmp hash iconv intl imap json mbstring mcrypt mysql mysqli opcache
pcntl pdo pdo_mysql phar posix readline simplexml soap sockets sysvsem
tokenizer xmlrpc xsl zip && \  
docker-php-source delete &&\  
rm -rf /var/cache/apk/*

