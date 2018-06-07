# vim:set ft=dockerfile:  
FROM debian:jessie  
MAINTAINER DongNan <dongyh@126.com>  
  
# 替换apt源  
#COPY 163.sources.list /etc/apt/sources.list  
# add gosu for easy step-down from root  
ENV GOSU_VERSION=1.7  
  
RUN set -x \  
&& apt-get update && apt-get install -y \--no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg \--keyserver ha.pool.sks-keyservers.net \--recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg \--batch \--verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get purge -y \--auto-remove ca-certificates wget  
  
RUN mkdir /docker-entrypoint-initdb.d  
# install "pwgen" for randomizing passwords  
# install "apt-transport-https" for Percona's repo (switched to https-only)  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
apt-transport-https ca-certificates \  
pwgen \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GPG_KEYS \  
# pub 1024D/CD2EFD2A 2009-12-15  
# Key fingerprint = 430B DF5C 56E7 C94E 848E E60C 1C4C BDCD CD2E FD2A  
# uid Percona MySQL Development Team <mysql-dev@percona.com>  
# sub 2048g/2D607DAF 2009-12-15  
430BDF5C56E7C94E848EE60C1C4CBDCDCD2EFD2A \  
# pub 4096R/8507EFA5 2016-06-30  
# Key fingerprint = 4D1B B29D 63D9 8E42 2B21 13B1 9334 A25F 8507 EFA5  
# uid Percona MySQL Development Team (Packaging key) <mysql-dev@percona.com>  
# sub 4096R/4CAC6D72 2016-06-30  
4D1BB29D63D98E422B2113B19334A25F8507EFA5  
RUN set -ex; \  
export GNUPGHOME="$(mktemp -d)"; \  
for key in $GPG_KEYS; do \  
gpg \--keyserver ha.pool.sks-keyservers.net \--recv-keys "$key"; \  
done; \  
gpg \--export $GPG_KEYS > /etc/apt/trusted.gpg.d/percona.gpg; \  
rm -r "$GNUPGHOME"; \  
apt-key list  
  
# 安装 mysql (percona-5.7)  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
  
ENV PERCONA_MAJOR=5.7 \  
PERCONA_VERSION=5.7.17-12-1.jessie \  
MYSQL_DATA_DIR=/data/mysql  
  
RUN echo 'deb https://repo.percona.com/apt jessie main' >
/etc/apt/sources.list.d/percona.list  
# we set debconf keys to make APT a little quieter  
RUN { \  
echo percona-server-server-$PERCONA_MAJOR percona-server-server/root_password
password 'unused'; \  
echo percona-server-server-$PERCONA_MAJOR percona-server-
server/root_password_again password 'unused'; \  
} | debconf-set-selections \  
&& apt-get update \  
&& apt-get install -y percona-server-server-$PERCONA_MAJOR=$PERCONA_VERSION \  
#&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /etc/apt/sources.list.d/percona.list \  
# purge and re-create /data/mysql with appropriate ownership  
&& rm -rf $MYSQL_DATA_DIR && mkdir -p $MYSQL_DATA_DIR \  
&& chown -R mysql:mysql $MYSQL_DATA_DIR  
  
# 复制mysql配置文件  
COPY mysql/my.cnf /etc/mysql/my.cnf  
COPY mysql/debian.cnf /etc/mysql/debian.cnf  
COPY mysql/mysql /etc/init.d/mysql  
RUN chmod +x /etc/init.d/mysql  
# 安装openresty  
ENV RESTY_VERSION="1.11.2.2" \  
RESTY_LUAROCKS_VERSION="2.3.0" \  
RESTY_OPENSSL_VERSION="1.0.2j" \  
RESTY_PCRE_VERSION="8.39" \  
RESTY_J="1" \  
RESTY_INSTALL_DIR=/opt/app/openresty \  
RESTY_NGINX_DIR=/opt/app/nginx \  
NGINX_CONF_DIR=/etc/nginx \  
NGINX_LOG_DIR=/data/logs/nginx \  
NGINX_PID_PATH=/var/run/nginx.pid  
ENV RESTY_CONFIG_OPTIONS \  
\--with-file-aio \  
\--with-http_addition_module \  
\--with-http_auth_request_module \  
\--with-http_dav_module \  
\--with-http_flv_module \  
\--with-http_geoip_module=dynamic \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_image_filter_module=dynamic \  
\--with-http_mp4_module \  
\--with-http_random_index_module \  
\--with-http_realip_module \  
\--with-http_secure_link_module \  
\--with-http_slice_module \  
\--with-http_ssl_module \  
\--with-http_stub_status_module \  
\--with-http_sub_module \  
\--with-http_v2_module \  
\--with-http_xslt_module=dynamic \  
\--with-ipv6 \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-md5-asm \  
\--with-pcre-jit \  
\--with-sha1-asm \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-threads  
# These are not intended to be user-specified  
ENV _RESTY_CONFIG_DEPS \  
\--prefix=$RESTY_INSTALL_DIR \  
\--sbin-path=$RESTY_NGINX_DIR/sbin/nginx \  
\--conf-path=$NGINX_CONF_DIR/nginx.conf \  
\--http-log-path=$NGINX_LOG_DIR/access.log \  
\--error-log-path=$NGINX_LOG_DIR/error.log \  
\--lock-path=$RESTY_NGINX_DIR/nginx.lock \  
\--pid-path=$NGINX_PID_PATH \  
\--http-client-body-temp-path=$RESTY_NGINX_DIR/temp/body \  
\--http-fastcgi-temp-path=$RESTY_NGINX_DIR/temp/fastcgi \  
\--http-proxy-temp-path=$RESTY_NGINX_DIR/temp/proxy \  
\--with-openssl=/tmp/openssl-${RESTY_OPENSSL_VERSION} \  
\--with-pcre=/tmp/pcre-${RESTY_PCRE_VERSION}  
  
