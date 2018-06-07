FROM ubuntu:12.04.5  
# define Docker image label information  
LABEL com.ciandt.vendor="CI&T Software SA" \  
com.ciandt.release-date="2016-11-08" \  
com.ciandt.maintainers.1="Ivan Pinatti - @ivan_pinatti" \  
com.ciandt.maintainers.2="Thomas Bryan - @thobryan"  
# defines root user, to perform privileged operations  
USER root  
  
# enable apt mirrors (best performance due to use the closest repository)  
RUN readonly APT_SOURCES="/etc/apt/sources.list" \  
&& readonly UBUNTU_RELEASE_NAME="$(cat /etc/lsb-release | grep CODENAME | cut
-d '=' -f2)" \  
&& sed \--in-place \  
\--regexp-extended \  
\--expression \  
"1s/^/deb mirror:\/\/mirrors\\.ubuntu\\.com\/mirrors\\.txt
"${UBUNTU_RELEASE_NAME}"-security main restricted universe multiverse\n\n/" \  
\--expression \  
"1s/^/deb mirror:\/\/mirrors\\.ubuntu\\.com\/mirrors\\.txt
"${UBUNTU_RELEASE_NAME}"-backports main restricted universe multiverse\n/" \  
\--expression \  
"1s/^/deb mirror:\/\/mirrors\\.ubuntu\\.com\/mirrors\\.txt
"${UBUNTU_RELEASE_NAME}"-updates main restricted universe multiverse\n/" \  
\--expression \  
"1s/^/deb mirror:\/\/mirrors\\.ubuntu\\.com\/mirrors\\.txt
"${UBUNTU_RELEASE_NAME}" main restricted universe multiverse\n/" \  
\--expression \  
"1s/^/\\# Enable Ubuntu mirrors and multiverse\n/" \  
"${APT_SOURCES}"  
# upgrade Ubuntu packages, install security updates and required packages  
RUN readonly UBUNTU_PACKAGES=" \  
curl \  
" \  
&& apt-get update \  
&& apt-get upgrade \--assume-yes \  
&& apt-get install \--no-install-recommends \  
\--assume-yes \  
${UBUNTU_PACKAGES} \  
# remove apt cache in order to improve Docker image size  
&& apt-get clean  
  
## Apache2  
# environment variables  
ENV APACHE2_MAJOR_VERSION 2.2  
ENV APACHE2_MINOR_VERSION 22  
ENV APACHE2_VERSION ${APACHE2_MAJOR_VERSION}.${APACHE2_MINOR_VERSION}  
  
# declare required packages  
RUN readonly APACHE2_PACKAGES=" \  
apache2=${APACHE2_VERSION}-* \  
apache2-mpm-prefork \  
libapache2-mod-xsendfile \  
libapache2-mod-fcgid \  
libapache2-mod-passenger \  
libapache2-mod-fastcgi \  
ssl-cert \  
" \  
# install packages  
&& apt-get install \  
\--no-install-recommends \  
\--assume-yes \  
${APACHE2_PACKAGES} \  
# remove apt cache in order to improve Docker image size  
&& apt-get clean  
  
# disable modules  
RUN readonly APACHE2_MODULES_TO_DISABLE=" \  
autoindex \  
cgid \  
" \  
&& a2dismod ${APACHE2_MODULES_TO_DISABLE} \  
# enable modules  
&& readonly APACHE2_MODULES_TO_ENABLE=" \  
actions \  
expires \  
fastcgi \  
fcgid \  
headers \  
passenger \  
rewrite \  
ssl \  
suexec \  
vhost_alias \  
xsendfile \  
" \  
&& a2enmod ${APACHE2_MODULES_TO_ENABLE}  
  
