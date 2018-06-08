FROM alpine:edge  
MAINTAINER Wodby <admin@wodby.com>  
  
# Create user www-data  
RUN addgroup -g 82 -S www-data && \  
adduser -u 82 -D -S -G www-data www-data  
  
# Install packages  
RUN echo 'http://nl.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories && \  
  
apk add --update \  
# Base packages  
openssl \  
ca-certificates \  
git \  
curl \  
wget \  
perl \  
pcre \  
imap \  
imagemagick \  
mariadb-client \  
bash \  
bash-doc \  
bash-completion \  
subversion \  
# Temp packages  
build-base \  
autoconf \  
libtool \  
php7-dev \  
pcre-dev \  
imagemagick-dev \  
# PHP packages  
php7 \  
php7-fpm \  
php7-opcache \  
php7-xml \  
php7-ctype \  
php7-ftp \  
php7-gd \  
php7-json \  
php7-posix \  
php7-curl \  
php7-dom \  
php7-pdo \  
php7-pdo_mysql \  
php7-sockets \  
php7-zlib \  
php7-mcrypt \  
php7-mysqli \  
php7-sqlite3 \  
php7-bz2 \  
php7-phar \  
php7-openssl \  
php7-posix \  
php7-zip \  
php7-calendar \  
php7-iconv \  
php7-imap \  
php7-soap \  
php7-pear \  
php7-redis \  
php7-mbstring \  
php7-xdebug \  
php7-memcached \  
php7-exif && \  
# Create symlinks for backward compatibility  
ln -sf /usr/bin/php7 /usr/bin/php && \  
ln -sf /usr/sbin/php-fpm7 /usr/bin/php-fpm && \  
# Install imagick  
sed -ie 's/-n//g' /usr/bin/pecl && \  
yes | pecl install imagick && \  
echo 'extension=imagick.so' > /etc/php7/conf.d/imagick.ini && \  
rm -rf /tmp/pear && \  
# Install uploadprogess  
cd /tmp/ && wget https://github.com/Jan-E/uploadprogress/archive/master.zip &&
\  
unzip master.zip && \  
cd uploadprogress-master/ && \  
phpize7 && ./configure --with-php-config=/usr/bin/php-config7 && \  
make && make install && \  
echo 'extension=uploadprogress.so' > /etc/php7/conf.d/20_uploadprogress.ini &&
\  
cd .. && rm -rf ./master.zip ./uploadprogress-master && \  
  
# Install composer  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
# Add composer parallel install plugin  
composer global require "hirak/prestissimo:^0.3" && \  
composer global require "phpunit/phpunit" && \  
  
ln -sf "/root/.composer/vendor/bin/phpunit" /usr/local/bin/ && \  
# Install wp-cli  
composer create-project wp-cli/wp-cli /usr/local/src/wp-cli --no-dev && \  
ln -sf /usr/local/src/wp-cli/bin/wp /usr/bin/wp && \  
# Cleanup  
apk del --purge *-dev build-base autoconf libtool && \  
rm -rf /usr/include/php /usr/lib/php/build && \  
rm -rf /var/cache/apk/*  
  
# Configure php.ini  
RUN sed -i \  
-e "s/^expose_php.*/expose_php = Off/" \  
-e "s/^;date.timezone.*/date.timezone = UTC/" \  
-e "s/^memory_limit.*/memory_limit = -1/" \  
-e "s/^max_execution_time.*/max_execution_time = 300/" \  
-e "s/^post_max_size.*/post_max_size = 512M/" \  
-e "s/^upload_max_filesize.*/upload_max_filesize = 512M/" \  
-e "s/^error_reporting.*/error_reporting = E_ALL/" \  
-e "s/^display_errors.*/display_errors = On/" \  
-e "s/^display_startup_errors.*/display_startup_errors = On/" \  
-e "s/^track_errors.*/track_errors = On/" \  
-e "s/^mysqlnd.collect_memory_statistics.*/mysqlnd.collect_memory_statistics = On/" \  
/etc/php7/php.ini && \  
  
echo "error_log = \"/proc/self/fd/2\"" | tee -a /etc/php7/php.ini  
  
RUN rm /etc/php7/conf.d/xdebug.ini  
COPY 00_opcache.ini /etc/php7/conf.d/  
COPY 00_xdebug.ini /etc/php7/conf.d/  
COPY php-fpm.conf /etc/php7/  
# Create work dir  
RUN mkdir -p /var/www/html && chown -R 82:82 /var/www  
WORKDIR /var/www/html  
VOLUME /var/www/html  
  
EXPOSE 9000 9999  
  
COPY docker-entrypoint.sh /usr/local/bin/  
CMD "docker-entrypoint.sh"  