# openresty deps  
ENV RESTY_DEPS \  
build-essential \  
ca-certificates \  
curl \  
libgd-dev \  
libgeoip-dev \  
libncurses5-dev \  
libperl-dev \  
libreadline-dev \  
libxslt1-dev \  
make \  
perl \  
unzip \  
zlib1g-dev  
  
# 临时  
#COPY ustc.sources.list /etc/apt/sources.list  
# nginx 使用web用户运行  
RUN groupadd -r web && useradd -r -g web web  
# 1) Install apt dependencies  
# 2) Download and untar OpenSSL, PCRE, and OpenResty  
# 3) Build OpenResty  
# 4) Cleanup  
RUN \  
DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \--no-install-recommends
$RESTY_DEPS \  
&& cd /tmp \  
&& curl -fSL
https://www.openssl.org/source/openssl-${RESTY_OPENSSL_VERSION}.tar.gz -o
openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
&& tar xzf openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
&& curl -fSL
https://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-${RESTY_PCRE_VERSION}.tar.gz
-o pcre-${RESTY_PCRE_VERSION}.tar.gz \  
&& tar xzf pcre-${RESTY_PCRE_VERSION}.tar.gz \  
&& curl -fSL https://openresty.org/download/openresty-${RESTY_VERSION}.tar.gz
-o openresty-${RESTY_VERSION}.tar.gz \  
&& tar xzf openresty-${RESTY_VERSION}.tar.gz \  
&& cd /tmp/openresty-${RESTY_VERSION} \  
&& ./configure -j${RESTY_J} ${_RESTY_CONFIG_DEPS} ${RESTY_CONFIG_OPTIONS} \  
&& make -j${RESTY_J} \  
&& make -j${RESTY_J} install \  
&& mkdir -p $NGINX_LOG_DIR \  
&& mkdir -p $RESTY_NGINX_DIR/temp \  
&& cd /tmp \  
&& rm -rf \  
openssl-${RESTY_OPENSSL_VERSION} \  
openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
openresty-${RESTY_VERSION}.tar.gz openresty-${RESTY_VERSION} \  
pcre-${RESTY_PCRE_VERSION}.tar.gz pcre-${RESTY_PCRE_VERSION} \  
&& curl -fSL
http://luarocks.org/releases/luarocks-${RESTY_LUAROCKS_VERSION}.tar.gz -o
luarocks-${RESTY_LUAROCKS_VERSION}.tar.gz \  
&& tar xzf luarocks-${RESTY_LUAROCKS_VERSION}.tar.gz \  
&& cd luarocks-${RESTY_LUAROCKS_VERSION} \  
&& ./configure \  
\--prefix=$RESTY_INSTALL_DIR/luajit \  
\--with-lua=$RESTY_INSTALL_DIR/luajit \  
\--lua-suffix=jit-2.1.0-beta2 \  
\--with-lua-include=$RESTY_INSTALL_DIR/luajit/include/luajit-2.1 \  
&& make build \  
&& make install \  
#&& DEBIAN_FRONTEND=noninteractive apt-get purge -y --auto-remove $RESTY_DEPS
\  
#&& rm -rf /var/lib/apt/lists/* \  
&& cd /tmp \  
&& rm -rf luarocks-${RESTY_LUAROCKS_VERSION}
luarocks-${RESTY_LUAROCKS_VERSION}.tar.gz  
#  
COPY nginx/nginx /etc/init.d/nginx  
COPY nginx/upstream.conf ${NGINX_CONF_DIR}/upstream.conf  
COPY nginx/nginx.conf ${NGINX_CONF_DIR}/nginx.conf  
RUN chmod +x /etc/init.d/nginx && ln -sf ${NGINX_CONF_DIR}
$RESTY_NGINX_DIR/conf  
  
# 安装memcached  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r memcache && useradd -r -g memcache memcache  
  
