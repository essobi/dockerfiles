FROM romash/dod-nginx  
MAINTAINER Romash <tcp6000@gmail.com>  
  
RUN adduser -u 82 -D -S -G www-data www-data && \  
  
echo '@edge http://nl.alpinelinux.org/alpine/edge/main' >>
/etc/apk/repositories && \  
echo '@testing http://nl.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories && \  
echo '@community http://nl.alpinelinux.org/alpine/edge/community' >>
/etc/apk/repositories && \  
# Install common packages  
apk add --update \  
openssh \  
git \  
grep \  
pcre \  
perl \  
patch \  
patchutils \  
diffutils \  
&& \  
# Install specific packages  
apk add --update \  
mariadb-client \  
imap \  
redis \  
imagemagick \  
&& \  
# PHP packages  
apk add --update \  
php5 \  
php5-common \  
php5-cli \  
php5-fpm \  
php5-opcache \  
php5-dom \  
php5-xml \  
php5-xmlreader \  
php5-ctype \  
php5-ftp \  
php5-gd \  
php5-json \  
php5-posix \  
php5-curl \  
php5-pdo \  
php5-pdo_mysql \  
php5-sockets \  
php5-zlib \  
php5-mcrypt \  
php5-pcntl \  
php5-mysql \  
php5-mysqli \  
php5-sqlite3 \  
php5-bz2 \  
php5-pear \  
php5-exif \  
php5-phar \  
php5-openssl \  
php5-zip \  
php5-calendar \  
php5-iconv \  
php5-imap \  
php5-soap \  
php5-memcache \  
php5-redis@testing \  
php5-xdebug \  
php5-xsl \  
php5-ldap \  
php5-bcmath \  
php5-memcached@testing \  
&& \  
# Configure php.ini  
sed -i \  
-e "s/^expose_php.*/expose_php = Off/" \  
-e "s/^;date.timezone.*/date.timezone = UTC/" \  
-e "s/^memory_limit.*/memory_limit = -1/" \  
-e "s/^max_execution_time.*/max_execution_time = 600/" \  
-e "s/^post_max_size.*/post_max_size = 2048M/" \  
-e "s/^upload_max_filesize.*/upload_max_filesize = 2048M/" \  
-e "s/^;always_populate_raw_post_data.*/always_populate_raw_post_data = -1/" \  
# -e "s/^error_reporting.*/error_reporting = E_ALL/" \  
# -e "s/^display_errors.*/display_errors = On/" \  
# -e "s/^display_startup_errors.*/display_startup_errors = On/" \  
# -e "s/^track_errors.*/track_errors = On/" \  
# -e "s/^mysqlnd.collect_memory_statistics.*/mysqlnd.collect_memory_statistics
= On/" \  
/etc/php5/php.ini && \  
  
echo "error_log = \"/var/log/php/error.log\"" | tee -a /etc/php5/php.ini && \  
# Configure php log dir  
mkdir /var/log/php && \  
touch /var/log/php/error.log && \  
touch /var/log/php/fpm-error.log && \  
touch /var/log/php/fpm-slow.log && \  
chown -R www-data:www-data /var/log/php && \  
# Install Dev tools  
apk add --update \  
php5-dev \  
pcre-dev \  
build-base \  
autoconf \  
libtool \  
&& \  
# Install PHP extensions through Pecl  
sed -ie 's/-n//g' /usr/bin/pecl && \  
echo '\n' | pecl install uploadprogress && \  
apk --update add imagemagick-dev && \  
echo '\n' | pecl install imagick && \  
echo 'extension=imagick.so' > /etc/php5/conf.d/imagick.ini && \  
echo 'extension=uploadprogress.so' > /etc/php5/conf.d/uploadprogress.ini && \  
# Define Git global config  
git config --global user.name "Roman A. Shvetsov" && \  
git config --global user.email "tcp6000@gmail.com" && \  
git config --global push.default current && \  
# Disable Xdebug  
rm /etc/php5/conf.d/xdebug.ini && \  
# Install composer  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
  
# Add composer parallel install plugin  
composer global require "hirak/prestissimo:^0.3" && \  
  
# Install drush  
php -r "readfile('https://s3.amazonaws.com/files.drush.org/drush.phar');" >
/usr/local/bin/drush && \  
chmod +x /usr/local/bin/drush && \  
  
# Install Drupal Console  
curl https://drupalconsole.com/installer -o /usr/local/bin/drupal && \  
chmod +x /usr/local/bin/drupal && \  
  
# Fix permissions  
chmod 755 /root && \  
chown -R www-data:www-data /var/www/html && \  
  
# Remove redis binaries and config  
ls /usr/bin/redis-* | grep -v redis-cli | xargs rm && \  
rm -f /etc/redis.conf && \  
  
# Cleanup  
apk del --purge \  
*-dev \  
build-base \  
autoconf \  
libtool \  
&& \  
  
rm -rf \  
/usr/include/php5 \  
/usr/lib/php5/build \  
/usr/lib/php5/modules/*.a \  
/var/cache/apk/* \  
/usr/share/man \  
/tmp/* \  
/root/.composer  
  
COPY rootfs /  
  
WORKDIR /var/www/html  
  
  
  

