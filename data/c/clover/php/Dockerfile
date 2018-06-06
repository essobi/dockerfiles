FROM clover/base AS base  
  
RUN groupadd \  
\--gid 50 \  
\--system \  
www \  
&& useradd \  
\--home-dir /var/www \  
\--no-create-home \  
\--system \  
\--shell /bin/false \  
\--uid 50 \  
\--gid 50 \  
www  
  
FROM library/ubuntu:xenial AS build  
  
ENV LANG=C.UTF-8  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y \  
python-software-properties \  
software-properties-common \  
apt-utils  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& add-apt-repository -y ppa:ondrej/php \  
&& add-apt-repository -y ppa:ondrej/pkg-gearman \  
&& apt-get update  
  
RUN mkdir -p /build /rootfs  
WORKDIR /build  
RUN apt-get download \  
firebird2.5-common \  
fontconfig \  
fontconfig-config \  
freetds-common \  
gnupg2 \  
gnupg-agent \  
imagemagick-common \  
libapparmor1 \  
libasn1-8-heimdal \  
libaspell15 \  
libassuan0 \  
libavahi-client3 \  
libavahi-common3 \  
libavahi-common-data \  
libbsd0 \  
libcairo2 \  
libcap-ng0 \  
libc-client2007e \  
libcomerr2 \  
libcurl3 \  
libcurl3-gnutls \  
libdatrie1 \  
libdbi1 \  
libdbus-1-3 \  
libdevmapper1.02.1 \  
libedit2 \  
libenchant1c2a \  
libevent-2.0-5 \  
libexpat1 \  
libfbclient2 \  
libffi6 \  
libfftw3-double3 \  
libfontconfig1 \  
libfreetype6 \  
libgcrypt20 \  
libgd3 \  
libgearman8 \  
libgeoip1 \  
libglib2.0-0 \  
libgmp10 \  
libgnutls30 \  
libgomp1 \  
libgpg-error0 \  
libgpgme11 \  
libgraphicsmagick-q16-3 \  
libgraphite2-3 \  
libgssapi3-heimdal \  
libgssapi-krb5-2 \  
libharfbuzz0b \  
libhcrypto4-heimdal \  
libheimbase1-heimdal \  
libheimntlm0-heimdal \  
libhogweed4 \  
libhunspell-1.3-0 \  
libhx509-5-heimdal \  
libicu55 \  
libidn11 \  
libjasper1 \  
libjbig0 \  
libjpeg8 \  
libjpeg-turbo8 \  
libk5crypto3 \  
libkeyutils1 \  
libkrb5-26-heimdal \  
libkrb5-3 \  
libkrb5support0 \  
libksba8 \  
liblcms2-2 \  
libldap-2.4-2 \  
liblqr-1-0 \  
libltdl7 \  
liblzma5 \  
libmagic1 \  
libmagickcore-6.q16-2 \  
libmagickwand-6.q16-2 \  
libmcrypt4 \  
libmemcached11 \  
libnettle6 \  
libnl-3-200 \  
libnpth0 \  
libnuma1 \  
libodbc1 \  
libp11-kit0 \  
libpango-1.0-0 \  
libpangocairo-1.0-0 \  
libpangoft2-1.0-0 \  
libpgm-5.2-0 \  
libpixman-1-0 \  
libpng12-0 \  
libpq5 \  
libqdbm14 \  
librabbitmq4 \  
librecode0 \  
libroken18-heimdal \  
librrd4 \  
librtmp1 \  
libsasl2-2 \  
libsasl2-modules-db \  
libsodium18 \  
libsqlite3-0 \  
libssh2-1 \  
libssl1.1 \  
libstdc++6 \  
libsybdb5 \  
libsystemd0 \  
libtasn1-6 \  
libthai0 \  
libthai-data \  
libtidy5 \  
libtiff5 \  
libudev1 \  
libuuid1 \  
libvirt0 \  
libwebp6 \  
libwebpmux3 \  
libwind0-heimdal \  
libwmf0.2-7 \  
libx11-6 \  
libx11-data \  
libxau6 \  
libxcb1 \  
libxcb-render0 \  
libxcb-shm0 \  
libxdmcp6 \  
libxen-4.6 \  
libxenstore3.0 \  
libxext6 \  
libxml2 \  
libxmlrpc-epi0 \  
libxpm4 \  
libxrender1 \  
libxslt1.1 \  
libyajl2 \  
libyaml-0-2 \  
libzip5 \  
libzmq5 \  
libnorm1 \  
mlock \  
php-amqp \  
php-apcu \  
php5.6-bcmath \  
php5.6-bz2 \  
php5.6-cli \  
php5.6-common \  
php5.6-curl \  
php5.6-dba \  
php5.6-enchant \  
php5.6-fpm \  
php5.6-gd \  
php-gearman \  
php-geoip \  
php-gettext \  
php-gmagick \  
php5.6-gmp \  
php-gnupg \  
php-http \  
php-igbinary \  
php-imagick \  
php5.6-imap \  
php5.6-interbase \  
php5.6-intl \  
php5.6-json \  
php5.6-ldap \  
php-lua \  
liblua5.2-0 \  
php-sodium \  
php-libvirt-php \  
php-mailparse \  
php5.6-mbstring \  
php5.6-mcrypt \  
php-memcache \  
php-memcached \  
php-mongo \  
php-mongodb \  
php-msgpack \  
php5.6-mysql \  
php-oauth \  
php5.6-odbc \  
php5.6-opcache \  
php-pgsql \  
php-phalcon \  
php-propro \  
php5.6-pspell \  
php-radius \  
php-raphf \  
php5.6-readline \  
php5.6-recode \  
php-redis \  
php-rrd \  
php-sass \  
libsass0 \  
php5.6-soap \  
php-solr \  
php5.6-sqlite \  
php5.6-sqlite3 \  
php-ssh2 \  
php-stomp \  
php5.6-sybase \  
php-tideways \  
php5.6-tidy \  
php-uploadprogress \  
php-uuid \  
php-xcache \  
php-xdebug \  
php-xhprof \  
php5.6-xml \  
php5.6-xmlrpc \  
php5.6-xsl \  
php-yac \  
php-yaml \  
php5.6-zip \  
php-zmq \  
pinentry-curses  
RUN find *.deb | xargs -I % dpkg-deb -x % /rootfs  
  