ENV MEMCACHED_VERSION=1.4.36 \  
MEMCACHED_SHA1=519b417515206b0b95ff9bf14106a891f6a2252e \  
MEMCACHED_INSTALL_DIR=/opt/app/memcached  
ENV MEMCACHED_BUILD_DEPS \  
ca-certificates \  
curl \  
dpkg-dev \  
gcc \  
libc6-dev \  
libevent-dev \  
libsasl2-dev \  
make \  
perl  
  
RUN #DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y ${MEMCACHED_BUILD_DEPS}
\--no-install-recommends \  
&& cd /tmp \  
&& rm -rf memcached* \  
&& curl -fSL
"https://memcached.org/files/memcached-${MEMCACHED_VERSION}.tar.gz" -o
memcached.tar.gz \  
&& echo "$MEMCACHED_SHA1 memcached.tar.gz" | sha1sum -c - \  
&& mkdir -p /tmp/memcached \  
&& tar -xzf memcached.tar.gz -C /tmp/memcached \--strip-components=1 \  
&& rm memcached.tar.gz \  
&& cd /tmp/memcached \  
&& ./configure \  
\--prefix=${MEMCACHED_INSTALL_DIR} \  
\--build="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
\--enable-sasl \  
&& make -j "$(nproc)" \  
&& make install \  
&& rm -rf /tmp/memcached \  
&& apt-mark manual \  
libevent-2.0-5 \  
libsasl2-2 \  
&& memcached -V  
  
# 安装 Redis  
ENV REDIS_VERSION=3.2.8 \  
REDIS_INSTALL_DIR=/opt/app/redis  
# redis deps  
ENV REDIS_DEPS \  
ca-certificates \  
curl \  
gcc \  
libc6-dev \  
make  
# 创建 redis 用户  
RUN groupadd -r redis && useradd -r -g redis redis  
# 编译安装 redis  
RUN \  
#DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \--no-install-recommends
$REDIS_DEPS \  
&& cd /tmp \  
&& rm -rf redis* \  
&& curl -fSL http://download.redis.io/releases/redis-${REDIS_VERSION}.tar.gz
-o redis-${REDIS_VERSION}.tar.gz \  
&& tar xzvf redis-${REDIS_VERSION}.tar.gz \  
&& cd redis-${REDIS_VERSION} \  
&& make && make PREFIX=$REDIS_INSTALL_DIR install \  
#&& DEBIAN_FRONTEND=noninteractive apt-get purge -y --auto-remove $REDIS_DEPS
\  
#&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/redis* \  
&& mkdir -p /data/redis \  
&& chown redis:redis -R /data/redis \  
&& mkdir -p /data/logs/redis \  
&& chown redis:redis -R /data/logs/redis  
#  
COPY redis/redis /etc/init.d/redis  
COPY redis/redis.conf /etc/redis.conf  
RUN chmod +x /etc/init.d/redis  
# 安装 gearmand  
ENV GEARMAND_VERSION=1.1.12 \  
GEARMAND_INSTALL_DIR=/opt/app/gearmand \  
GEARMAND_DOWNLOAD_URL=https://launchpad.net/gearmand/1.2/1.1.12/+download/gearmand-1.1.12.tar.gz  
  
# 编译依赖库  
ENV GEARMAND_BUILD_DEPS \  
ca-certificates \  
curl \  
autoconf \  
pkg-config \  
g++ \  
gcc \  
make  
# gearmand deps  
ENV GEARMAND_DEPS \  
libc-dev-bin \  
libstdc++-4.8-dev \  
libboost-thread1.55.0 \  
libboost-thread-dev \  
libboost-system1.55-dev \  
libboost-context1.55-dev \  
libboost-program-options1.55-dev \  
libboost-filesystem1.55-dev \  
libboost-regex1.55-dev \  
libevent-dev \  
uuid-dev \  
gperf \  
libgoogle-perftools-dev  
# 安装依赖  
RUN \  
#DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \--no-install-recommends
$GEARMAND_BUILD_DEPS $GEARMAND_DEPS \  
# 编译安装 gearmand  
&& cd /tmp \  
&& curl -fSL $GEARMAND_DOWNLOAD_URL -o gearmand-${GEARMAND_VERSION}.tar.gz \  
&& tar zxvf gearmand-${GEARMAND_VERSION}.tar.gz && cd
gearmand-${GEARMAND_VERSION} \  
&& ./configure \--prefix=$GEARMAND_INSTALL_DIR \  
\--with-sqlite3=no \--disable-libdrizzle \--disable-libmemcached \  
\--disable-libpq \--with-mysql=no \  
#&& DEBIAN_FRONTEND=noninteractive apt-get purge -y --auto-remove
$GEARMAND_BUILD_DEPS \  
#&& rm -rf /var/lib/apt/lists/* \  
&& make && make install \  
&& rm -rf /tmp/gearmand-${GEARMAND_VERSION}*  
  
# 创建 php 用户  
RUN groupadd -r php && useradd -r -g php php  
  
