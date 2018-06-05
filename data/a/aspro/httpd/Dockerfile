FROM ubuntu:xenial  
  
ENV HTTPD_VERSION 2.4.27  
ENV APR_VERSIOV 1.6.2  
ENV APR_UTIL_VERSION 1.6.0  
  
ENV MIRROR_URL https://www.apache.org/dyn/closer.cgi?action=download&filename=  
ENV ARCHIVE_URL https://archive.apache.org/dist/  
  
ENV HTTPD_PATH httpd/httpd-$HTTPD_VERSION.tar.bz2  
ENV APR_PATH apr/apr-$APR_VERSIOV.tar.bz2  
ENV APR_UTIL_PATH apr/apr-util-$APR_UTIL_VERSION.tar.bz2  
  
ENV HTTPD_PREFIX /usr/local/apache2  
ENV PATH $HTTPD_PREFIX/bin:$PATH  
  
RUN set -x \  
&& dpkg --add-architecture i386 \  
&& apt-get update \  
&& deps="\  
libexpat1:i386 \  
libpcre++0v5:i386 \  
libnghttp2-14:i386 \  
libssl1.0.0:i386 \  
" \  
&& buildDeps=" \  
gcc-multilib \  
g++-multilib \  
libexpat1-dev:i386 \  
libpcre++-dev:i386 \  
libnghttp2-dev:i386 \  
libssl-dev:i386 \  
make \  
wget \  
ca-certificates \  
bzip2 \  
" \  
&& apt-get install -y --no-install-recommends \  
$deps \  
$buildDeps \  
  
&& cd /tmp \  
  
# downloads httpd  
&& { wget -O httpd.tar.bz2 "${MIRROR_URL}${HTTPD_PATH}" \  
|| wget -O httpd.tar.bz2 "${ARCHIVE_URL}${HTTPD_PATH}" ; } \  
&& { wget -O httpd.tar.bz2.asc "${MIRROR_URL}${HTTPD_PATH}.asc" \  
|| wget -O httpd.tar.bz2.asc "${ARCHIVE_URL}${HTTPD_PATH}.asc" ; } \  
  
# downloads apr  
&& { wget -O apr.tar.bz2 "${MIRROR_URL}${APR_PATH}" \  
|| wget -O apr.tar.bz2 "${ARCHIVE_URL}${APR_PATH}" ; } \  
&& { wget -O apr.tar.bz2.asc "${MIRROR_URL}${APR_PATH}.asc" \  
|| wget -O apr.tar.bz2.asc "${ARCHIVE_URL}${APR_PATH}.asc" ; } \  
  
# downloads apr-util  
&& { wget -O apr-util.tar.bz2 "${MIRROR_URL}${APR_UTIL_PATH}" \  
|| wget -O apr-util.tar.bz2 "${ARCHIVE_URL}${APR_UTIL_PATH}" ; } \  
&& { wget -O apr-util.tar.bz2.asc "${MIRROR_URL}${APR_UTIL_PATH}.asc" \  
|| wget -O apr-util.tar.bz2.asc "${ARCHIVE_URL}${APR_UTIL_PATH}.asc" ; } \  
  
# verify httpd  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
A93D62ECC3C8EA12DB220EC934EA76E6791485A8 \  
&& gpg --verify httpd.tar.bz2.asc httpd.tar.bz2 \  
&& echo 'httpd verified' \  
  
# verify apr  
&& wget -O apr.keys https://people.apache.org/keys/group/apr.asc \  
&& gpg --import apr.keys \  
&& gpg --verify apr.tar.bz2.asc apr.tar.bz2 \  
&& echo 'apr verified' \  
&& gpg --verify apr-util.tar.bz2.asc apr-util.tar.bz2 \  
&& echo 'apr-util verified'\  
  
# extract httpd  
&& mkdir -p /tmp/src \  
&& tar -xvf /tmp/httpd.tar.bz2 -C /tmp/src --strip-components=1 \  
  
# extract apr  
&& mkdir -p /tmp/src/srclib/apr \  
&& tar -xvf /tmp/apr.tar.bz2 -C /tmp/src/srclib/apr --strip-components=1 \  
  
# extract apr-utils  
&& mkdir -p /tmp/src/srclib/apr-util \  
&& tar -xvf /tmp/apr-util.tar.bz2 -C /tmp/src/srclib/apr-util --strip-
components=1 \  
  
&& mkdir -p "$HTTPD_PREFIX" \  
&& chown www-data:www-data "$HTTPD_PREFIX" \  
  
# build httpd  
&& cd /tmp/src \  
&& ./configure \  
\--prefix="$HTTPD_PREFIX" \  
\--enable-mods-shared=reallyall \  
\--enable-http2 \  
\--with-included-apr \  
\--host=i686-linux-gnu "CFLAGS=-m32" "CXXFLAGS=-m32" "LDFLAGS=-m32" \  
&& make -j"$(nproc)" \  
&& make install \  
  
&& sed -ri \  
-e 's!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g' \  
-e 's!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g' \  
"$HTTPD_PREFIX/conf/httpd.conf" \  
  
# clear  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/*  
  
COPY httpd-foreground /usr/local/bin/  
RUN chmod +x /usr/local/bin/httpd-foreground  
  
EXPOSE 80  
CMD ["httpd-foreground"]  