WORKDIR /rootfs  
  
RUN mkdir -p \  
var/lib/php/sessions \  
var/log \  
var/www \  
run/php \  
etc/php/5.6/fpm \  
etc/php/5.6/cli \  
&& chmod 1777 var/lib/php/sessions \  
&& mv usr/lib/php/5.6/php.ini-production etc/php/5.6/fpm/php.ini \  
&& mv usr/lib/php/5.6/php.ini-production.cli etc/php/5.6/cli/php.ini \  
&& mv usr/share/php5.6-*/*/*.ini etc/php/5.6/mods-available \  
&& rm -rf \  
etc/X11 \  
etc/apache2 \  
etc/freetds \  
etc/fonts/conf.d/README \  
etc/gss \  
etc/init \  
etc/init.d \  
etc/logrotate.d \  
etc/php/5.5 \  
etc/php/7.0 \  
etc/php/7.1 \  
etc/php/7.2 \  
lib/systemd \  
lib/udev \  
usr/include \  
usr/lib/aspell/x86_64-linux-gnu/*.la \  
usr/lib/x86_64-linux-gnu/ImageMagick-6.8.9/modules-Q16/coders/*.la \  
usr/lib/x86_64-linux-gnu/ImageMagick-6.8.9/modules-Q16/filters/*.la \  
usr/lib/odbc \  
usr/lib/tmpfiles.d \  
usr/lib/php/5.6 \  
usr/lib/php/php5.6-fpm-reopenlogs \  
usr/lib/php/20121212 \  
usr/lib/php/20131226/*.la \  
usr/lib/php/20151012 \  
usr/lib/php/20160303 \  
usr/lib/php/20160731 \  
usr/lib/php/20170718 \  
usr/sbin/addgnupghome \  
usr/sbin/applygnupgdefaults \  
usr/share/doc \  
usr/share/gcc-5 \  
usr/share/man \  
usr/share/info \  
usr/share/apport \  
usr/share/bug \  
usr/share/doc-base \  
usr/share/lintian \  
usr/share/upstart \  
usr/share/firebird2.5-common \  
usr/share/gdb \  
usr/share/gnupg2/*.txt \  
usr/share/gnupg2/gpg-conf.skel \  
usr/share/php5.6-* \  
&& ln -s php5.6 usr/bin/php \  
&& ln -s phar5.6 usr/bin/phar \  
&& ln -s phar.phar5.6 usr/bin/phar.phar \  
&& ln -s php-fpm5.6 usr/sbin/php-fpm \  
&& ln -s /dev/stderr var/log/php5.6-fpm.log \  
&& sed -i -r \  
-e 's, *listen *= *.*,listen = 9000,g' \  
-e 's, *user *= *.*,user = www,g' \  
-e 's, *group *= *.*,group = www,g' \  
-e 's, *listen\.owner *= *.*,listen.owner = www,g' \  
-e 's, *listen\.group *= *.*,listen.group = www,g' \  
etc/php/5.6/fpm/pool.d/www.conf \  
&& sed -i -r \  
's,[ ;]*systemd_interval *= *.*,systemd_interval = 0,g' \  
etc/php/5.6/fpm/php-fpm.conf \  
&& sed -i -r \  
-e 's,[ ;]*openssl[.]cafile *= *.*,openssl.cafile = /etc/ssl/certs/ca-certificates.crt,g' \  
-e 's,[ ;]*openssl[.]capath *= *.*,openssl.capath = /usr/share/ca-certificates/mozilla,g' \  
etc/php/5.6/fpm/php.ini \  
&& sed -i -r \  
-e 's,[ ;]*openssl[.]cafile *= *.*,openssl.cafile = /etc/ssl/certs/ca-certificates.crt,g' \  
-e 's,[ ;]*openssl[.]capath *= *.*,openssl.capath = /usr/share/ca-certificates/mozilla,g' \  
etc/php/5.6/cli/php.ini \  
&& for file in etc/php/5.6/mods-available/*.ini; do \  
priority=$(grep -E " *; *priority=" ${file} | sed -r "s/ *; *priority *=
*([0-9]+.*)/\1/g"); \  
if [ -z "${priority}" ]; then priority=20; fi; \  
ln -s "../../mods-available/$(basename ${file})"
etc/php/5.6/cli/conf.d/${priority}-$(basename ${file}); \  
ln -s "../../mods-available/$(basename ${file})"
etc/php/5.6/fpm/conf.d/${priority}-$(basename ${file}); \  
done \  
&& find \  
etc/firebird/2.5/firebird.conf \  
etc/ldap/ldap.conf \  
etc/libnl-3/* \  
etc/magic* \  
usr/share/avahi/service-types \  
| xargs -I % sed -i -r \  
-e 's,^[[:space:]]*[#;]+.*$,,g' \  
-e 's,[[:space:]]+, ,g' \  
-e '/^[[:space:]]*$/d' \  
%  
  
COPY --from=base /etc/group /etc/gshadow /etc/passwd /etc/shadow etc/  
COPY init.sh etc/  
  
WORKDIR /  
  
  
FROM clover/common  
  
ENV LANG=C.UTF-8  
  
COPY --from=build /rootfs /  
  
CMD ["sh", "/etc/init.sh"]  
  
EXPOSE 9000  

