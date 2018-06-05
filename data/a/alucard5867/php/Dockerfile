FROM alucard5867/centos:centos7  
  
MAINTAINER XJP09_HK <jianping_xie@aliyun.com>  
  
ENV GPG_KEYS 1A4E8B7277C42E53DBA9C7B9BCAA30EA9C0D5763  
  
ENV PHP_VERSION 7.0.8  
ENV PHP_SHA256
0a2142c458b0846f556b16da1c927d74c101aa951bb840549abe5c58584fb394  
  
ENV PHP_DIR /usr/local/php  
ENV PHP_INI_DIR "$PHP_DIR"/etc  
  
ENV PATH $PATH:"$PHP_DIR"/sbin:"$PHP_DIR"/bin  
  
RUN set -xe \  
# Install deps  
&& BUILD_DEPS=" \  
gcc \  
gcc-c++ \  
make \  
file \  
autoconf \  
libxml2-devel \  
libcurl-devel \  
openssl-devel \  
libpng-devel \  
freetype-devel \  
libedit-devel \  
" \  
&& yum install -y $BUILD_DEPS \  
# Install libmcrypt  
&& LIBMCRYPT_VERSION=2.5.8 \  
&& LIBMCRYPT_DIR=/usr/local/libmcrypt \  
&& LIBMCRYPT_FILE="libmcrypt-$LIBMCRYPT_VERSION" \  
&& curl -fSLO
"http://freefr.dl.sourceforge.net/project/mcrypt/Libmcrypt/$LIBMCRYPT_VERSION/$LIBMCRYPT_FILE.tar.gz"
\  
&& tar -xf "$LIBMCRYPT_FILE.tar.gz" \  
&& cd "$LIBMCRYPT_FILE" \  
&& ./configure \  
\--prefix="$LIBMCRYPT_DIR" \  
&& make \  
&& make install \  
&& make clean \  
&& cd .. \  
&& rm -rf "$LIBMCRYPT_FILE" \  
&& rm "$LIBMCRYPT_FILE.tar.gz" \  
# Get php src  
&& PHP_FILENAME=php-"$PHP_VERSION".tar.xz \  
&& PHP_SRC_DIR=/usr/local/src/php \  
&& curl -fSL "http://php.net/get/$PHP_FILENAME/from/this/mirror" -o
"$PHP_FILENAME" \  
&& echo "$PHP_SHA256 *$PHP_FILENAME" | sha256sum -c - \  
&& curl -fSL "http://php.net/get/$PHP_FILENAME.asc/from/this/mirror" -o
"$PHP_FILENAME.asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& for key in $GPG_KEYS; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done \  
&& gpg --batch --verify "$PHP_FILENAME.asc" "$PHP_FILENAME" \  
&& rm -r "$GNUPGHOME" "$PHP_FILENAME.asc" \  
&& mkdir -p $PHP_SRC_DIR \  
&& tar -xf "$PHP_FILENAME" -C $PHP_SRC_DIR --strip-components=1 \  
&& rm "$PHP_FILENAME" \  
# Compile php  
&& cd $PHP_SRC_DIR \  
&& mkdir -p $PHP_INI_DIR/conf.d \  
&& ./configure \  
\--prefix="$PHP_DIR" \  
\--with-config-file-path="$PHP_INI_DIR" \  
\--with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \  
\--enable-fpm \  
\--with-fpm-user="$WWW_USER" \  
\--with-fpm-group="$WWW_GROUP" \  
\--disable-cgi \  
\--enable-mysqlnd \  
\--enable-mbstring \  
\--enable-sockets \  
\--enable-bcmath \  
\--enable-ftp \  
\--enable-zip \  
\--enable-soap \  
\--with-libxml-dir \  
\--with-curl \  
\--with-openssl \  
\--with-mysqli \  
\--with-pdo-mysql \  
\--with-zlib \  
\--with-iconv-dir \  
\--with-mcrypt="$LIBMCRYPT_DIR" \  
\--with-gd \  
\--with-freetype-dir \  
\--with-libedit \  
\--disable-fileinfo \  
&& make -j"$(nproc)" \  
&& make install \  
&& { find "$PHP_DIR"/bin "$PHP_DIR"/sbin -type f -executable -exec strip
--strip-all '{}' \+ || true; } \  
&& make clean \  
# Init php-fpm  
&& cd "$PHP_INI_DIR" \  
# Config php.ini  
&& cp "$PHP_SRC_DIR/php.ini-production" php.ini \  
&& sed -i "/;error_log = syslog/a error_log = $PHP_DIR/var/log/php-error.log"
php.ini \  
&& sed -i "/\\[opcache\\]/a zend_extension = opcache.so" php.ini \  
&& sed -i "/;opcache.enable=0/a opcache.enable = 1" php.ini \  
# Config php-fpm.conf  
&& cp php-fpm.conf.default php-fpm.conf \  
&& sed -i "/;daemonize = yes/a daemonize = no" php-fpm.conf \  
&& cp php-fpm.d/www.conf.default php-fpm.d/www.conf \  
&& rm -rf "$PHP_SRC_DIR" \  
# Install php extension  
&& cd /tmp \  
# ext_xxx=name,version,is_zend  
&& ext_redis="redis,3.0.0,0" \  
&& ext_xdebug="xdebug,2.4.0,1" \  
&& ext_yaf="yaf,3.0.2,0" \  
&& ext_list=("$ext_redis") \  
&& for ext in ${ext_list[*]}; do \  
name=$(echo "${ext[@]}" | awk -F , '{print $1}'); \  
version=$(echo "${ext[@]}" | awk -F , '{print $2}'); \  
is_zend=$(echo "${ext[@]}" | awk -F , '{print $3}'); \  
extfile="$name-$version"; \  
tgzfile="$extfile.tgz"; \  
curl -fSLO "https://pecl.php.net/get/$tgzfile"; \  
mkdir -p "$extfile"; \  
tar -xf "$tgzfile" -C "$extfile" \--strip-components=1; \  
cd "$extfile"; \  
phpize; \  
./configure; \  
make; \  
make install; \  
make clean; \  
cd ..; \  
rm -rf "$extfile"; \  
rm -rf "$tgzfile"; \  
{ \  
echo ; \  
echo "[$name]"; \  
if [ $is_zend = "1" ]; then \  
echo "zend_extension = $name.so"; \  
else \  
echo "extension = $name.so"; \  
fi; \  
echo ; \  
} >> "$PHP_INI_DIR"/php.ini; \  
done \  
# Clean deps  
&& yum remove -y $BUILD_DEPS \  
&& yum clean all  
  
RUN chown "$WWW_USER":"$WWW_GROUP" "$PHP_DIR"/var/log  
  
EXPOSE 9000  
  
CMD ["php-fpm", "-F", "-O"]  

