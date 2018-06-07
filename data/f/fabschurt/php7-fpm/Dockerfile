FROM alpine:3.5  
MAINTAINER Fabien Schurter <fabien@fabschurt.com>  
  
RUN apk update --no-cache && \  
apk add \  
php7-fpm \  
php7-bz2 \  
php7-ctype \  
php7-curl \  
php7-dom \  
php7-gettext \  
php7-iconv \  
php7-intl \  
php7-json \  
php7-openssl \  
php7-mbstring \  
php7-mcrypt \  
php7-pcntl \  
php7-pdo \  
php7-phar \  
php7-session \  
php7-sockets \  
php7-xml \  
php7-xmlreader \  
php7-xsl \  
php7-zip \  
php7-zlib \  
&& \  
rm /etc/php7/php-fpm.d/*.conf && \  
ln -s /usr/bin/php7 /usr/bin/php && \  
ln -s /usr/sbin/php-fpm7 /usr/sbin/php-fpm && \  
addgroup -S php-fpm && \  
adduser -SDH -s /sbin/nologin -G php-fpm php-fpm && \  
rm -rf /var/cache/apk/*  
COPY config /etc/php7  
  
EXPOSE 9000  
CMD ["php-fpm"]  

