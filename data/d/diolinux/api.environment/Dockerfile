FROM library/alpine:3.7  
LABEL maintainer="Gerardo Junior <me@gerardo-junior.com>"  
  
# Get installation variables  
ARG HTTPD_VERSION=2.4.33  
ARG
HTTPD_VERSION_SHA256=de02511859b00d17845b9abdd1f975d5ccb5d0b280c567da5bf2ad4b70846f05  
ARG HTTPD_SOURCE_URL=https://www.apache.org/dist/httpd  
  
ARG PHP_VERSION=7.2.5  
ARG
PHP_VERSION_SHA256=af70a33b3f7a51510467199b39af151333fbbe4cc21923bad9c7cf64268cddb2  
ARG PHP_SOURCE_URL=https://secure.php.net/get  
  
ARG PHP_MONGO_VERSION=1.4.3  
ARG
PHP_MONGO_VERSION_SHA256=633485d2dd3f608143d0716f7ebf352a32d94b16eb7947a2bb851b29bad3e912  
ARG PHP_MONGO_SOURCE_URL=https://github.com/mongodb/mongo-php-
driver/releases/download  
  
ARG PHALCON_VERSION=3.3.2  
ARG
PHALCON_VERSION_SHA256=823fd693a7e9e8999edfd405970a81b7bf731fa28109a64774216fc5f68d2975  
ARG PHALCON_SOURCE_URL=https://github.com/phalcon/cphalcon/archive  
  
ARG DEBUG=false  
ARG XDEBUG_VERSION=2.6.0  
ARG
XDEBUG_VERSION_SHA256=b5264cc03bf68fcbb04b97229f96dca505d7b87ec2fb3bd4249896783d29cbdc  
ARG XDEBUG_SOURCE_URL=https://xdebug.org/files  
  
ARG COMPOSER_VERISON=1.6.5  
ARG
COMPOSER_VERISON_SHA256=67bebe9df9866a795078bb2cf21798d8b0214f2e0b2fd81f2e907a8ef0be3434  
ARG COMPOSER_SOURCE_URL=https://github.com/composer/composer/releases/download  
  
  
ENV COMPILE_DEPS .build-deps \  
dpkg-dev dpkg \  
autoconf \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pkgconf \  
re2c \  
lua-dev \  
libxml2-dev \  
lua-dev \  
nghttp2-dev \  
pcre-dev \  
zlib-dev \  
libxml2-dev \  
libressl-dev \  
curl-dev \  
libedit-dev \  
libsodium-dev \  
apr-dev \  
apr-util-dev \  
apr-util-ldap \  
perl \  
tar \  
xz  
  
# Install compile deps  
RUN apk add --no-cache --virtual ${COMPILE_DEPS}  
  
# Install run deps  
RUN apk --update add --virtual .persistent-deps \  
sudo \  
curl \  
libressl  
# Enter in tmp folder  
RUN cd /tmp  
  
# Create project directory  
RUN mkdir -p /usr/share/src  
  
# Create user www-data  
RUN set -xe && \  
addgroup www-data && \  
adduser -G www-data -s /bin/sh -D www-data && \  
echo "www-data ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/default && \  
chown -Rf www-data /usr/share/src  
  
# Compile and install apache  
RUN set -xe && \  
curl -L -o httpd-${HTTPD_VERSION}.tar.bz2
${HTTPD_SOURCE_URL}/httpd-${HTTPD_VERSION}.tar.bz2 && \  
if [ -n "$HTTPD_VERSION_SHA256" ]; then \  
echo "${HTTPD_VERSION_SHA256} httpd-${HTTPD_VERSION}.tar.bz2" | sha256sum -c -
\  
; fi && \  
tar -xf httpd-${HTTPD_VERSION}.tar.bz2 && \  
cd httpd-${HTTPD_VERSION} && \  
sh ./configure --build="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
\--prefix="/usr/local/apache2" \  
\--enable-mods-shared=reallyall \  
\--enable-mpms-shared=all \  
\--enable-so \  
\--enable-ssl \  
\--enable-rewrite \  
\--htmldir="/usr/share/src" && \  
make -j "$(nproc)" && \  
make install && \  
cd ../ && \  
runDeps="$runDeps $( scanelf --needed --nobanner --format '%n#p' --recursive
/usr/local \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' )" && \  
apk add --virtual .httpd-rundeps $runDeps  
  
