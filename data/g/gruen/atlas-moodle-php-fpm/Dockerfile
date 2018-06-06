FROM php:7-fpm-alpine  
  
LABEL maintainer "Darren Green <darren.green@meetingprotocol.com>"  
  
RUN apk add \  
\--update \  
\--no-cache \  
zlib-dev \  
libpng \  
libpng-dev \  
libjpeg-turbo \  
libjpeg-turbo-dev \  
freetype \  
freetype-dev \  
icu \  
icu-dev \  
libxml2 \  
libxml2-dev \  
&& docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include \  
\--with-png-dir=/usr/include \  
\--with-jpeg-dir=/usr/include \  
&& NPROC="$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1)" \  
&& docker-php-ext-install \  
pdo_mysql \  
mysqli \  
zip \  
gd \  
intl \  
xmlrpc \  
soap \  
&& docker-php-ext-enable \  
pdo_mysql \  
mysqli \  
zip \  
gd \  
&& echo "catch_workers_output = yes" >> /usr/local/etc/php-fpm.d/www.conf \  
&& echo "php_flag[display_errors] = on" >> /usr/local/etc/php-fpm.d/www.conf \  
&& echo "php_admin_flag[log_errors] = on" >> /usr/local/etc/php-fpm.d/www.conf
\  
&& apk del \  
\--no-cache \  
freetype-dev \  
libpng-dev \  
libjpeg-turbo-dev  
  

