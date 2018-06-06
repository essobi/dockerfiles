FROM alpine:3.6  
ENV TERM=xterm  
  
ENV PROFTPD_VERSION 1.3.6  
ENV UID 5001  
ENV GID 82  
ENV PROFTPD_DEPS \  
g++ \  
gcc \  
libc-dev \  
make \  
libressl-dev \  
gettext \  
sqlite-dev \  
mariadb-dev  
  
RUN set -x \  
&& apk add --no-cache --virtual .persistent-deps \  
ca-certificates \  
curl \  
mariadb-client-libs \  
sqlite-libs \  
&& apk add --no-cache --virtual .build-deps \  
$PROFTPD_DEPS \  
&& curl -fSL
ftp://ftp.proftpd.org/distrib/source/proftpd-${PROFTPD_VERSION}.tar.gz -o
proftpd.tgz \  
&& tar -xf proftpd.tgz \  
&& rm proftpd.tgz \  
&& mkdir -p /usr/local \  
&& mv proftpd-${PROFTPD_VERSION} /usr/local/proftpd  
  
RUN set -x \  
&& sleep 1 \  
&& cd /usr/local/proftpd \  
&& sed -i 's/__mempcpy/mempcpy/g' lib/pr_fnmatch.c \  
&& ./configure \  
\--enable-ctrls --enable-openssl --enable-quotatab --enable-nls \  
\--with-
modules=mod_tls:mod_quotatab:mod_sql:mod_quotatab_sql:mod_quotatab_file:mod_ifsession:mod_ctrls_admin:mod_auth_otp:mod_sql_sqlite:mod_sql_mysql:mod_ban:mod_readme:mod_sftp:mod_sftp_sql
--enable-nls \  
&& make \  
&& cd /usr/local/proftpd && make install \  
&& make clean \  
&& rm -rf /usr/local/proftpd \  
&& apk del .build-deps \  
&& addgroup -Sg 82 www-data 2>/dev/null \  
&& adduser -h /var/www -s /usr/sbin/nologin -H -u 82 -D -G www-data www-data \  
&& rm -rf /var/cache/apk/*  
  
CMD ["/usr/local/sbin/proftpd", "-n", "-c", "/usr/local/etc/proftpd.conf" ]  