# PHPIZE 依赖库  
ENV PHPIZE_DEPS \  
autoconf \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pkg-config \  
re2c  
# PHP 依赖库  
ENV PHP_DEPS \  
ca-certificates curl libedit2 libsqlite3-0 xz-utils \  
libgd3 libgd2-xpm-dev libpcre3 libpcre3-dev libcurl3 \  
libreadline-dev libncurses5-dev libxml2 libxml2-dev\  
openssl libcurl4-openssl-dev libssl-dev libmcrypt-dev \  
libfreetype6-dev libbz2-dev zlib1g-dev libicu-dev  
  
# 安装 PHP5.6  
ENV PHP56_VERSION=5.6.28 \  
PHP56_INSTALL_DIR=/opt/app/php56 \  
PHP56_CONF_DIR=/etc/php56 \  
PHP56_LOG_DIR=/data/logs/php56 \  
PHP56_FPM_DIR=/etc/init.d/php-fpm-56  
# 编译安装  
RUN \  
#DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \--no-install-recommends
${PHPIZE_DEPS} ${PHP_DEPS} \  
&& cd /tmp \  
&& curl -fSL
http://jp2.php.net/get/php-${PHP56_VERSION}.tar.xz/from/this/mirror -o
php-${PHP56_VERSION}.tar.xz \  
&& tar xf php-${PHP56_VERSION}.tar.xz && cd php-${PHP56_VERSION} \  
&& ./configure \--prefix=${PHP56_INSTALL_DIR} \  
\--with-config-file-path=${PHP56_CONF_DIR} \  
\--enable-pcntl \--enable-fpm \--enable-gd-native-ttf \  
\--with-freetype-dir \--enable-bcmath \--enable-sysvmsg \  
\--enable-sysvsem \--enable-sysvshm \--enable-soap \  
\--enable-opcache \--enable-mysqlnd \--enable-exif \  
\--enable-sockets \--enable-mbstring \--enable-zip \  
\--disable-ipv6 \--disable-cgi \--with-gd \--with-jpeg-dir \  
\--with-openssl \--with-png-dir \--with-zlib \--with-mhash \  
\--with-curl \--with-mysql=mysqlnd \--with-mysqli=mysqlnd \--with-pdo-
mysql=mysqlnd \  
&& make -j "$(nproc)" && make install \  
&& rm -rf /tmp/php-${PHP56_VERSION}* \  
&& mkdir -p ${PHP56_LOG_DIR} \  
&& chown php:php -R ${PHP56_LOG_DIR} \  
&& mkdir -p ${PHP56_CONF_DIR} \  
&& ln -sf ${PHP56_CONF_DIR} ${PHP56_INSTALL_DIR}/etc  
  
COPY ${ROOT_DIR}/php56/php-fpm-56 ${PHP56_FPM_DIR}  
COPY ${ROOT_DIR}/php56/php-fpm.conf ${PHP56_CONF_DIR}/php-fpm.conf  
COPY ${ROOT_DIR}/php56/php.ini ${PHP56_CONF_DIR}/php.ini  
RUN chmod +x ${PHP56_FPM_DIR}  
  
# 安装 PHP5.5  
ENV PHP55_VERSION=5.5.38 \  
PHP55_INSTALL_DIR=/opt/app/php55 \  
PHP55_CONF_DIR=/etc/php55 \  
PHP55_LOG_DIR=/data/logs/php55 \  
PHP55_FPM_DIR=/etc/init.d/php-fpm-55  
# 编译安装  
RUN \  
#DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \--no-install-recommends
${PHPIZE_DEPS} ${PHP_DEPS} \  
&& cd /tmp \  
&& curl -fSL
http://jp2.php.net/get/php-${PHP55_VERSION}.tar.xz/from/this/mirror -o
php-${PHP55_VERSION}.tar.xz \  
&& tar xf php-${PHP55_VERSION}.tar.xz && cd php-${PHP55_VERSION} \  
&& ./configure \--prefix=${PHP55_INSTALL_DIR} \  
\--with-config-file-path=${PHP55_CONF_DIR} \  
\--enable-pcntl \--enable-fpm \--enable-gd-native-ttf \  
\--with-freetype-dir \--enable-bcmath \--enable-sysvmsg \  
\--enable-sysvsem \--enable-sysvshm \--enable-soap \  
\--enable-opcache \--enable-mysqlnd \--enable-exif \  
\--enable-sockets \--enable-mbstring \--enable-zip \  
\--disable-ipv6 \--disable-cgi \--with-gd \--with-jpeg-dir \  
\--with-openssl \--with-png-dir \--with-zlib \--with-mhash \  
\--with-curl \--with-mysql=mysqlnd \--with-mysqli=mysqlnd \--with-pdo-
mysql=mysqlnd \  
&& make -j "$(nproc)" && make install \  
&& rm -rf /tmp/php-${PHP55_VERSION}* \  
&& mkdir -p ${PHP55_LOG_DIR} \  
&& chown php:php -R ${PHP55_LOG_DIR} \  
&& mkdir -p ${PHP55_CONF_DIR} \  
&& ln -sf ${PHP55_CONF_DIR} ${PHP55_INSTALL_DIR}/etc  
  
