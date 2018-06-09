FROM alpine:3.7  
# Environments  
ENV TIMEZONE Etc/UTC  
  
RUN apk update && \  
apk add --update tzdata && \  
cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \  
echo "${TIMEZONE}" > /etc/timezone && \  
apk add --update \  
ca-certificates \  
fuse \  
mysql-client \  
php7-bcmath \  
php7-bz2 \  
php7-ctype \  
php7-curl \  
php7-dom \  
php7-fpm \  
php7-gd \  
php7-gettext \  
php7-gmp \  
php7-iconv \  
php7-intl \  
php7-json \  
php7-mcrypt \  
php7-memcached \  
php7-mysqli \  
php7-odbc \  
php7-opcache \  
php7-openssl \  
php7-phar \  
php7-pdo \  
php7-pdo_dblib \  
php7-pdo_mysql \  
php7-pdo_odbc \  
php7-pdo_pgsql \  
php7-pdo_sqlite \  
php7-soap \  
php7-xml \  
php7-xmlreader \  
php7-xmlrpc \  
php7-zip \  
php7-zlib \  
&& \  
# Cleaning up  
mkdir /www && \  
apk del tzdata && \  
rm -rf /var/cache/apk/*  
  
COPY php/php.ini /etc/php7/php.ini  
COPY php/php-fpm.conf /etc/php7/php-fpm.conf  
COPY php/www.conf /etc/php7/php-fpm.d/www.conf  
  
# Set Workdir  
WORKDIR /www  
  
# Expose volumes  
VOLUME ["/www"]  
  
# Expose ports  
EXPOSE 9000  
# Entry point  
ENTRYPOINT ["/usr/sbin/php-fpm7", "--nodaemonize"]  

