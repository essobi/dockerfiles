FROM alpine:3.5  
  
# Избавляемся от геморроя:  
ENV TERM=xterm  
  
# Немного настроек:  
ENV PROFTPD_VERSION 1.3.6rc2  
ENV UID 5001  
ENV GID 82  
  
ENV PROFTPD_DEPS \  
g++ \  
gcc \  
libc-dev \  
make \  
mariadb-dev  
  
# Устанавливаем и подготавливаем pure-ftpd:  
RUN set -x \  
&& apk add --no-cache --virtual .persistent-deps \  
ca-certificates \  
curl \  
mariadb-client-libs \  
&& apk add --no-cache --virtual .build-deps \  
$PROFTPD_DEPS \  
&& curl -fSL
ftp://ftp.proftpd.org/distrib/source/proftpd-${PROFTPD_VERSION}.tar.gz -o
proftpd.tgz \  
&& tar -xf proftpd.tgz \  
&& rm proftpd.tgz \  
&& mkdir -p /usr/local \  
&& mv proftpd-${PROFTPD_VERSION} /usr/local/proftpd \  
&& sleep 1 \  
&& cd /usr/local/proftpd \  
&& sed -i 's/__mempcpy/mempcpy/g' lib/pr_fnmatch.c \  
&& ./configure --with-
modules=mod_sql:mod_sql_mysql:mod_quotatab:mod_quotatab_sql:mod_sftp:mod_sftp_sql
--with-includes=/usr/include/mysql/ \  
&& make \  
&& cd /usr/local/proftpd && make install \  
&& make clean \  
&& rm -rf /usr/local/proftpd \  
&& apk del .build-deps \  
&& addgroup -Sg 82 www-data 2>/dev/null \  
&& adduser -h /var/www -s /usr/sbin/nologin -H -u 82 -D -G www-data www-data \  
&& rm -rf /var/cache/apk/*  
  
CMD ["/usr/local/sbin/proftpd", "-n", "-c", "/usr/local/etc/proftpd.conf" ]

