FROM romash/dod-nginx  
MAINTAINER Romash <tcp6000@gmail.com>  
  
RUN export UPLOADPROGRESS_VER="0.1.0" && \  
export XDEBUG_VER="2.4.0" && \  
  
adduser -u 82 -D -S -G www-data www-data && \  
  
echo 'http://alpine.gliderlabs.com/alpine/edge/main' > /etc/apk/repositories
&& \  
echo 'http://alpine.gliderlabs.com/alpine/edge/community' >>
/etc/apk/repositories && \  
echo 'http://alpine.gliderlabs.com/alpine/edge/testing' >>
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
# Install PHP packages  
apk add \  
php7 \  
php7-fpm \  
php7-opcache \  
php7-session \  
php7-dom \  
php7-xml \  
php7-xmlreader \  
php7-ctype \  
php7-ftp \  
php7-gd \  
php7-json \  
php7-posix \  
php7-curl \  
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
php7-zip \  
php7-calendar \  
php7-iconv \  
php7-imap \  
php7-soap \  
php7-dev \  
php7-pear \  
php7-redis \  
php7-mbstring \  
php7-xdebug \  
php7-exif \  
php7-xsl \  
php7-ldap \  
php7-bcmath \  
php7-memcached \  
php7-oauth \  
php7-apcu \  
&& \  
# Create symlinks PHP -> PHP7  
ln -sf /usr/bin/php7 /usr/bin/php && \  
ln -sf /usr/sbin/php-fpm7 /usr/bin/php-fpm && \  
# Configure php.ini  
sed -i \  
-e "s/^expose_php.*/expose_php = Off/" \  
-e "s/^;date.timezone.*/date.timezone = UTC/" \  
-e "s/^memory_limit.*/memory_limit = -1/" \  
-e "s/^max_execution_time.*/max_execution_time = 600/" \  
-e "s/^post_max_size.*/post_max_size = 2048M/" \  
-e "s/^upload_max_filesize.*/upload_max_filesize = 2048M/" \  
/etc/php7/php.ini && \  
  
echo "error_log = \"/var/log/php/error.log\"" | tee -a /etc/php7/php.ini && \  
# Configure php log dir  
rm -rf /var/log/php7 && \  
mkdir /var/log/php && \  
touch /var/log/php/error.log && \  
touch /var/log/php/fpm-error.log && \  
touch /var/log/php/fpm-slow.log && \  
chown -R www-data:www-data /var/log/php && \  
# Install uploadprogess extension  
apk add --update build-base autoconf libtool pcre-dev && \  
wget -qO- https://s3.amazonaws.com/wodby-
releases/uploadprogress/v${UPLOADPROGRESS_VER}/php7-uploadprogress.tar.gz |
tar xz -C /tmp/ && \  
cd /tmp/uploadprogress-${UPLOADPROGRESS_VER} && \  
phpize7 && \  
./configure --with-php-config=/usr/bin/php-config7 && \  
make && \  
make install && \  
echo 'extension=uploadprogress.so' > /etc/php7/conf.d/uploadprogress.ini && \  
  
# Define Git global config  
git config --global user.name "Roman A. Shvetsov" && \  
git config --global user.email "tcp6000@gmail.com" && \  
git config --global push.default current && \  
  
# Disable Xdebug  
rm /etc/php7/conf.d/xdebug.ini && \  
  
# Install composer  
curl -sS https://getcomposer.org/installer | php7 -- --install-
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
/usr/include/php7 \  
/usr/lib/php7/build \  
/usr/lib/php7/modules/*.a \  
/var/cache/apk/* \  
/usr/share/man \  
/tmp/* \  
/root/.composer  
  
COPY rootfs /  
  
WORKDIR /var/www/html  
  
  

