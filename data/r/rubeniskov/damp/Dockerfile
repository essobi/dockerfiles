FROM debian:jessie  
  
MAINTAINER Rubén López Gómez <me@rubeniskov.com>  
  
ENV MYSQL_MAJOR 5.5  
ENV MYSQL_VERSION 5.5.47  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
  
RUN apt-get update -y \  
&& apt-get install -y perl --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update -y \  
&& apt-get install -y libaio1 pwgen \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
A4A9406876FCBD3C456770C88C718D3B5072E1F5  
  
RUN apt-get update && apt-get install -y curl --no-install-recommends && rm
-rf /var/lib/apt/lists/* \  
&& curl -SL
"http://dev.mysql.com/get/Downloads/MySQL-$MYSQL_MAJOR/mysql-$MYSQL_VERSION-
linux2.6-x86_64.tar.gz" -o mysql.tar.gz \  
&& curl -SL
"http://mysql.he.net/Downloads/MySQL-$MYSQL_MAJOR/mysql-$MYSQL_VERSION-
linux2.6-x86_64.tar.gz.asc" -o mysql.tar.gz.asc \  
&& apt-get purge -y --auto-remove curl \  
&& gpg --verify mysql.tar.gz.asc \  
&& mkdir /usr/local/mysql \  
&& tar -xzf mysql.tar.gz -C /usr/local/mysql --strip-components=1 \  
&& rm mysql.tar.gz* \  
&& rm -rf /usr/local/mysql/mysql-test /usr/local/mysql/sql-bench \  
&& rm -rf /usr/local/mysql/bin/*-debug /usr/local/mysql/bin/*_embedded \  
&& find /usr/local/mysql -type f -name "*.a" -delete \  
&& apt-get update && apt-get install -y binutils && rm -rf
/var/lib/apt/lists/* \  
&& { find /usr/local/mysql -type f -executable -exec strip --strip-all '{}' \+
|| true; } \  
&& apt-get purge -y --auto-remove binutils  
  
ENV PATH $PATH:/usr/local/mysql/bin:/usr/local/mysql/scripts  
  
RUN cp /usr/local/mysql/support-files/mysql.server /etc/init.d/mysql  
  
RUN mkdir -p /etc/mysql/conf.d \  
&& { \  
echo '[mysqld]'; \  
echo 'skip-host-cache'; \  
echo 'skip-name-resolve'; \  
echo 'user = mysql'; \  
echo 'datadir = /var/lib/mysql'; \  
echo '!includedir /etc/mysql/conf.d/'; \  
} > /etc/mysql/my.cnf  
  
ENV PHP_INI_DIR /usr/local/etc/php  
  
RUN apt-get update -y \  
&& apt-get install -y ca-certificates curl librecode0 libsqlite3-0
libcurl4-openssl-dev libxml2-dev --no-install-recommends \  
&& rm -r /var/lib/apt/lists/*  
  
RUN apt-get update -y \  
&& apt-get install -y autoconf file g++ gcc libc-dev make pkg-config re2c
--no-install-recommends \  
&& rm -r /var/lib/apt/lists/*  
  
RUN mkdir -p $PHP_INI_DIR/conf.d  
  
RUN apt-get update -y \  
&& apt-get install -y apache2-bin apache2.2-common --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN rm -rf /var/www/html && mkdir -p /var/lock/apache2 /var/run/apache2
/var/log/apache2 /var/www/html \  
&& chown -R www-data:www-data /var/lock/apache2 /var/run/apache2
/var/log/apache2 /var/www/html  
  
RUN a2dismod mpm_event \  
&& a2enmod mpm_prefork  
  
RUN mv /etc/apache2/apache2.conf /etc/apache2/apache2.conf.dist \  
&& rm /etc/apache2/conf-enabled/* /etc/apache2/sites-enabled/*  
  
ENV PHP_EXTRA_BUILD_DEPS apache2-dev  
  
ENV PHP_EXTRA_CONFIGURE_ARGS --with-apxs2  
  
ENV GPG_KEYS 0B96609E270F565C13292B24C13C70B87267B52D
0BD78B5F97500D450838F95DFE857D9A90D90EC1
F38252826ACD957EF380D39F2F7956BC5DA04B5D  
  
RUN set -xe \  
&& for key in $GPG_KEYS; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV PHP_VERSION 5.5.31  
ENV PHP_FILENAME php-5.5.31.tar.xz  
  
ENV PHP_SHA256
a9ac5b94fcc3811b661a090dddd716f81e43947240b35e6a0123e609a135ac54  
  
RUN buildDeps=" \  
$PHP_EXTRA_BUILD_DEPS \  
libreadline6-dev \  
librecode-dev \  
libsqlite3-dev \  
libssl-dev \  
libidn11-dev \  
xz-utils \  
" \  
&& set -x \  
&& apt-get update && apt-get install -y libcurl4-openssl-dev $buildDeps \--no-
install-recommends && rm -rf /var/lib/apt/lists/* \  
&& curl -fSL "http://php.net/get/$PHP_FILENAME/from/this/mirror" -o
"$PHP_FILENAME" \  
&& echo "$PHP_SHA256 *$PHP_FILENAME" | sha256sum -c - \  
&& curl -fSL "http://php.net/get/$PHP_FILENAME.asc/from/this/mirror" -o
"$PHP_FILENAME.asc" \  
&& gpg --verify "$PHP_FILENAME.asc" \  
&& mkdir -p /usr/src/php \  
&& tar -xf "$PHP_FILENAME" -C /usr/src/php --strip-components=1 \  
&& rm "$PHP_FILENAME"* \  
&& cd /usr/src/php \  
&& ./configure \  
\--with-config-file-path="$PHP_INI_DIR" \  
\--with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \  
$PHP_EXTRA_CONFIGURE_ARGS \  
\--disable-cgi \  
\--enable-mysqlnd \  
\--with-curl \  
\--with-openssl \  
\--with-readline \  
\--with-recode \  
\--with-zlib \  
&& make -j"$(nproc)" \  
&& make install \  
&& { find /usr/local/bin /usr/local/sbin -type f -executable -exec strip
--strip-all '{}' \+ || true; } \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false $buildDeps \  
&& make clean  
  
COPY ./root/ /  
  
RUN chmod -R 775 /etc/init.d/* \  
&& chmod -R 755 /usr/local/damp/scripts/* \  
&& ln -s /usr/local/damp/scripts/* /usr/local/bin/ \  
&& bash /usr/local/damp/docker/setup  
  
EXPOSE 80  
CMD service damp start  

