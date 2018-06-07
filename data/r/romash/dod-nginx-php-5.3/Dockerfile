FROM romash/dod-nginx:1.10.1-s6-prod  
MAINTAINER Romash <tcp6000@gmail.com>  
  
# Create user www-data  
RUN adduser -u 82 -D -S -G www-data www-data  
  
# Install packages  
RUN export PHP_VER="5.3.29" && \  
  
# Install dev packages  
echo '@edge http://nl.alpinelinux.org/alpine/edge/main' >>
/etc/apk/repositories && \  
echo '@testing http://nl.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories && \  
echo '@community http://nl.alpinelinux.org/alpine/edge/community' >>
/etc/apk/repositories && \  
apk \--update upgrade && \  
apk add \  
libxml2-dev \  
openssl-dev \  
bzip2-dev \  
curl-dev \  
jpeg-dev \  
libpng-dev \  
libxpm-dev \  
freetype-dev \  
gettext-dev \  
gmp-dev \  
imap-dev \  
krb5-dev \  
icu-dev \  
openldap-dev \  
libmcrypt-dev \  
freetds-dev \  
enchant-dev \  
aspell-dev \  
readline-dev \  
libedit-dev \  
net-snmp-dev \  
tidyhtml-dev@community \  
libxslt-dev \  
imagemagick-dev \  
db-dev \  
gdbm-dev \  
build-base \  
autoconf \  
libtool && \  
  
# Fix tidybuffio issue  
mkdir -p /usr/include/freetype2/freetype && \  
cp /usr/include/tidybuffio.h /usr/include/buffio.h && \  
  
# Download PHP src and configure  
wget -qO- http://php.net/get/php-${PHP_VER}.tar.gz/from/this/mirror | tar xz
-C /tmp && \  
cd /tmp/php-${PHP_VER} && \  
./configure \  
\--prefix=/usr \  
\--sysconfdir=/etc/php \  
\--localstatedir=/var \  
\--with-config-file-path=/etc/php \  
\--with-config-file-scan-dir=/etc/php/conf.d \  
\--mandir=/usr/share/man \  
\--disable-rpath \  
\--disable-debug \  
\--disable-static \  
\--disable-embed \  
\--enable-inline-optimization \  
\--enable-fpm \  
\--enable-pcntl \  
\--enable-mbregex \  
\--enable-mbstring \  
\--enable-shared \  
\--enable-session \  
\--enable-pdo=shared \  
\--enable-xml=shared \  
\--enable-libxml=shared \  
\--enable-bcmath=shared \  
\--enable-calendar=shared \  
\--enable-exif=shared \  
\--enable-ftp=shared \  
\--enable-json=shared \  
\--enable-pcntl=shared \  
\--enable-dba=shared \  
\--with-gdbm=shared \  
\--enable-phar=shared \  
\--enable-posix=shared \  
\--enable-ctype=shared \  
\--enable-shmop=shared \  
\--enable-soap=shared \  
\--enable-sockets=shared \  
\--enable-sysvmsg=shared \  
\--enable-sysvsem=shared \  
\--enable-xmlreader=shared \  
\--enable-sysvshm=shared \  
\--enable-zip=shared \  
\--enable-wddx=shared \  
\--enable-intl=shared \  
\--enable-dom=shared \  
\--with-bz2=shared \  
\--with-curl=shared \  
\--with-enchant=shared \  
\--with-gd=shared \  
\--with-jpeg-dir=shared,/usr \  
\--with-png-dir=shared,/usr \  
\--with-freetype-dir=shared,/usr \  
\--enable-gd-native-ttf \  
\--enable-gd-jis-conv \  
\--with-xmlrpc=shared \  
\--with-iconv=shared \  
\--with-gettext=shared \  
\--with-zlib=shared \  
\--with-openssl=shared \  
\--with-kerberos \  
\--with-imap=shared \  
\--with-imap-ssl=shared \  
\--with-ldap=shared \  
\--with-ldap-sasl \  
\--with-mcrypt=shared \  
\--with-gmp=shared \  
\--with-mysql=shared,mysqlnd \  
\--with-mysql-sock=/var/run/mysqld/mysqld.sock \  
\--with-zlib-dir=shared \  
\--with-pdo-mysql=shared,mysqlnd \  
\--with-mysql=shared,mysqlnd \  
\--with-mysqli=shared,mysqlnd \  
\--with-pdo-dblib=shared \  
\--with-pspell=shared \  
\--with-snmp=shared \  
\--with-tidy=shared \  
\--with-xsl=shared \  
\--with-layout=GNU \  
\--with-regex=php \  
\--with-icu-dir=/usr \  
\--with-pcre-regex \  
\--with-readline \  
\--with-pear \  
\--with-pic \  
\--with-libdir=lib \  
\--with-iconv=shared \  
\--without-db1 \  
\--without-db2 \  
\--without-db3 \  
\--without-db4 \  
\--without-qdbm \  
\--without-pdo_sqlite \  
\--without-sqlite \  
\--without-sqlite3 \  
\--without-apache && \  
  
