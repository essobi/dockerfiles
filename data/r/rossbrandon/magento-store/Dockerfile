FROM php:5.6-fpm-alpine  
  
LABEL maintainer="Ross Brandon <rbrandon@magento.com>"  
# Install packages  
RUN apk --update add --no-cache \  
php5-json \  
php5-curl \  
php5-ctype \  
libxml2-dev \  
libmcrypt-dev \  
ssmtp \  
autoconf \  
g++ \  
make \  
&& docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) \  
iconv \  
mcrypt \  
mbstring \  
mysqli \  
pdo_mysql \  
soap \  
&& pecl install \  
xdebug-2.5.0 \  
oauth-1.2.3 \  
&& docker-php-ext-enable \  
xdebug \  
&& apk del \  
autoconf \  
g++ \  
make \  
&& rm -rf /var/cache/apk/*  
  
# Configure directories, files, and permissions  
RUN find /var/www/html/ -type d -exec chmod 700 {} \;  
RUN find /var/www/html/ -type f -exec chmod 600 {} \;

