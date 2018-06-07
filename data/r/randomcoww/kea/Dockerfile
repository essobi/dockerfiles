## based on haproxy dockerfile  
## https://github.com/docker-library/haproxy/blob/master/1.8/alpine/Dockerfile  
  
FROM alpine:latest  
  
ENV LOG_VERSION REL_1_2_1  
ENV KEA_VERSION kea-1-4-0-beta  
  
RUN set -x \  
\  
&& apk add --no-cache --virtual .build-deps \  
libressl \  
mariadb-dev \  
postgresql-dev \  
boost-dev \  
autoconf \  
make \  
automake \  
libtool \  
g++ \  
\  
## build log4cplus  
&& cd / \  
&& wget -O log4cplus.zip
https://github.com/log4cplus/log4cplus/archive/$LOG_VERSION.zip \  
&& mkdir -p /usr/src \  
&& unzip -d /usr/src log4cplus.zip \  
&& rm log4cplus.zip \  
&& cd /usr/src/log4cplus-$LOG_VERSION \  
\  
&& autoreconf \  
\--install \  
\--force \  
\--warnings=all \  
&& CXXFLAGS='-Os' ./configure \  
\--prefix=/usr/local \  
\--with-working-locale \  
\--enable-static=false \  
&& make -j "$(getconf _NPROCESSORS_ONLN)" \  
&& make install \  
\  
## build kea  
&& cd / \  
&& wget -O kea.tar.gz
https://www.isc.org/downloads/file/$KEA_VERSION/?version=tar-gz \  
&& mkdir -p /usr/src/kea \  
&& tar xf kea.tar.gz --strip-components=1 -C /usr/src/kea \  
&& rm kea.tar.gz \  
&& cd /usr/src/kea \  
\  
&& autoreconf \  
\--install \  
&& CXXFLAGS='-Os' ./configure \  
\--prefix=/usr/local \  
\--sysconfdir=/etc \  
\--localstatedir=/var \  
\--with-log4cplus=/usr/local/lib \  
\--with-dhcp-mysql \  
\--with-dhcp-pgsql \  
\--with-openssl \  
\--enable-static=false \  
&& make -j "$(getconf _NPROCESSORS_ONLN)" \  
&& make install \  
\  
## cleanup  
&& cd / \  
&& rm -rf /usr/src \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive /usr/local \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)" \  
&& apk add --virtual .kea-rundeps $runDeps \  
&& apk del .build-deps  
  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

