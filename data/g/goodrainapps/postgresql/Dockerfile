FROM goodrainapps/alpine:3.6  
MAINTAINER zhouyq@goodrain.com  
  
  
ENV PACKAGE_DEPS \  
alpine-sdk \  
bison flex \  
coreutils \  
perl perl-utils\  
readline-dev \  
zlib-dev \  
dpkg-dev dpkg \  
openssl-dev \  
libc-dev \  
libedit-dev \  
libxml2-dev \  
libxslt-dev \  
util-linux-dev \  
zlib-dev  
  
ENV PG_VERSION 9.3.17  
ENV PG_SHA256 9c03e5f280cfe9bd202fa01af773eb146abd8ab3065f7279d574c568f6948dbe  
ENV
PG_URL=https://ftp.postgresql.org/pub/source/v${PG_VERSION}/postgresql-${PG_VERSION}.tar.bz2  
  
ENV OSSP_UUID_VERSION 1.6.2  
ENV OSSP_UUID_SHA256
11a615225baa5f8bb686824423f50e4427acd3f70d394765bdff32801f0fd5b0  
  
RUN set -xe \  
&& apk add --no-cache --virtual .build-deps $PACKAGE_DEPS \  
\  
# install OSSP uuid (http://www.ossp.org/pkg/lib/uuid/)  
# see https://github.com/docker-library/postgres/pull/255 for more details  
&& wget -O uuid.tar.gz
"https://www.mirrorservice.org/sites/ftp.ossp.org/pkg/lib/uuid/uuid-$OSSP_UUID_VERSION.tar.gz"
\  
&& echo "$OSSP_UUID_SHA256 *uuid.tar.gz" | sha256sum -c - \  
&& mkdir -p /usr/src/ossp-uuid \  
&& tar \  
\--extract \  
\--file uuid.tar.gz \  
\--directory /usr/src/ossp-uuid \  
\--strip-components 1 \  
&& rm uuid.tar.gz \  
&& ( \  
cd /usr/src/ossp-uuid \  
&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
# explicitly update autoconf config.guess and config.sub so they support more
arches/libcs  
&& wget -O config.guess
'https://git.savannah.gnu.org/cgit/config.git/plain/config.guess?id=7d3d27baf8107b630586c962c057e22149653deb'
\  
&& wget -O config.sub
'https://git.savannah.gnu.org/cgit/config.git/plain/config.sub?id=7d3d27baf8107b630586c962c057e22149653deb'
\  
&& ./configure \  
\--build="$gnuArch" \  
\--prefix=/usr/local \  
&& make -j "$(nproc)" \  
&& make install \  
) \  
&& rm -rf /usr/src/ossp-uuid \  
\  
&& wget -O postgresql.tar.bz2 ${PG_URL} \  
&& echo "$PG_SHA256 *postgresql.tar.bz2" | sha256sum -c - \  
&& mkdir -p /usr/src/postgresql \  
&& tar --strip-components 1 -xjf postgresql.tar.bz2 -C /usr/src/postgresql \  
&& rm postgresql.tar.bz2 \  
&& cd /usr/src/postgresql \  
# update "DEFAULT_PGSOCKET_DIR" to "/var/run/postgresql" (matching Debian)  
# see https://anonscm.debian.org/git/pkg-
postgresql/postgresql.git/tree/debian/patches/51-default-sockets-in-
var.patch?id=8b539fcb3e093a521c095e70bdfa76887217b89f  
&& awk '$1 == "#define" && $2 == "DEFAULT_PGSOCKET_DIR" && $3 == "\"/tmp\"" {
$3 = "\"/var/run/postgresql\""; print; next } { print }'
src/include/pg_config_manual.h > src/include/pg_config_manual.h.new \  
&& grep '/var/run/postgresql' src/include/pg_config_manual.h.new \  
&& mv src/include/pg_config_manual.h.new src/include/pg_config_manual.h \  
&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
# explicitly update autoconf config.guess and config.sub so they support more
arches/libcs  
&& wget -O config/config.guess
'https://git.savannah.gnu.org/cgit/config.git/plain/config.guess?id=7d3d27baf8107b630586c962c057e22149653deb'
\  
&& wget -O config/config.sub
'https://git.savannah.gnu.org/cgit/config.git/plain/config.sub?id=7d3d27baf8107b630586c962c057e22149653deb'
\  
\  
&& ./configure \  
\--build="$gnuArch" \  
\--enable-integer-datetimes \  
\--enable-thread-safety \  
\--disable-rpath \  
\--with-ossp-uuid \  
\--with-gnu-ld \  
\--with-openssl \  
\--with-libxml \  
\--with-libxslt \  
\--with-includes=/usr/local/include \  
\--with-libraries=/usr/local/lib \  
\--prefix=/usr/local \  
&& make -j "$(nproc)" world \  
&& make install-world \  
&& make -C contrib install \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .postgresql-rundeps $runDeps \  
&& cd / \  
&& rm -rf /usr/src/postgresql \  
\  
&& apk del --no-cache .build-deps  
  
RUN mkdir -p /var/run/postgresql && chown -R postgres:postgres
/var/run/postgresql && chmod 2777 /var/run/postgresql  
ENV PGDATA /var/lib/postgresql/data  
ENV LANG en_US.utf8  
VOLUME /var/lib/postgresql/data  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
  
EXPOSE 5432  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["postgres"]  