COPY ${ROOT_DIR}/php55/php-fpm-55 ${PHP55_FPM_DIR}  
COPY ${ROOT_DIR}/php55/php-fpm.conf ${PHP55_CONF_DIR}/php-fpm.conf  
COPY ${ROOT_DIR}/php55/php.ini ${PHP55_CONF_DIR}/php.ini  
RUN chmod +x ${PHP55_FPM_DIR}  
  
# 安装 PHP5.3  
ENV PHP53_VERSION=5.3.29 \  
PHP53_INSTALL_DIR=/opt/app/php53 \  
PHP53_CONF_DIR=/etc/php53 \  
PHP53_LOG_DIR=/data/logs/php53 \  
PHP53_FPM_DIR=/etc/init.d/php-fpm-53  
# 编译安装  
RUN \  
#DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \--no-install-recommends
${PHPIZE_DEPS} ${PHP_DEPS} \  
&& mkdir /usr/include/freetype2/freetype \  
&& ln -s /usr/include/freetype2/freetype.h
/usr/include/freetype2/freetype/freetype.h \  
&& cd /tmp \  
&& curl -fSL
http://jp2.php.net/get/php-${PHP53_VERSION}.tar.xz/from/this/mirror -o
php-${PHP53_VERSION}.tar.xz \  
&& tar xf php-${PHP53_VERSION}.tar.xz && cd php-${PHP53_VERSION} \  
&& ./configure \--prefix=${PHP53_INSTALL_DIR} \  
\--with-config-file-path=${PHP53_CONF_DIR} \  
\--enable-pcntl \--enable-fpm \--enable-gd-native-ttf \  
\--with-freetype-dir \--enable-bcmath \--enable-sysvmsg \  
\--enable-sysvsem \--enable-sysvshm \--enable-zend-multibyte \  
\--enable-soap \--enable-mysqlnd \--enable-exif \--enable-sockets \  
\--enable-mbstring \--enable-zip \--disable-ipv6 \--disable-cgi \  
\--with-gd \--with-jpeg-dir \--with-png-dir \--with-zlib \  
\--with-mhash \--with-curl \--with-mysql=mysqlnd \  
\--with-mysqli=mysqlnd \--with-pdo-mysql=mysqlnd \  
&& make -j "$(nproc)" && make install \  
&& rm -rf /tmp/php-${PHP53_VERSION}* \  
&& mkdir -p ${PHP53_LOG_DIR} \  
&& chown php:php -R ${PHP53_LOG_DIR} \  
&& mkdir -p ${PHP53_CONF_DIR} \  
&& ln -s ${PHP53_CONF_DIR} ${PHP53_INSTALL_DIR}/etc  
  
COPY ${ROOT_DIR}/php53/php-fpm-53 ${PHP53_FPM_DIR}  
COPY ${ROOT_DIR}/php53/php-fpm.conf ${PHP53_CONF_DIR}/php-fpm.conf  
COPY ${ROOT_DIR}/php53/php.ini ${PHP53_CONF_DIR}/php.ini  
RUN chmod +x ${PHP53_FPM_DIR}  
  