# Make and install PHP  
make CC='gcc' CFLAGS='-Os -fomit-frame-pointer -g' LDFLAGS='-Wl,\--as-needed'
CPPFLAGS='-Os -fomit-frame-pointer' CXXFLAGS='-Os -fomit-frame-pointer -g' &&
\  
make install && \  
  
# Minize compiled php bins and create symlink  
strip /usr/bin/php /usr/sbin/php-fpm /usr/lib/php/20090626/* && \  
ln -sf /usr/sbin/php-fpm /usr/bin/php-fpm && \  
ln -sfn /usr/lib/php/20090626 /usr/lib/php/modules && \  
  
# Copy default php.ini and configure it  
cp php.ini-production /etc/php/php.ini && \  
sed -i \  
-e "s/^expose_php.*/expose_php = Off/" \  
-e "s/^;date.timezone.*/date.timezone = UTC/" \  
-e "s/^memory_limit.*/memory_limit = -1/" \  
-e "s/^max_execution_time.*/max_execution_time = 600/" \  
-e "s/^post_max_size.*/post_max_size = 2048M/" \  
-e "s/^upload_max_filesize.*/upload_max_filesize = 2048M/" \  
# -e "s@^;sendmail_path.*@sendmail_path = /usr/sbin/sendmail -t -i -S
opensmtpd:25@" \  
/etc/php/php.ini && \  
echo "extension_dir = /usr/lib/php/modules" | tee -a /etc/php/php.ini && \  
echo "error_log = /var/log/php/error.log" | tee -a /etc/php/php.ini && \  
  
# Configure PHP extensions  
mkdir -p /etc/php/conf.d && \  
echo 'extension=bz2.so' > /etc/php/conf.d/bz2.ini && \  
echo 'extension=calendar.so' > /etc/php/conf.d/calendar.ini && \  
echo 'extension=ctype.so' > /etc/php/conf.d/ctype.ini && \  
echo 'extension=curl.so' > /etc/php/conf.d/curl.ini && \  
echo 'extension=dom.so' > /etc/php/conf.d/dom.ini && \  
echo 'extension=ftp.so' > /etc/php/conf.d/ftp.ini && \  
echo 'extension=gd.so' > /etc/php/conf.d/gd.ini && \  
echo 'extension=mcrypt.so' > /etc/php/conf.d/mcrypt.ini && \  
echo 'extension=mysql.so' > /etc/php/conf.d/mysql.ini && \  
echo 'extension=mysqli.so' > /etc/php/conf.d/mysqli.ini && \  
echo 'extension=pcntl.so' > /etc/php/conf.d/pcntl.ini && \  
echo 'extension=pdo.so' > /etc/php/conf.d/pdo.ini && \  
echo 'extension=pdo_mysql.so' > /etc/php/conf.d/pdo_mysql.ini && \  
echo 'extension=redis.so' > /etc/php/conf.d/redis.ini && \  
echo 'extension=sockets.so' > /etc/php/conf.d/sockets.ini && \  
echo 'extension=zip.so' > /etc/php/conf.d/zip.ini && \  
echo 'extension=zlib.so' > /etc/php/conf.d/zlib.ini && \  
echo 'extension=xml.so' > /etc/php/conf.d/xml.ini && \  
echo 'extension=json.so' > /etc/php/conf.d/json.ini && \  
echo 'extension=phar.so' > /etc/php/conf.d/phar.ini && \  
echo 'extension=openssl.so' > /etc/php/conf.d/openssl.ini && \  
echo 'extension=posix.so' > /etc/php/conf.d/posix.ini && \  
echo 'extension=iconv.so' > /etc/php/conf.d/iconv.ini && \  
echo 'extension=imap.so' > /etc/php/conf.d/imap.ini && \  
echo 'extension=soap.so' > /etc/php/conf.d/soap.ini && \  
  
