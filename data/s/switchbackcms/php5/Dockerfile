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
php5-bcmath \  
php5-bz2 \  
php5-ctype \  
php5-curl \  
php5-dom \  
php5-fpm \  
php5-gd \  
php5-gettext \  
php5-gmp \  
php5-iconv \  
php5-intl \  
php5-json \  
php5-mcrypt \  
php5-mysqli \  
php5-odbc \  
php5-opcache \  
php5-openssl \  
php5-phar \  
php5-pdo \  
php5-pdo_dblib \  
php5-pdo_mysql \  
php5-pdo_odbc \  
php5-pdo_pgsql \  
php5-pdo_sqlite \  
php5-soap \  
php5-xml \  
php5-xmlreader \  
php5-xmlrpc \  
php5-zip \  
php5-zlib \  
&& \  
# Cleaning up  
mkdir /www && \  
apk del tzdata && \  
rm -rf /var/cache/apk/*  
  
COPY php/php.ini /etc/php5/php.ini  
COPY php/php-fpm.conf /etc/php5/php-fpm.conf  
COPY php/www.conf /etc/php5/php-fpm.d/www.conf  
  
# Set Workdir  
WORKDIR /www  
  
# Expose volumes  
VOLUME ["/www"]  
  
# Expose ports  
EXPOSE 9000  
# Entry point  
ENTRYPOINT ["/usr/bin/php-fpm5", "--nodaemonize"]  

