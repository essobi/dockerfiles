FROM php:5.6-fpm-alpine3.4  
  
COPY etc/php/5.6 /etc/php/5.6  
  
RUN echo http://dl-cdn.alpinelinux.org/alpine/v3.5/community >>
/etc/apk/repositories && \  
apk add --no-cache --virtual php-deps \  
gettext \  
libxml2 \  
libxslt \  
openssl \  
pcre \  
readline \  
shadow && \  
groupmod -o -g 33 www-data && usermod -o -u 33 www-data  
  
ARG CONFIGURE_PARAMS="\  
--datadir=/usr/share/php/5.6 \  
--disable-all \  
--disable-cgi \  
--disable-debug \  
--disable-phpdbg \  
--disable-rpath \  
--disable-static \  
--enable-calendar=shared \  
--enable-ctype=shared \  
--enable-dom=shared \  
--enable-exif=shared \  
--enable-fileinfo=shared \  
--enable-filter \  
--enable-ftp=shared \  
--enable-json=shared \  
--enable-libxml \  
--enable-mysqlnd=shared \  
--enable-opcache=shared \  
--enable-pdo=shared \  
--enable-phar=shared \  
--enable-posix=shared \  
--enable-session \  
--enable-shmop=shared \  
--enable-simplexml=shared \  
--enable-sockets=shared \  
--enable-sysvmsg=shared \  
--enable-sysvsem=shared \  
--enable-sysvshm=shared \  
--enable-tokenizer=shared \  
--enable-wddx=shared \  
--enable-xml=shared \  
--enable-xmlreader=shared \  
--enable-xmlwriter=shared \  
--includedir=/usr/include \  
--infodir=/usr/share/info \  
--libdir=/usr/lib/php \  
--libexecdir=/usr/lib/php \  
--localstatedir=/var \  
--mandir=/usr/share/man \  
--prefix=/usr \  
--sysconfdir=/etc \  
--with-gettext=shared \  
--with-iconv=shared \  
--with-mhash=/usr \  
--with-openssl=yes \  
--with-pcre-regex=/usr \  
--with-pic \  
--with-readline=shared \  
--with-xsl=shared \  
--with-zlib-dir=/usr \  
--with-zlib=/usr \  
--without-pear"  
  
RUN rm -f \  
/usr/local/bin/pear \  
/usr/local/bin/peardev \  
/usr/local/bin/pecl \  
/usr/local/bin/phar \  
/usr/local/bin/phar.phar \  
/usr/local/bin/php \  
/usr/local/bin/php-config \  
/usr/local/bin/phpize \  
/usr/local/sbin/php-fpm  
  
  
RUN apk add --no-cache --virtual php-build-deps \  
autoconf \  
g++ \  
gcc \  
gettext-dev \  
libxml2-dev \  
libxslt-dev \  
make \  
mariadb-dev \  
openssl-dev \  
pcre-dev \  
readline-dev && \  
docker-php-source extract && \  
cd /usr/src/php && \  
export CFLAGS="-g -O2 -fPIE -fstack-protector-strong -Wformat -Werror=format-
security -O2 -Wall -pedantic -fsigned-char -fno-strict-aliasing -g" && \  
export CPPFLAGS="-Wdate-time -D_FORTIFY_SOURCE=2" && \  
export CXXFLAGS="-g -O2 -fPIE -fstack-protector-strong -Wformat
-Werror=format-security" && \  
export LDFLAGS="-Wl,-Bsymbolic-functions -fPIE -pie -Wl,-z,relro -Wl,-z,now
-Wl,--as-needed" && \  
./configure $CONFIGURE_PARAMS \  
--with-config-file-path=/etc/php/5.6/fpm \  
--with-config-file-scan-dir=/etc/php/5.6/fpm/conf.d \  
--disable-cli \  
--disable-pcntl \  
--enable-fpm \  
--with-fpm-user=www-data \  
--with-fpm-group=www-data && \  
make && \  
make install && \  
./configure $CONFIGURE_PARAMS \  
--with-config-file-path=/etc/php/5.6/cli \  
--with-config-file-scan-dir=/etc/php/5.6/cli/conf.d \  
--enable-pcntl \  
--enable-cli && \  
grep -rl '5.6/fpm' . | sort -u | while read file; do sed -i -r -e
's!5.6/fpm!5.6/cli!g' ${file}; done && \  
make && \  
make install && \  
docker-php-source delete && \  
apk del php-build-deps  
  
RUN php -r 'copy("http://pear.php.net/install-pear-nozlib.phar",
"/tmp/install-pear-nozlib.phar");' && \  
PHP_PEAR_SYSCONF_DIR=/etc/pear php -n -dshort_open_tag=0 -dopen_basedir=
-derror_reporting=1803 -dmemory_limit=-1 -ddetect_unicode=0 -f /tmp/install-
pear-nozlib.phar -- \  
--dir /usr/share/php \  
--bin $(dirname $(which php)) \  
--config /usr/share/php/cfg \  
--www /usr/share/php/www \  
--php $(which php) \  
--download /tmp/pear/download \  
--temp /tmp/pear/temp \  
--data /usr/share/php/data \  
--doc /usr/share/php/docs \  
--test /usr/share/php/tests \  
--man /usr/share/man && \  
sed -i -r -e "s!PHP_SYSCONFDIR\\);!PHP_SYSCONFDIR . '/pear');!g"
/usr/share/php/PEAR/Config.php && \  
sed -i "$ s|\\-n||g" /usr/bin/pecl && \  
rm /tmp/install-pear-nozlib.phar  
  
ARG LOGFILES="/var/log/php5.6-fpm.log"  
  
ENV LOGFILES=$LOGFILES  
  
RUN rm $LOGFILES || :; \  
mkdir -p /run/php  
  
COPY usr/local /usr/local  
  
ENTRYPOINT ["/usr/local/bin/logged-stdout"]  
  
EXPOSE 9000  
  
CMD ["php-fpm", "-F", "-y/etc/php/5.6/fpm/php-fpm.conf",
"-c/etc/php/5.6/fpm/"]

