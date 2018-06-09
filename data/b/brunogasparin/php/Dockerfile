FROM debian:jessie  
  
# phpize deps  
RUN apt-get update && apt-get install -y \  
autoconf \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pkg-config \  
re2c \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
# persistent / runtime deps  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
curl \  
libedit2 \  
libsqlite3-0 \  
libxml2 \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
ENV PHP_INI_DIR /usr/local/etc/php  
RUN mkdir -p $PHP_INI_DIR/conf.d  
  
RUN apt-get update && apt-get install -y apache2-bin apache2.2-common --no-
install-recommends && rm -rf /var/lib/apt/lists/*  
  
RUN rm -rf /var/www/html && mkdir -p /var/lock/apache2 /var/run/apache2
/var/log/apache2 /var/www/html && chown -R www-data:www-data /var/lock/apache2
/var/run/apache2 /var/log/apache2 /var/www/html  
  
# Apache + PHP requires preforking Apache for best results  
RUN a2dismod mpm_event && a2enmod mpm_prefork  
  
RUN mv /etc/apache2/apache2.conf /etc/apache2/apache2.conf.dist && rm
/etc/apache2/conf-enabled/* /etc/apache2/sites-enabled/*  
COPY apache2.conf /etc/apache2/apache2.conf  
# it'd be nice if we could not COPY apache2.conf until the end of the
Dockerfile, but its contents are checked by PHP during compilation  
ENV PHP_EXTRA_BUILD_DEPS apache2-dev  
ENV PHP_EXTRA_CONFIGURE_ARGS --with-apxs2  
  
ENV PHP_VERSION 5.3.29  
ENV PHP_FILENAME php-5.3.29.tar.xz  
ENV PHP_MD5 dcff9c881fe436708c141cfc56358075  
  
# @TODO verify public GPG Keys from php release  
# ENV GPG_KEYS 0A95E9A026542D53835E3F3A7DEC4E69FC9C83D7
0B96609E270F565C13292B24C13C70B87267B52D  
# RUN curl -fSL "http://php.net/get/$PHP_FILENAME.asc/from/this/mirror" -o
"$PHP_FILENAME.asc" \  
# && export GNUPGHOME="$(mktemp -d)"  
# && for key in $GPG_KEYS; do \  
# gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
# done \  
# RUN gpg --batch --verify "$PHP_FILENAME.asc" "$PHP_FILENAME"  
# RUN rm -r "$GNUPGHOME" "$PHP_FILENAME.asc" \  
RUN set -xe \  
&& buildDeps=" \  
$PHP_EXTRA_BUILD_DEPS \  
libcurl4-openssl-dev \  
libedit-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
xz-utils \  
" \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
&& curl -fSL "http://php.net/get/$PHP_FILENAME/from/this/mirror" -o
"$PHP_FILENAME" \  
&& echo "$PHP_MD5 *$PHP_FILENAME" | md5sum -c - \  
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
\--with-curl \  
# --with-libedit @todo compile with libedit  
# --with-openssl @todo compile with openssl  
\--with-zlib \  
&& make -j"$(nproc)" \  
&& make install \  
&& { find /usr/local/bin /usr/local/sbin -type f -executable -exec strip
--strip-all '{}' \+ || true; } \  
&& make clean \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false $buildDeps  
  
COPY docker-php-ext-* /usr/local/bin/  
  
COPY apache2-foreground /usr/local/bin/  
WORKDIR /var/www/html  
  
EXPOSE 80  
CMD ["apache2-foreground"]