# Compile and install php  
RUN set -xe && \  
curl -L -o php-${PHP_VERSION}.tar.xz
${PHP_SOURCE_URL}/php-${PHP_VERSION}.tar.xz/from/this/mirror && \  
if [ -n "$PHP_VERSION_SHA256" ]; then \  
echo "${PHP_VERSION_SHA256} php-${PHP_VERSION}.tar.xz" | sha256sum -c - \  
; fi && \  
tar -Jxf php-${PHP_VERSION}.tar.xz && \  
cd php-${PHP_VERSION} && \  
mkdir -p /usr/local/etc/php/conf.d && \  
export CFLAGS="-fstack-protector-strong -fpic -fpie -O2" && \  
export CPPFLAGS=$CFLAGS && \  
export LDFLAGS="-Wl,-O1 -Wl,--hash-style=both -pie" && \  
sh ./configure --build="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
\--with-apxs2="/usr/local/apache2/bin/apxs" \  
\--with-config-file-path="/usr/local/etc/php" \  
\--with-config-file-scan-dir="/usr/local/etc/php/conf.d" \  
\--enable-cgi \  
\--enable-ftp \  
\--enable-mbstring \  
\--with-sodium=shared \  
\--with-curl \  
\--with-libedit \  
\--with-openssl \  
\--with-zlib \  
$(test "$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" = 's390x-linux-gnu'
&& echo '--without-pcre-jit') && \  
make -j "$(nproc)" && \  
make install && \  
find /usr/local/bin /usr/local/sbin -type f -executable -exec strip --strip-
all '{}' \+ || true && \  
make clean && \  
mv php.ini-production /usr/local/etc/php/php.ini && \  
cd .. && \  
runDeps="$( scanelf --needed --nobanner --format '%n#p' --recursive /usr/local
\  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' )" && \  
apk add \--no-cache --virtual .php-rundeps $runDeps && \  
pecl update-channels && \  
rm -rf /tmp/pear ~/.pearrc && \  
unset CFLAGS \  
CPPFLAGS \  
LDFLAGS  
COPY httpd.conf /usr/local/apache2/conf/httpd.conf  
  
# Compile and install mongodb php driver  
RUN set -xe && \  
curl -L -o php-mongodb-${PHP_MONGO_VERSION}.tgz
${PHP_MONGO_SOURCE_URL}/${PHP_MONGO_VERSION}/mongodb-${PHP_MONGO_VERSION}.tgz
&& \  
if [ -n "PHP_MONGO_VERSION_SHA256" ]; then \  
echo "${PHP_MONGO_VERSION_SHA256} php-mongodb-${PHP_MONGO_VERSION}.tgz" |
sha256sum -c - \  
; fi && \  
tar -xzf php-mongodb-${PHP_MONGO_VERSION}.tgz && \  
cd mongodb-${PHP_MONGO_VERSION} && \  
phpize && \  
sh ./configure && \  
make all && \  
make install && \  
cd ../ && \  
echo -e "[mongodb] \n" \  
"extension = $(find /usr/local/lib/php/extensions/ -name mongodb.so)" >
/usr/local/etc/php/conf.d/mongodb.ini  
  
# Compile and install phalcon php extension  
RUN set -xe && \  
curl -L -o phalcon-${PHALCON_VERSION}.tar.gz
${PHALCON_SOURCE_URL}/v${PHALCON_VERSION}.tar.gz && \  
if [ -n "PHALCON_VERSION_SHA256" ]; then \  
echo "${PHALCON_VERSION_SHA256} phalcon-${PHALCON_VERSION}.tar.gz" | sha256sum
-c - \  
; fi && \  
tar -xzf phalcon-${PHALCON_VERSION}.tar.gz && \  
cd ./cphalcon-${PHALCON_VERSION}/build/ && \  
sh ./install --arch safe && \  
cd ../../ && \  
echo -e "[phalcon] \n" \  
"extension = $(find /usr/local/lib/php/extensions/ -name phalcon.so)" >
/usr/local/etc/php/conf.d/phalcon.ini  
  