# if exists X-Forwarded-Proto in header set HTTPS=on  
RUN echo "SetEnvIf X-Forwarded-Proto https HTTPS=on" > \  
/etc/apache2/conf.d/https-forward-flag.conf  
# tweak conf  
RUN readonly APACHE2_CONF_FILE="/etc/apache2/apache2.conf" \  
# set ServerName - to avoid the warning message "apache2 could not fully
qualified domain name"  
&& echo "ServerName localhost" >> \  
"${APACHE2_CONF_FILE}" \  
# configure log  
&& sed \--in-place \  
\--regexp-extended \  
\--expression \  
's!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g' \  
\--expression \  
's!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g' \  
${APACHE2_CONF_FILE}  
  
# create docroot folder  
RUN mkdir \--parents /var/www/html/docroot  
# create conf file to accept any site  
COPY apache2/any-site \  
/etc/apache2/sites-available/any-site  
# disable default site - enable any-site  
RUN a2dissite default \  
&& a2ensite any-site  
  
# create run foreground script  
COPY apache2/apache2-foreground.sh \  
/usr/local/bin/apache2-foreground  
# start/stop service  
RUN service apache2 start \  
&& service apache2 stop  
  
## PHP 5  
# environment variables  
ENV PHP_MAJOR_VERSION 5.6  
ENV PHP_MINOR_VERSION 24  
ENV PHP_VERSION ${PHP_MAJOR_VERSION}.${PHP_MINOR_VERSION}  
ENV PHP_EXTENSION_GNUPG_VERSION 1.4.0  
ENV PHP_EXTENSION_HTTP_VERSION 2.5.5  
ENV PHP_EXTENSION_IGBINARY_VERSION 1.2.1  
ENV PHP_EXTENSION_IMAGICK_VERSION 3.3.0  
ENV PHP_EXTENSION_MEMCACHE_VERSION 3.0.8  
ENV PHP_EXTENSION_MONGO_VERSION 1.6.12  
ENV PHP_EXTENSION_OAUTH_VERSION 1.2.3  
ENV PHP_EXTENSION_PROPRO_VERSION 1.0.2  
ENV PHP_EXTENSION_RAPHF_VERSION 1.1.2  
ENV PHP_EXTENSION_SSH2_VERSION BETA  
ENV PHP_EXTENSION_UPLOADPROGRESS_VERSION 1.0.3.1  
ENV PHP_EXTENSION_XDEBUG_VERSION 2.4.1  
ENV PHP_EXTENSION_XHPROF_VERSION BETA  
  
