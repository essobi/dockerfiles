FROM usijo/docker-alpine  
MAINTAINER Hongshun Yang<ojisucom@gmail.com>  
  
## php5-fpm/cli/cgi with zts  
RUN echo '@php5_zts http://php5-zts.ddns.net/repo/alpine/main' >>
/etc/apk/repositories  
  
## 当尝试安装php扩展时，尽量使用php5-xx@php5_zts  
## 比如pecl install pthreads 需要php5-dev@php5_zts  
#php5-apache2@php5_zts \  
#php5-ftp@php5_zts \  
#php5-ldap@php5_zts \  
#php5-mssql@php5_zts \  
#php5-odbc@php5_zts \  
#php5-pdo_odbc@php5_zts \  
#php5-pdo_pgsql@php5_zts \  
#php5-pdo_sqlite@php5_zts \  
#php5-pgsql@php5_zts \  
#php5-sqlite3@php5_zts \  
#php5-wddx@php5_zts \  
#php5-doc@php5_zts \  
#php5-pspell@php5_zts \  
RUN apk add -U php5@php5_zts \  
php5-calendar@php5_zts \  
php5-bcmath@php5_zts \  
php5-bz2@php5_zts \  
php5-cgi@php5_zts \  
php5-cli@php5_zts \  
php5-common@php5_zts \  
php5-ctype@php5_zts \  
php5-curl@php5_zts \  
php5-dba@php5_zts \  
php5-dbg@php5_zts \  
php5-dev@php5_zts \  
php5-dom@php5_zts \  
php5-embed@php5_zts \  
php5-enchant@php5_zts \  
php5-exif@php5_zts \  
php5-fpm@php5_zts \  
php5-gd@php5_zts \  
php5-gettext@php5_zts \  
php5-gmp@php5_zts \  
php5-iconv@php5_zts \  
php5-imap@php5_zts \  
php5-intl@php5_zts \  
php5-json@php5_zts \  
php5-mcrypt@php5_zts \  
php5-mysql@php5_zts \  
php5-mysqli@php5_zts \  
php5-opcache@php5_zts \  
php5-openssl@php5_zts \  
php5-pcntl@php5_zts \  
php5-pdo@php5_zts \  
php5-pdo_dblib@php5_zts \  
php5-pdo_mysql@php5_zts \  
php5-pear@php5_zts \  
php5-phar@php5_zts \  
php5-phpdbg@php5_zts \  
php5-posix@php5_zts \  
php5-shmop@php5_zts \  
php5-snmp@php5_zts \  
php5-soap@php5_zts \  
php5-sockets@php5_zts \  
php5-sysvmsg@php5_zts \  
php5-sysvsem@php5_zts \  
php5-sysvshm@php5_zts \  
php5-xml@php5_zts \  
php5-xmlreader@php5_zts \  
php5-xmlrpc@php5_zts \  
php5-xsl@php5_zts \  
php5-zip@php5_zts \  
php5-zlib@php5_zts  
  
## support pear pecl  
## fix pecl (xml extension)  
RUN sed -i "$ s|\\-n||g" /usr/bin/pecl  
  
#ENV pecl_memcached_ver 2.2.0  
#&& pecl download memcached-${pecl_memcached_ver} \  
#&& tar xzvf memcached-${pecl_memcached_ver}.tgz \  
#&& cd memcached-${pecl_memcached_ver}/ \  
#&& phpize && ./configure --disable-memcached-sasl && make && make install \  
#&& cd .. \  
#&& rm -r memcached-${pecl_memcached_ver}  
ENV LIBICONV_VERSION 1.15  
ENV LIBICONV_DOWNLOAD_URL
http://ftp.gnu.org/pub/gnu/libiconv/libiconv-$LIBICONV_VERSION.tar.gz  
  
## libdatrie 0.2.10 not work  
ENV LIBDATRIE_VERSION 0.2.9  
ENV LIBDATRIE_DOWNLOAD_URL
ftp://sourceforge.mirrorservice.org/sites/distfiles.finkmirrors.net/libdatrie-$LIBDATRIE_VERSION.tar.xz  
  
  
## install runkit for hot deploy swoole code  
RUN apk add -U pcre-dev imagemagick-dev libmemcached-dev zlib-dev cyrus-sasl-
dev \  
&& apk add -U --virtual build-deps autoconf build-base linux-headers git
libtool \  
&& pecl install apcu-4.0.10 \  
&& pecl install imagick-3.4.2 \  
&& pecl install memcached-2.2.0 \  
&& pecl install redis-2.2.8 \  
&& pecl install pthreads-2.0.10 \  
&& pecl install runkit-1.0.4 \  
&& cd /tmp/ \  
&& wget -qO- $LIBICONV_DOWNLOAD_URL | tar xvz \  
&& cd libiconv-$LIBICONV_VERSION \  
&& ./configure && make && make install \  
&& cd /tmp/ \  
&& wget $LIBDATRIE_DOWNLOAD_URL \  
&& tar xvf libdatrie-$LIBDATRIE_VERSION.tar.xz \  
&& cd libdatrie-$LIBDATRIE_VERSION \  
&& ./configure && make && make install \  
&& cd /tmp/ \  
&& git clone https://github.com/wulijun/php-ext-trie-filter.git \  
&& cd php-ext-trie-filter \  
&& phpize \  
&& ./configure && make && make install \  
&& cd ~ \  
&& rm -rf /tmp/* \  
&& apk del -U build-deps \  
&& rm -rf /var/cache/apk/*  
  
RUN echo "extension=apcu.so" > /etc/php5/conf.d/apcu.ini  
RUN echo "extension=imagick.so" > /etc/php5/conf.d/imagick.ini  
RUN echo "extension=memcached.so" > /etc/php5/conf.d/memcached.ini  
RUN echo "extension=redis.so" > /etc/php5/conf.d/redis.ini  
RUN echo "extension=pthreads.so" > /etc/php5/conf.d/pthreads.ini  
RUN echo "extension=trie_filter.so" > /etc/php5/conf.d/trie_filter.ini  
RUN echo "extension=runkit.so" > /etc/php5/conf.d/runkit.ini  
  
  
## listen [::]:9000  
COPY tmpl/_etc_php5_php-fpm.conf.tmpl /etc/php5/php-fpm.conf.tmpl  
  
RUN mkdir -p /var/www/html  
  
VOLUME /var/www/html  
  
EXPOSE 9000  
#todo log  
## --nodaemonize  
CMD ["dockerize", "-template","/etc/php5/php-fpm.conf.tmpl:/etc/php5/php-
fpm.conf","php-fpm","-F"]  
  

