FROM centos:7  
# persistent / runtime deps  
ENV PHPIZE_DEPS \  
autoconf \  
file \  
gcc \  
gcc-c++ \  
glibc-devel \  
make \  
mingw64-pkg-config \  
re2c  
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN yum install -y http://rpms.famillecollet.com/enterprise/remi-release-7.rpm  
RUN yum update -y  
RUN yum install -y \  
$PHPIZE_DEPS \  
ca-certificates \  
curl \  
libedit \  
sqlite \  
libxml2 \  
&& yum clean all \  
&& rm -rf /var/cache/yum/*  
  
ENV PHP_INI_DIR /etc/php  
RUN mkdir -p $PHP_INI_DIR/conf.d  
  
ENV PHP_EXTRA_BUILD_DEPS ''  
ENV PHP_EXTRA_CONFIGURE_ARGS ''  
ENV GPG_KEYS A917B1ECDA84AEC2B568FED6F50ABC807BD5DCD0  
  
ENV PHP_VERSION 7.1.0  
ENV PHP_FILENAME php-7.1.0.tar.xz  
ENV PHP_SHA256
a810b3f29c21407c24caa88f50649320d20ba6892ae1923132598b8a0ca145b6  
  
RUN set -xe \  
&& buildDeps=" \  
$PHP_EXTRA_BUILD_DEPS \  
curl-devel \  
libedit-devel \  
sqlite-devel \  
openssl-devel \  
libxml2-devel \  
xz \  
" \  
&& yum install -y $buildDeps && rm -rf /var/cache/yum/* \  
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
&& mkdir -p /usr/src/php \  
&& tar -xf "$PHP_FILENAME" -C /usr/src/php --strip-components=1 \  
&& rm "$PHP_FILENAME" \  
&& cd /usr/src/php \  
&& ./configure \  
\--with-config-file-path="$PHP_INI_DIR" \  
\--with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \  
$PHP_EXTRA_CONFIGURE_ARGS \  
\--disable-cgi \  
# --enable-mysqlnd is included here because it's harder to compile after the
fact than extensions are (since it's a plugin for several extensions, not an
extension in itself)  
\--enable-mysqlnd \  
# --enable-mbstring is included here because otherwise there's no way to get
pecl to use it properly (see https://github.com/docker-library/php/issues/195)  
\--enable-mbstring \  
\--with-curl \  
\--with-libedit \  
\--with-openssl \  
\--with-zlib \  
&& make -j"$(nproc)" \  
&& make install \  
&& { find /usr/local/bin /usr/local/sbin -type f -executable -exec strip
--strip-all '{}' \+ || true; } \  
&& make clean \  
&& yum clean all  
  
COPY docker-php-* /usr/local/bin/  
RUN chmod -v +x /usr/local/bin/docker-php-*  
  
CMD ["/sbin/init"]  

