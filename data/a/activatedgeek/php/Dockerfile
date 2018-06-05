FROM alpine:latest  
  
MAINTAINER Sanyam Kapoor "1sanyamkapoor@gmail.com"  
  
RUN apk update &&\  
apk add --update \  
curl \  
openrc \  
php-bcmath \  
php-bz2 \  
php-cli \  
php-curl \  
php-ctype \  
php-dba \  
php-dom \  
php-exif \  
php-fpm \  
php-ftp \  
php-gd \  
php-gettext \  
php-iconv \  
php-json \  
php-mcrypt \  
php-mysql \  
php-mysqli \  
php-opcache \  
php-openssl \  
php-pdo \  
php-pdo_mysql \  
php-pdo_sqlite \  
php-phar \  
php-posix \  
php-shmop \  
php-soap \  
php-sockets \  
php-sqlite3 \  
php-sysvmsg \  
php-sysvsem \  
php-sysvshm \  
php-wddx \  
php-xcache \  
php-xml \  
php-xmlreader \  
php-zip \  
php-zlib \  
musl &&\  
php -r "readfile('https://getcomposer.org/installer');" > composer-setup.php
&&\  
php composer-setup.php --install-dir=/bin --filename=composer &&\  
php -r "unlink('composer-setup.php');" &&\  
# use sockets as they are memory efficient  
sed -i "s/^listen.*/listen = \/var\/run\/php5\\-fpm.sock/" /etc/php/php-
fpm.conf &&\  
# allow container environment variables into PHP-FPM  
sed -i "s/^;clear_env.*/clear_env = no/" /etc/php/php-fpm.conf &&\  
# don't override  
rm -rf /var/cache/apk/*  

