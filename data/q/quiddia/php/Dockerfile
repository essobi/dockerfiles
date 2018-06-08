FROM quiddia/debian:8.2  
MAINTAINER Radek Antoniuk <radek.antoniuk@quiddia.com>  
  
ENV PHP_VERSION 5.2.17  
ENV FPM_VERSION 0.5.14  
  
RUN buildDeps="gcc make patch git file \  
libxml2-dev libssl-dev libcurl4-openssl-dev libapache2-mod-fcgid libbz2-dev
libjpeg-dev libpng-dev libtidy-dev libc-client2007e-dev \  
libfreetype6-dev libxpm-dev libmcrypt-dev libltdl-dev libmhash-dev
libmysqlclient-dev libreadline-dev libdmalloc-dev libxslt1-dev \  
libldap2-dev libkrb5-dev libpspell-dev"; \  
apt-get update && apt-get install --yes --no-install-recommends --force-yes
${buildDeps}  
  
RUN curl -SL "http://php-fpm.org/downloads/php-$PHP_VERSION-
fpm-${FPM_VERSION}.diff.gz" -o /tmp/php-fpm.diff.gz && \  
git clone https://github.com/warden/php52-backports /tmp/php-src && cd
/tmp/php-src && \  
gzip -d /tmp/php-fpm.diff.gz && patch -p1 < /tmp/php-fpm.diff && \  
ln -s /usr/lib/libc-client.a /usr/lib/x86_64-linux-gnu/ && \  
ln -s /usr/lib/libc-client.so /usr/lib/x86_64-linux-gnu/ && \  
./configure \  
--with-libdir=/lib/x86_64-linux-gnu \  
--with-config-file-path=/etc/php \  
--with-config-file-scan-dir="/etc/php/conf.d" \  
--prefix=/usr \  
--mandir=/usr/share/man \  
--with-fpm-conf="/etc/php/php-fpm.conf" \  
--enable-gd-native-ttf \  
--enable-bcmath \  
--enable-exif \  
--enable-shmop \  
--enable-sysvmsg \  
--enable-inline-optimization \  
--enable-ftp \  
--enable-fastcgi \  
--enable-fpm \  
--enable-force-cgi-redirect \  
--enable-mbstring \  
--enable-pdo \  
--enable-pcntl \  
--enable-soap \  
--enable-sockets \  
--enable-dmalloc \  
--enable-zip \  
--disable-short-tags \  
--disable-ipv6 \  
--with-bz2 \  
--with-curl \  
--with-gd \  
--with-gettext \  
--with-imap \  
--with-imap-ssl \  
--with-kerberos \  
--with-ldap \  
--with-libxml-dir=/usr \  
--with-mhash \  
--with-mysql \  
--with-mysqli \  
--with-openssl=/usr \  
--with-pcre-regex \  
--with-pear=/usr/share/pear \  
--with-png-dir=/usr \  
--with-pdo-mysql \  
--with-pspell \  
--with-readline \  
--with-tidy \  
--with-ttf \  
--with-zlib \  
--with-xpm-dir=/usr \  
--with-xsl && \  
make && make install && \  
apt-get purge -y --auto-remove ${buildDeps} && \  
cp php.ini-recommended /etc/php/ && \  
rm -rf /var/lib/apt/lists/* /tmp/* && \  
mkdir -p /var/www/html /etc/php/conf.d  
  
ADD conf/ /etc/php/  
  
VOLUME /var/www  
WORKDIR /var/www  
  
EXPOSE 9000  
  
CMD ["php-cgi", "--fpm"]  