# Configure php log dir  
mkdir -p /var/log/php && \  
touch /var/log/php/error.log && \  
touch /var/log/php/fpm-error.log && \  
touch /var/log/php/fpm-slow.log && \  
chown -R www-data:www-data /var/log/php && \  
  
# Install PHP extensions through Pecl  
sed -ie 's/-n//g' `which pecl` && \  
pecl install ZendOpcache-7.0.5 && \  
pecl install xdebug-2.2.7 && \  
pecl install uploadprogress-1.0.3.1 && \  
pecl install redis-2.2.8 && \  
echo '\n' | pecl install imagick-3.3.0 && \  
echo '\n' | pecl install memcache-2.2.7 && \  
  
# Enable PHP extensions (OPcache and Xdebug ini are overrided in rootfs)  
echo 'extension=uploadprogress.so' > /etc/php/conf.d/uploadprogress.ini && \  
echo 'extension=uploadprogress.so' > /etc/php/conf.d/uploadprogress.ini && \  
echo 'extension=redis.so' > /etc/php/conf.d/redis.ini && \  
echo 'extension=imagick.so' > /etc/php/conf.d/imagick.ini && \  
echo 'extension=memcache.so' > /etc/php/conf.d/memcache.ini && \  
  
# Cleanup after PHP build  
cd / && rm -rf /usr/include/php /usr/lib/php/build /usr/lib/php/modules/*.a &&
\  
  
# Install APK packaged  
apk add \  
git \  
tar \  
sed \  
grep \  
wget \  
curl \  
pwgen \  
openssh \  
rsync \  
patch \  
patchutils \  
mariadb-client \  
krb5-libs \  
redis \  
nano \  
bash \  
diffutils \  
zlib \  
libxml2 \  
readline \  
freetype \  
libjpeg-turbo \  
libpng \  
curl \  
imap \  
c-client \  
libltdl \  
libmcrypt \  
libbz2 \  
libssl1.0 \  
libcrypto1.0 \  
imagemagick \  
gzip && \  
  
# Remove Redis binaries and config  
ls /usr/bin/redis-* | grep -v redis-cli | xargs rm && \  
rm -f /etc/redis.conf && \  
  
# Install composer  
curl -sS https://getcomposer.org/installer | php -- \--install-
dir=/usr/local/bin \--filename=composer && \  
  
# Add composer parallel install plugin  
composer global require "hirak/prestissimo:^0.3" && \  
  
# Install drush  
git clone https://github.com/drush-ops/drush.git /usr/local/src/drush && \  
cd /usr/local/src/drush && \  
git checkout 7.2.0 && \  
ln -sf /usr/local/src/drush/drush /usr/bin/drush && \  
composer install && rm -rf ./.git && \  
  
# Cleanup  
apk del \--purge *-dev build-base autoconf libtool && \  
rm -rf /usr/include/php /usr/lib/php/build && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/* && \  
rm -rf /usr/share/man  
  
COPY rootfs /  
  
#cron  
RUN chmod a+x /etc/periodic/15min/drupal_cron && \  
chmod a+x /etc/periodic/daily/backup_db && \  
chmod a+x /etc/periodic/daily/backup_files  
  
WORKDIR /var/www/html  