# required packages  
RUN readonly PHP_DEV_PACKAGES=" \  
make \  
gcc \  
pkg-config \  
apache2-prefork-dev \  
libxml2-dev \  
libcurl4-openssl-dev \  
libbz2-dev \  
libdb4.8-dev \  
libjpeg-dev \  
libpng12-dev \  
libxpm-dev \  
libfreetype6-dev \  
postgresql-server-dev-9.1 \  
libt1-dev \  
libgd2-xpm-dev \  
libgmp-dev \  
libmysqlclient-dev \  
libsasl2-dev \  
libmhash-dev \  
unixodbc-dev \  
freetds-dev \  
libpspell-dev \  
libsnmp-dev \  
libtidy-dev \  
libmcrypt-dev \  
libc-client-dev \  
libreadline6-dev \  
libssh2-1-dev \  
libgpgme11-dev \  
libmagickwand-dev \  
libxslt1-dev \  
" \  
&& readonly PHP_PACKAGES=" \  
autoconf \  
libbsd0 \  
libedit2 \  
libxml2 \  
libmagic1 \  
ucf \  
sgml-base \  
xml-core \  
libc-client2007e \  
libxslt1.1 \  
libudev0:i386 \  
libdb4.8 \  
libfreetype6 \  
unixodbc \  
libreadline6 \  
libssh2-1 \  
libgpgme11 \  
" \  
&& apt-get install \  
\--no-install-recommends \  
\--assume-yes \  
${PHP_DEV_PACKAGES} \  
${PHP_PACKAGES} \  
# create temp folder  
&& mkdir \--parents /tmp/php/src/${PHP_VERSION} \  
# donwload  
&& cd /tmp/php/src/${PHP_VERSION} \  
&& curl \--silent \  
\--show-error \  
\--location \  
\--output php-${PHP_VERSION}.tar.gz \  
https://php.net/get/php-${PHP_VERSION}.tar.gz/from/this/mirror \  
&& tar \--gunzip \  
\--extract \  
\--file \  
php-${PHP_VERSION}.tar.gz \  
# fix link for required library  
&& ln \--force \  
\--symbolic \  
/usr/lib/libc-client.a \  
/usr/lib/x86_64-linux-gnu/libc-client.a \  
# configure  
&& cd /tmp/php/src/${PHP_VERSION}/php-${PHP_VERSION} \  
&& ./configure \  
\--enable-cli \  
\--with-config-file-path=/usr/local/php${PHP_MAJOR_VERSION}/etc/cli \  
\--with-config-file-scan-dir=/usr/local/php${PHP_MAJOR_VERSION}/etc/cli/conf.d
\  
\--prefix=/usr/local/php${PHP_MAJOR_VERSION} \  
\--enable-bcmath \  
\--with-gmp \  
\--with-bz2=/usr \  
\--enable-calendar \  
\--with-curl \  
\--enable-dba \  
\--with-db4 \  
\--enable-exif \  
\--with-gd \  
\--with-jpeg-dir=/usr/lib \  
\--with-png-dir=/usr/lib \  
\--with-freetype-dir=/usr \  
\--enable-ftp \  
\--with-gettext \  
#--with-imap \  
\--with-kerberos \  
\--with-imap-ssl \  
\--enable-inline-optimization \  
\--with-ldap \  
\--with-ldap-sasl \  
\--with-openssl=/usr \  
\--enable-mbstring \  
\--enable-mbregex \  
\--with-mcrypt \  
\--with-mhash \  
\--with-mssql \  
\--with-mysql \  
\--with-mysql-sock=/var/run/mysqld/mysqld.sock \  
\--with-mysqli=/usr/bin/mysql_config \  
\--enable-pcntl \  
\--with-pcre-regex \  
\--with-pgsql \  
\--with-pdo-mysql \  
\--with-pdo-pgsql \  
\--with-pdo-dblib \  
\--with-pspell=/usr \  
\--with-readline \  
\--enable-shmop \  
\--enable-soap \  
\--enable-sockets \  
\--enable-sysvsem \  
\--enable-sysvshm \  
\--enable-sysvmsg \  
\--with-tidy \  
\--with-t1lib=/usr \  
\--enable-wddx \  
\--enable-xml \  
\--with-xmlrpc \  
\--with-xsl \  
\--with-xpm-dir=/usr \  
\--enable-zip \  
\--with-zlib \  
\--with-libdir=/lib/x86_64-linux-gnu \  
CFLAGS="-g -O2 -fno-omit-frame-pointer" \  
CXXFLAGS=-fno-omit-frame-pointer \  
\--with-apxs2=/usr/bin/apxs2 \  
# compile  
&& make \  
# install  
&& make install \  
# create CLI folder and copy php.ini  
&& mkdir \--parents /usr/local/php${PHP_MAJOR_VERSION}/etc/cli \  
&& readonly PHP_CONF="/usr/local/php${PHP_MAJOR_VERSION}/etc/cli/php.ini" \  
&& cp /tmp/php/src/${PHP_VERSION}/php-${PHP_VERSION}/php.ini-production \  
${PHP_CONF} \  
# set PHP configuration parameters according Aquia environment  
&& sed \--in-place \  
\--regexp-extended \  
\--expression \  
's!^display_errors = .*$!display_errors = STDOUT!g' \  
\--expression \  
's!^enable_dl = .*$!enable_dl = On!g' \  
\--expression \  
's!^expose_php = .*$!expose_php = Off!g' \  
\--expression \  
's!^ignore_repeated_errors = .*$!ignore_repeated_errors = On!g' \  
\--expression \  
's!^mail.add_x_header = .*$!mail.add_x_header = Off!g' \  
\--expression \  
's!^short_open_tag = .*$!short_open_tag = On!g' \  
\--expression \  
's!^memory_limit = .*$!memory_limit = 512M!g' \  
\--expression \  
's!^post_max_size = .*$!post_max_size = 256M!g' \  
\--expression \  
's!^request_order = .*$!request_order = GP!g' \  
\--expression \  
's!^upload_max_filesize = .*$!upload_max_filesize = 256M!g' \  
\--expression \  
's!^variables_order = .*$!variables_order = EGPCS!g' \  
${PHP_CONF} \  
&& echo "realpath_cache_size = 900K" >> "${PHP_CONF}" \  
&& echo "realpath_cache_ttl = 300" >> "${PHP_CONF}" \  
&& echo "sendmail_path = /usr/sbin/sendmail -t -i" >> "${PHP_CONF}" \  
&& echo "error_log = syslog" >> "${PHP_CONF}" \  
&& echo "date.timezone = UTC" >> "${PHP_CONF}" \  
# purge source files  
&& cd / \  
&& rm \--recursive \  
\--force \  
/tmp/php \  
# create link for PHP binary  
&& ln \--force \--symbolic \  
/usr/local/php${PHP_MAJOR_VERSION}/bin/php \  
/usr/local/bin/php \  
# create link for Pecl binary  
&& ln \--force \--symbolic \  
/usr/local/php${PHP_MAJOR_VERSION}/bin/pecl \  
/usr/local/bin/pecl \  
# set PECL in php.ini  
&& pecl config-set \  
php_ini \  
/usr/local/php"${_PHP_MAJOR_VERSION}"/etc/cli/php.ini \  
# install extensions (3rd party) through PECL, configure its ini files and
links  
&& pecl install \  
gnupg-"${PHP_EXTENSION_GNUPG_VERSION}" \  
igbinary-"${PHP_EXTENSION_IGBINARY_VERSION}" \  
imagick-"${PHP_EXTENSION_IMAGICK_VERSION}" \  
memcache-"${PHP_EXTENSION_MEMCACHE_VERSION}" \  
mongo-"${PHP_EXTENSION_MONGO_VERSION}" \  
OAuth-"${PHP_EXTENSION_OAUTH_VERSION}" \  
propro-"${PHP_EXTENSION_PROPRO_VERSION}" \  
raphf-"${PHP_EXTENSION_RAPHF_VERSION}" \  
ssh2-"${PHP_EXTENSION_SSH2_VERSION}" \  
uploadprogress-"${PHP_EXTENSION_UPLOADPROGRESS_VERSION}" \  
xdebug-"${PHP_EXTENSION_XDEBUG_VERSION}" \  
xhprof-"${PHP_EXTENSION_XHPROF_VERSION}" \  
&& echo '' | pecl install pecl_http-"${PHP_EXTENSION_HTTP_VERSION}" \  
&& mkdir \--parents /usr/local/php5.6/etc/conf.d \  
&& cd /usr/local/php5.6/etc/conf.d \  
&& echo "extension=gnupg.so" > gnupg.ini \  
&& echo "extension=http.so" > http.ini \  
&& echo "extension=igbinary.so" > igbinary.ini \  
&& echo "extension=imagick.so" > imagick.ini \  
&& echo "extension=memcache.so" > memcache.ini \  
&& echo "extension=mongo.so" > mongo.ini \  
&& echo "extension=oauth.so" > oauth.ini \  
&& echo "extension=oauth.so" > oauth.ini \  
&& echo "extension=ssh2.so" > ssh2.ini \  
&& echo "extension=uploadprogress.so" > uploadprogress.ini \  
&& echo "extension=xhprof.so" > xhprof.ini \  
&& echo "extension=raphf.so" > raphf.ini \  
&& echo "extension=xdebug.so" > xdebug.ini \  
&& echo "extension=propro.so" > propro.ini \  
&& echo
"zend_extension=/usr/local/php${_PHP_MAJOR_VERSION}/lib/php/extensions/no-
debug-non-zts-20131226/xdebug.so" \  
> ${PHP_CONF} \  
&& mkdir \--parents /usr/local/php${PHP_MAJOR_VERSION}/etc/cli/conf.d \  
&& ln \--force \--symbolic \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/conf.d/gnupg.ini \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/cli/conf.d/gnupg.ini \  
&& ln \--force \--symbolic \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/conf.d/http.ini \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/cli/conf.d/http.ini \  
&& ln \--force \--symbolic \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/conf.d/igbinary.ini \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/cli/conf.d/igbinary.ini \  
&& ln \--force \--symbolic \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/conf.d/imagick.ini \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/cli/conf.d/imagick.ini \  
&& ln \--force \--symbolic \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/conf.d/memcache.ini \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/cli/conf.d/memcache.ini \  
&& ln \--force \--symbolic \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/conf.d/mongo.ini \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/cli/conf.d/mongo.ini \  
&& ln \--force \--symbolic \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/conf.d/oauth.ini \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/cli/conf.d/oauth.ini \  
&& ln \--force \--symbolic \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/conf.d/propro.ini \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/cli/conf.d/propro.ini \  
&& ln \--force \--symbolic \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/conf.d/raphf.ini \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/cli/conf.d/raphf.ini \  
&& ln \--force \--symbolic \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/conf.d/ssh2.ini \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/cli/conf.d/ssh2.ini \  
&& ln \--force \--symbolic \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/conf.d/uploadprogress.ini \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/cli/conf.d/uploadprogress.ini \  
&& ln \--force \--symbolic \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/conf.d/xdebug.ini \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/cli/conf.d/xdebug.ini \  
&& ln \--force \--symbolic \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/conf.d/xhprof.ini \  
/usr/local/php${PHP_MAJOR_VERSION}/etc/cli/conf.d/xhprof.ini \  
# remove DEV packages  
&& apt-get remove \  
\--purge \  
\--assume-yes \  
${PHP_DEV_PACKAGES} \  
# remove apt cache in order to improve Docker image size  
&& apt-get clean  
  