# Download and install composer  
RUN set -xe && \  
curl -L -o composer-${COMPOSER_VERISON}.phar
${COMPOSER_SOURCE_URL}/${COMPOSER_VERISON}/composer.phar && \  
if [ -n "COMPOSER_VERISON_SHA256" ]; then \  
echo "${COMPOSER_VERISON_SHA256} composer-${COMPOSER_VERISON}.phar" |
sha256sum -c - \  
; fi && \  
mv composer-${COMPOSER_VERISON}.phar /usr/local/bin/composer && \  
chmod +x /usr/local/bin/composer  
  
# Compile, install and configure XDebug php extension  
ARG XDEBUG_CONFIG_HOST=0.0.0.0  
ARG XDEBUG_CONFIG_PORT=9000  
ARG XDEBUG_CONFIG_IDEKEY="IDEA_XDEBUG"  
RUN set -xe && \  
if [[ "$DEBUG" = "true" ]] ; then \  
curl -L -o xdebug-${XDEBUG_VERSION}.tgz
${XDEBUG_SOURCE_URL}/xdebug-${XDEBUG_VERSION}.tgz && \  
if [ -n "XDEBUG_VERSION_SHA256" ]; then \  
echo "${XDEBUG_VERSION_SHA256} xdebug-${XDEBUG_VERSION}.tgz" | sha256sum -c -
\  
; fi && \  
tar -xzf xdebug-${XDEBUG_VERSION}.tgz && \  
cd ./xdebug-${XDEBUG_VERSION} && \  
phpize && \  
sh ./configure --enable-xdebug && \  
make && \  
make install && \  
make clean && \  
cd ../ && \  
echo -e "[XDebug] \n" \  
"zend_extension = $(find /usr/local/lib/php/extensions/ -name xdebug.so) \n" \  
"xdebug.remote_enable = on \n" \  
"xdebug.remote_host = ${XDEBUG_CONFIG_HOST} \n" \  
"xdebug.remote_port = ${XDEBUG_CONFIG_PORT} \n" \  
"xdebug.remote_handler = \"dbgp\" \n" \  
"xdebug.remote_connect_back = off \n" \  
"xdebug.cli_color = on \n" \  
"xdebug.idekey = \"${XDEBUG_CONFIG_IDEKEY}\"" >
/usr/local/etc/php/conf.d/xdebug.ini \  
; fi && \  
unset XDEBUG_CONFIG_HOST \  
XDEBUG_CONFIG_PORT \  
XDEBUG_CONFIG_IDEKEY  
  
# Cleanup system  
RUN set -xe && \  
apk del ${COMPLIE_DEPS} .build-deps && \  
rm -Rf /var/cache/apk/* /tmp/* $HOME/* && \  
unset COMPLIE_DEPS \  
HTTPD_VERSION \  
HTTPD_VERSION_SHA256 \  
HTTPD_SOURCE_URL \  
PHP_VERSION \  
PHP_VERSION_SHA256 \  
PHP_SOURCE_URL \  
PHP_MONGO_VERSION \  
PHP_MONGO_VERSION_SHA256 \  
PHP_MONGO_SOURCE_URL \  
PHALCON_VERSION \  
PHALCON_VERSION_SHA256 \  
PHALCON_SOURCE_URL \  
XDEBUG_VERSION \  
XDEBUG_VERSION_SHA256 \  
XDEBUG_SOURCE_URL \  
COMPOSER_VERISON \  
COMPOSER_VERISON_SHA256 \  
COMPOSER_SOURCE_URL  
  
# Copy scripts  
COPY ./tools/start.sh /usr/local/bin/start.sh  
COPY ./tools/entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh /usr/local/bin/start.sh  
  
# Set project directory  
VOLUME ["/usr/share/src"]  
WORKDIR /usr/share/src  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
USER www-data  
EXPOSE 80 8080

