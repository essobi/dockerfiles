FROM alpine:3.5  
  
ENV TIMEZONE Europe/Warsaw  
ENV PHP_MEMORY_LIMIT 512M  
ENV MAX_UPLOAD 50M  
ENV PHP_MAX_FILE_UPLOAD 200  
ENV PHP_MAX_POST 100M  
ENV SHORT_OPEN_TAG Off  
  
  
RUN apk update && \  
apk upgrade && \  
addgroup -g 82 -S www-data && \  
adduser -u 82 -D -S -G www-data www-data && \  
apk add --update \  
php5-mcrypt \  
php5-soap \  
php5-openssl \  
php5-gmp \  
php5-json \  
php5-zlib \  
php5-dom \  
php5-pdo \  
php5-zip \  
php5-mysql \  
php5-mysqli \  
php5-sqlite3 \  
php5-apcu \  
php5-pdo_pgsql \  
php5-bcmath \  
php5-gd \  
php5-xcache \  
php5-odbc \  
php5-pdo_mysql \  
php5-pdo_sqlite \  
php5-gettext \  
php5-xmlreader \  
php5-xmlrpc \  
php5-bz2 \  
php5-memcache \  
php5-iconv \  
php5-curl \  
php5-ctype \  
php5-intl \  
php5-fpm && \  
  
  
  
touch /etc/php5/conf.d/custom.ini && \  
sed -i "s|;*daemonize\s*=\s*yes|daemonize = no|g" /etc/php5/php-fpm.conf && \  
sed -i "s|;*listen\s*=\s*127.0.0.1:9000|listen = 9000|g" /etc/php5/php-
fpm.conf && \  
sed -i "s|;*listen\s*=\s*/||g" /etc/php5/php-fpm.conf && \  
sed -i "s/;listen.owner = nobody/listen.owner = www-data/g" /etc/php5/php-
fpm.conf && \  
sed -i "s/;listen.group = nobody/listen.group = www-data/g" /etc/php5/php-
fpm.conf && \  
sed -i "s/user = nobody/user = www-data/g" /etc/php5/php-fpm.conf && \  
sed -i "s/group = nobody/group = www-data/g" /etc/php5/php-fpm.conf && \  
echo "date.timezone = ${TIMEZONE}" >>/etc/php5/conf.d/custom.ini && \  
echo "memory_limit = ${PHP_MEMORY_LIMIT}" >>/etc/php5/conf.d/custom.ini && \  
echo "upload_max_filesize = ${MAX_UPLOAD}" >>/etc/php5/conf.d/custom.ini && \  
echo "max_file_uploads = ${PHP_MAX_FILE_UPLOAD}" >>/etc/php5/conf.d/custom.ini
&& \  
echo "post_max_size = ${PHP_MAX_POST}" >>/etc/php5/conf.d/custom.ini && \  
echo "short_open_tag = ${SHORT_OPEN_TAG}" >>/etc/php5/conf.d/custom.ini && \  
echo "sendmail_path = /usr/sbin/sendmail -t -i -S opensmtpd:25"
>>/etc/php5/conf.d/custom.ini && \  
  
mkdir /usr/share/nginx && \  
mkdir /usr/share/nginx/html && \  
mkdir /usr/share/webapps && \  
chmod +rx /usr/share/webapps && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/* && \  
rm -rf /src && \  
rm -rf /var/cache/apk/*  
  
  
  
# Set Workdir  
WORKDIR /usr/share/nginx/html  
  
# Expose volumes  
VOLUME ["/usr/share/nginx/html"]  
  
# Expose ports  
EXPOSE 9000  
# Entry point  
ENTRYPOINT ["/usr/bin/php-fpm"]  