# set PHP cgi script  
COPY php/php-cgi.sh \  
/usr/lib/cgi-bin/php${PHP_MAJOR_VERSION}-cgi  
  
# change placeholder  
RUN sed \--in-place \  
\--regexp-extended \  
\--expression \  
"s/<PHP_MAJOR_VERSION_PLACEHOLDER>/${PHP_MAJOR_VERSION}/g" \  
/usr/lib/cgi-bin/php${PHP_MAJOR_VERSION}-cgi  
  
# configure PHP cgi  
COPY php/php-cgi.conf \  
/etc/apache2/conf.d/php-cgi.conf  
# change placeholder  
RUN sed \--in-place \  
\--regexp-extended \  
\--expression \  
"s/<PHP_MAJOR_VERSION_PLACEHOLDER>/${PHP_MAJOR_VERSION}/g" \  
/etc/apache2/conf.d/php-cgi.conf  
# create a simple test page  
RUN echo '<?php phpinfo(); ?>' > /var/www/test.php  
# create NFS folder in order of mounting files  
RUN mkdir \--parents /nfs  
## DUMB-init  
# more information at: https://github.com/Yelp/dumb-init  
# environment variables  
ENV DUMB_INIT_VERSION 1.2.0  
  
# download  
RUN mkdir \--parents /tmp/dumb-init \  
&& cd /tmp/dumb-init \  
&& curl \--silent \  
\--show-error \  
\--location \  
\--remote-name \  
https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64.deb \  
# install  
&& dpkg \--install dumb-init_${DUMB_INIT_VERSION}_amd64.deb \  
# remove temp folder  
&& cd / \  
&& rm \--force \  
\--recursive \  
/tmp/dumb-init  
## Docker specifics  
# expose HTTP and HTTPS ports  
EXPOSE 80 443  
  
# change workdir to Apache2 folder  
WORKDIR /var/www/html  
# docker entrypoint/cmd configuration  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
CMD ["apache2-foreground"]  
  
## CI&T  
# copy pre-built scripts  
COPY ciandt /root/ciandt  

