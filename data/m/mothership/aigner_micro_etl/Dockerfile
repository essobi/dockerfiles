FROM php:7.1.4-fpm-alpine  
  
RUN apk add --no-cache --virtual .build-deps \  
gcc \  
make \  
curl \  
linux-headers \  
  
libc-dev \  
pcre-dev \  
zlib-dev \  
libxslt-dev \  
gd-dev \  
perl-dev \  
libmcrypt \  
# Requirement for php extension  
autoconf libpng-dev libjpeg-turbo-dev freetype-dev libmcrypt-dev icu-dev \  
#  
&& docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
#curl iconv session  
&& docker-php-ext-install pdo_mysql mysqli mcrypt gd exif intl xsl json soap
dom zip bcmath \  
  
# https://pecl.php.net/package/redis  
# https://xdebug.org/download.php  
&& pecl install redis-3.1.1 \  
&& pecl install xdebug-2.5.1 \  
&& docker-php-ext-enable redis xdebug  
  
# Cleanup  
RUN apk del .build-deps \  
&& apk add --no-cache gd libxslt libjpeg-turbo freetype libmcrypt icu-libs
libpng bash \  
&& rm -rf /var/cache/apk/*  
  
RUN apk add --no-cache git openssh  
  
###############################  
# composer.phar #  
###############################  
RUN curl -sL https://getcomposer.org/download/1.2.0/composer.phar -o
/usr/local/bin/composer \  
&& chmod +x /usr/local/bin/composer  
  
# Speed up install composer libraries  
RUN composer global require "hirak/prestissimo:^0.3"  
  
COPY src /var/www/share/dev/  
  
# Install dependencies  
RUN cd /var/www/share/dev && /usr/local/bin/composer install --no-dev  
  
#RUN rm /var/www/share/dev/resources/data/*json; exit 0  
WORKDIR /var/www/share/dev/  
  
ADD docker/php_fpm/cronjobs/crontab.txt /crontab.txt  
ADD docker/php_fpm/scripts/script.sh /script.sh  
COPY docker/php_fpm/scripts/entry.sh /entry.sh  
RUN chmod 755 /script.sh /entry.sh  
RUN /usr/bin/crontab /crontab.txt  
  
CMD ["/entry.sh"]