# 安装 PHP gearman 扩展  
ENV PHP_EXT_GEARMAN=gearman-1.1.2  
RUN \  
cd /tmp \  
&& rm -rf ${PHP_EXT_GEARMAN}* \  
&& curl -fSL https://pecl.php.net/get/${PHP_EXT_GEARMAN}.tgz -o
${PHP_EXT_GEARMAN}.tgz \  
# 安装PHP5.6扩展  
&& cd /tmp && tar xzf ${PHP_EXT_GEARMAN}.tgz \  
&& cd ${PHP_EXT_GEARMAN} \  
&& ${PHP56_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-gearman=/opt/app/gearmand \--with-php-
config=${PHP56_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_GEARMAN} \  
# 安装PHP5.5扩展  
&& cd /tmp && tar xzf ${PHP_EXT_GEARMAN}.tgz \  
&& cd ${PHP_EXT_GEARMAN} \  
&& ${PHP55_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-gearman=/opt/app/gearmand \--with-php-
config=${PHP55_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_GEARMAN} \  
# 安装PHP5.3扩展  
&& cd /tmp && tar xzf ${PHP_EXT_GEARMAN}.tgz \  
&& cd ${PHP_EXT_GEARMAN} \  
&& ${PHP53_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-gearman=/opt/app/gearmand \--with-php-
config=${PHP53_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_GEARMAN} \  
# 删除临时文件  
&& rm -rf /tmp/${PHP_EXT_GEARMAN}**  
  
# 安装 PHP memcache 扩展  
ENV PHP_EXT_MEMCACHE=memcache-3.0.8  
RUN \  
cd /tmp \  
&& rm -rf ${PHP_EXT_MEMCACHE}* \  
&& curl -fSL http://pecl.php.net/get/${PHP_EXT_MEMCACHE}.tgz -o
${PHP_EXT_MEMCACHE}.tgz \  
# 安装PHP5.6扩展  
&& cd /tmp && tar xzf ${PHP_EXT_MEMCACHE}.tgz \  
&& cd ${PHP_EXT_MEMCACHE} \  
&& ${PHP56_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-php-config=${PHP56_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_MEMCACHE} \  
# 安装PHP5.5扩展  
&& cd /tmp && tar xzf ${PHP_EXT_MEMCACHE}.tgz \  
&& cd ${PHP_EXT_MEMCACHE} \  
&& ${PHP55_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-php-config=${PHP55_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_MEMCACHE} \  
# 安装PHP5.3扩展  
&& cd /tmp && tar xzf ${PHP_EXT_MEMCACHE}.tgz \  
&& cd ${PHP_EXT_MEMCACHE} \  
&& ${PHP53_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-php-config=${PHP53_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_MEMCACHE} \  
# 删除临时文件  
&& rm -rf /tmp/${PHP_EXT_MEMCACHE}*  
  
# 安装 PHP memcached 扩展  
ENV PHP_EXT_MEMCACHED=memcached-2.2.0  
RUN \  
#DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \--no-install-recommends
libmemcached-dev \  
&& cd /tmp \  
&& rm -rf ${PHP_EXT_MEMCACHED}* \  
&& curl -fSL http://pecl.php.net/get/${PHP_EXT_MEMCACHED}.tgz -o
${PHP_EXT_MEMCACHED}.tgz \  
# 安装PHP5.6扩展  
&& cd /tmp && tar xzf ${PHP_EXT_MEMCACHED}.tgz \  
&& cd ${PHP_EXT_MEMCACHED} \  
&& ${PHP56_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-php-config=${PHP56_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_MEMCACHED} \  
# 安装PHP5.5扩展  
&& cd /tmp && tar xzf ${PHP_EXT_MEMCACHED}.tgz \  
&& cd ${PHP_EXT_MEMCACHED} \  
&& ${PHP55_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-php-config=${PHP55_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_MEMCACHED} \  
# 安装PHP5.3扩展  
&& cd /tmp && tar xzf ${PHP_EXT_MEMCACHED}.tgz \  
&& cd ${PHP_EXT_MEMCACHED} \  
&& ${PHP53_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-php-config=${PHP53_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_MEMCACHED} \  
# 删除临时文件  
&& rm -rf /tmp/${PHP_EXT_MEMCACHED}*  
  
# 安装 PHP msgpack 扩展  
ENV PHP_EXT_MSGPACK=msgpack-0.5.7  
RUN \  
cd /tmp \  
&& rm -rf ${PHP_EXT_MSGPACK}* \  
&& curl -fSL https://pecl.php.net/get/${PHP_EXT_MSGPACK}.tgz -o
${PHP_EXT_MSGPACK}.tgz \  
# 安装PHP5.6扩展  
&& cd /tmp && tar xzf ${PHP_EXT_MSGPACK}.tgz \  
&& cd ${PHP_EXT_MSGPACK} \  
&& ${PHP56_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-php-config=${PHP56_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_MSGPACK} \  
# 安装PHP5.5扩展  
&& cd /tmp && tar xzf ${PHP_EXT_MSGPACK}.tgz \  
&& cd ${PHP_EXT_MSGPACK} \  
&& ${PHP55_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-php-config=${PHP55_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_MSGPACK} \  
# 安装PHP5.3扩展  
&& cd /tmp && tar xzf ${PHP_EXT_MSGPACK}.tgz \  
&& cd ${PHP_EXT_MSGPACK} \  
&& ${PHP53_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-php-config=${PHP53_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_MSGPACK} \  
# 删除临时文件  
&& rm -rf /tmp/${PHP_EXT_MSGPACK}*  
  
# 安装 PHP yar 扩展  
ENV PHP_EXT_YAR=yar-1.2.5  
RUN \  
cd /tmp \  
&& rm -rf ${PHP_EXT_YAR}* \  
&& curl -fSL https://pecl.php.net/get/${PHP_EXT_YAR}.tgz -o ${PHP_EXT_YAR}.tgz
\  
# 安装PHP5.6扩展  
&& cd /tmp && tar xzf ${PHP_EXT_YAR}.tgz \  
&& cd ${PHP_EXT_YAR} \  
&& ${PHP56_INSTALL_DIR}/bin/phpize \  
&& ./configure \--enable-msgpack \--with-php-
config=${PHP56_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_YAR} \  
# 安装PHP5.5扩展  
&& cd /tmp && tar xzf ${PHP_EXT_YAR}.tgz \  
&& cd ${PHP_EXT_YAR} \  
&& ${PHP55_INSTALL_DIR}/bin/phpize \  
&& ./configure \--enable-msgpack \--with-php-
config=${PHP55_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_YAR} \  
# 安装PHP5.3扩展  
&& cd /tmp && tar xzf ${PHP_EXT_YAR}.tgz \  
&& cd ${PHP_EXT_YAR} \  
&& ${PHP53_INSTALL_DIR}/bin/phpize \  
&& ./configure \--enable-msgpack \--with-php-
config=${PHP53_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_YAR} \  
# 删除临时文件  
&& rm -rf /tmp/${PHP_EXT_YAR}*  
  
# 安装 PHP redis 扩展  
ENV PHP_EXT_REDIS=redis-3.1.1  
RUN \  
cd /tmp \  
&& rm -rf ${PHP_EXT_REDIS}* \  
&& curl -fSL https://pecl.php.net/get/${PHP_EXT_REDIS}.tgz -o
${PHP_EXT_REDIS}.tgz \  
# 安装PHP5.6扩展  
&& cd /tmp && tar xzf ${PHP_EXT_REDIS}.tgz \  
&& cd ${PHP_EXT_REDIS} \  
&& ${PHP56_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-php-config=${PHP56_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_REDIS} \  
# 安装PHP5.5扩展  
&& cd /tmp && tar xzf ${PHP_EXT_REDIS}.tgz \  
&& cd ${PHP_EXT_REDIS} \  
&& ${PHP55_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-php-config=${PHP55_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_REDIS} \  
# 安装PHP5.3扩展  
&& cd /tmp && tar xzf ${PHP_EXT_REDIS}.tgz \  
&& cd ${PHP_EXT_REDIS} \  
&& ${PHP53_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-php-config=${PHP53_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_REDIS} \  
# 删除临时文件  
&& rm -rf /tmp/${PHP_EXT_REDIS}*  
  
# 安装 PHP SeasLog 扩展  
ENV PHP_EXT_SEASLOG=SeasLog-1.6.9  
RUN \  
cd /tmp \  
&& rm -rf ${PHP_EXT_SEASLOG}* \  
&& curl -fSL https://pecl.php.net/get/${PHP_EXT_SEASLOG}.tgz -o
${PHP_EXT_SEASLOG}.tgz \  
# 安装PHP5.6扩展  
&& cd /tmp && tar xzf ${PHP_EXT_SEASLOG}.tgz \  
&& cd ${PHP_EXT_SEASLOG} \  
&& ${PHP56_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-php-config=${PHP56_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_SEASLOG} \  
# 安装PHP5.5扩展  
&& cd /tmp && tar xzf ${PHP_EXT_SEASLOG}.tgz \  
&& cd ${PHP_EXT_SEASLOG} \  
&& ${PHP55_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-php-config=${PHP55_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_SEASLOG} \  
# 安装PHP5.3扩展  
&& cd /tmp && tar xzf ${PHP_EXT_SEASLOG}.tgz \  
&& cd ${PHP_EXT_SEASLOG} \  
&& ${PHP53_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-php-config=${PHP53_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_SEASLOG} \  
# 删除临时文件  
&& rm -rf /tmp/${PHP_EXT_SEASLOG}*  
  
# 安装 hiredis,swoole --enable-async-redis 依赖  
ENV HIREDIS_VERSION=0.13.3  
ENV HIREDIS_SRC_DIR=hiredis  
RUN \  
cd /tmp \  
&& rm -rf ${HIREDIS_SRC_DIR}* \  
&& curl -fSL
https://github.com/redis/hiredis/archive/v${HIREDIS_VERSION}.tar.gz -o
${HIREDIS_SRC_DIR}-${HIREDIS_VERSION}.tar.gz \  
&& tar xzf ${HIREDIS_SRC_DIR}-${HIREDIS_VERSION}.tar.gz \  
&& cd ${HIREDIS_SRC_DIR}-${HIREDIS_VERSION} \  
&& make -j && make install && ldconfig  
  
# 安装 PHP swoole 扩展  
ENV PHP_EXT_SWOOLE=swoole-1.9.8  
RUN \  
cd /tmp \  
&& rm -rf ${PHP_EXT_SWOOLE}* \  
&& curl -fSL https://pecl.php.net/get/${PHP_EXT_SWOOLE}.tgz -o
${PHP_EXT_SWOOLE}.tgz \  
# 安装PHP5.6扩展  
&& cd /tmp && tar xzf ${PHP_EXT_SWOOLE}.tgz \  
&& cd ${PHP_EXT_SWOOLE} \  
&& ${PHP56_INSTALL_DIR}/bin/phpize \  
&& ./configure \--enable-async-redis \--enable-async-httpclient \--enable-
sockets \--with-php-config=${PHP56_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_SWOOLE} \  
# 安装PHP5.5扩展  
&& cd /tmp && tar xzf ${PHP_EXT_SWOOLE}.tgz \  
&& cd ${PHP_EXT_SWOOLE} \  
&& ${PHP55_INSTALL_DIR}/bin/phpize \  
&& ./configure \--enable-async-redis \--enable-async-httpclient \--enable-
sockets \--with-php-config=${PHP55_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_SWOOLE} \  
# 安装PHP5.3扩展  
&& cd /tmp && tar xzf ${PHP_EXT_SWOOLE}.tgz \  
&& cd ${PHP_EXT_SWOOLE} \  
&& ${PHP53_INSTALL_DIR}/bin/phpize \  
&& ./configure \--enable-async-redis \--enable-async-httpclient \--enable-
sockets \--with-php-config=${PHP53_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_SWOOLE} \  
# 删除临时文件  
&& rm -rf /tmp/${PHP_EXT_SWOOLE}*  
  
# 安装 PHP yac 扩展  
ENV PHP_EXT_YAC=yac-0.9.2  
RUN \  
cd /tmp \  
&& rm -rf ${PHP_EXT_YAC}* \  
&& curl -fSL https://pecl.php.net/get/${PHP_EXT_YAC}.tgz -o ${PHP_EXT_YAC}.tgz
\  
# 安装PHP5.6扩展  
&& cd /tmp && tar xzf ${PHP_EXT_YAC}.tgz \  
&& cd ${PHP_EXT_YAC} \  
&& ${PHP56_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-php-config=${PHP56_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_YAC} \  
# 安装PHP5.5扩展  
&& cd /tmp && tar xzf ${PHP_EXT_YAC}.tgz \  
&& cd ${PHP_EXT_YAC} \  
&& ${PHP55_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-php-config=${PHP55_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_YAC} \  
# 安装PHP5.3扩展  
&& cd /tmp && tar xzf ${PHP_EXT_YAC}.tgz \  
&& cd ${PHP_EXT_YAC} \  
&& ${PHP53_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-php-config=${PHP53_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_YAC} \  
# 删除临时文件  
&& rm -rf /tmp/${PHP_EXT_YAC}*  
  
# 安装 PHP yaf 扩展  
ENV PHP_EXT_YAF=yaf-2.3.5  
RUN \  
cd /tmp \  
&& rm -rf ${PHP_EXT_YAF}* \  
&& curl -fSL https://pecl.php.net/get/${PHP_EXT_YAF}.tgz -o ${PHP_EXT_YAF}.tgz
\  
# 安装PHP5.6扩展  
&& cd /tmp && tar xzf ${PHP_EXT_YAF}.tgz \  
&& cd ${PHP_EXT_YAF} \  
&& ${PHP56_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-php-config=${PHP56_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_YAF} \  
# 安装PHP5.5扩展  
&& cd /tmp && tar xzf ${PHP_EXT_YAF}.tgz \  
&& cd ${PHP_EXT_YAF} \  
&& ${PHP55_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-php-config=${PHP55_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_YAF} \  
# 安装PHP5.3扩展  
&& cd /tmp && tar xzf ${PHP_EXT_YAF}.tgz \  
&& cd ${PHP_EXT_YAF} \  
&& ${PHP53_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-php-config=${PHP53_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf ${PHP_EXT_YAF} \  
# 删除临时文件  
&& rm -rf /tmp/${PHP_EXT_YAF}*  
  
# 安装 PHP zendopcache 扩展,只有PHP5.3才需要手动安装  
ENV PHP_EXT_ZENDOPCACHE=zendopcache-7.0.5  
RUN \  
cd /tmp \  
&& rm -rf ${PHP_EXT_ZENDOPCACHE}* \  
&& curl -fSL https://pecl.php.net/get/${PHP_EXT_ZENDOPCACHE}.tgz -o
${PHP_EXT_ZENDOPCACHE}.tgz \  
&& tar xzf ${PHP_EXT_ZENDOPCACHE}.tgz \  
&& cd ${PHP_EXT_ZENDOPCACHE} \  
&& ${PHP53_INSTALL_DIR}/bin/phpize \  
&& ./configure \--with-php-config=${PHP53_INSTALL_DIR}/bin/php-config \  
&& make && make install \  
&& rm -rf /tmp/${PHP_EXT_ZENDOPCACHE}*  
  
# 安装 nodejs  
RUN \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \--no-install-recommends
nodejs  
  
  
# 安装 supervisord  
RUN \  
#DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \--no-install-recommends
supervisor \  
&& mkdir -p /data/logs/supervisor  
# 复制supervisor配置文件  
COPY supervisor /etc/supervisor  
COPY supervisor/supervisor /etc/init.d/supervisor  
# 删除无用文件,创建目录  
RUN \  
rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/* \  
&& mkdir /data/webroot \  
&& chown web:web /data/webroot  
  
VOLUME ["/data/webroot", "${NGINX_CONF_DIR}/servers"]  
EXPOSE 80  
  
# 初始化数据库  
COPY mysql/mysql_init.sh /tmp/mysql_init.sh  
RUN \  
chmod +x /tmp/mysql_init.sh \  
&& bash /tmp/mysql_init.sh && rm -rf /tmp/mysql_init.sh  
  
COPY .bashrc /root/.bashrc  
  
CMD ["supervisord","-c","/etc/supervisor/supervisord.conf","-n"]  

