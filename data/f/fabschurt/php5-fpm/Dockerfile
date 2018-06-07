FROM alpine:3.5  
MAINTAINER Fabien Schurter <fabien@fabschurt.com>  
  
RUN apk update --no-cache && \  
apk add \  
php5-fpm \  
php5-bz2 \  
php5-ctype \  
php5-curl \  
php5-dom \  
php5-gettext \  
php5-iconv \  
php5-intl \  
php5-json \  
php5-openssl \  
php5-mcrypt \  
php5-pcntl \  
php5-pdo \  
php5-phar \  
php5-sockets \  
php5-xml \  
php5-xmlreader \  
php5-xsl \  
php5-zip \  
php5-zlib \  
&& \  
addgroup -S php-fpm && \  
adduser -SDH -s /sbin/nologin -G php-fpm php-fpm && \  
rm -rf /var/cache/apk/*  
COPY config /etc/php5  
  
EXPOSE 9000  
CMD ["php-fpm"]  

