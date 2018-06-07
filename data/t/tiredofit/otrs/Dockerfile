FROM tiredofit/alpine:edge  
LABEL maintainer="Dave Conroy (dave at tiredofit dot ca)"  
  
### Set Defaults  
ENV OTRS_VERSION=5.0.23 \  
ZABBIX_HOSTNAME=otrs  
  
### Install packages  
RUN echo http://dl-4.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories && \  
apk update && \  
apk add \  
encodings \  
expat \  
fcgi \  
fcgiwrap \  
fontconfig \  
freetype \  
libbz2 \  
libfontenc \  
libgcrypt \  
libgpg-error \  
libidn \  
libpng \  
libxml2 \  
libxslt \  
mariadb-client \  
mkfontdir \  
mkfontscale \  
nginx \  
perl \  
perl-appconfig \  
perl-archive-zip \  
perl-canary-stability \  
perl-capture-tiny \  
perl-cgi \  
perl-cgi-fast \  
perl-class-mix \  
perl-common-sense \  
perl-convert-asn1 \  
perl-crypt-eksblowfish \  
perl-crypt-ssleay \  
perl-date-format \  
perl-dbd-mysql \  
perl-dbi \  
perl-devel-symdump \  
perl-encode-hanextra \  
perl-encode-locale \  
perl-fcgi \  
perl-file-listing \  
perl-html-parser \  
perl-html-tagset \  
perl-http-cookies \  
perl-http-daemon \  
perl-http-date \  
perl-http-message \  
perl-http-negotiate \  
perl-io-html \  
perl-io-socket-ssl \  
perl-json-xs \  
perl-ldap \  
perl-libwww \  
perl-lwp-mediatypes \  
perl-mail-imapclient \  
perl-net-dns \  
perl-net-http \  
perl-net-libidn \  
perl-net-ssleay \  
perl-params-classify \  
perl-parse-recdescent \  
perl-path-class \  
perl-pod-coverage \  
perl-template-toolkit \  
perl-test-pod \  
perl-text-csv \  
perl-text-csv_xs \  
perl-try-tiny \  
perl-types-serialiser \  
perl-uri \  
perl-www-robotrules \  
perl-xml-libxml \  
perl-xml-libxslt \  
perl-xml-namespacesupport \  
perl-xml-parser \  
perl-xml-sax \  
perl-xml-sax-base \  
perl-yaml-libyaml \  
spawn-fcgi \  
ttf-dejavu \  
&& \  
  
  
### Install OTRS  
mkdir -p /var/lib/otrs && \  
echo "Downloading & Extracting OTRS archive otrs-${OTRS_VERSION}.tar.gz" && \  
curl http://ftp.otrs.org/pub/otrs/otrs-${OTRS_VERSION}.tar.gz |tar -xzf - -C
/var/lib/otrs --strip 1 && \  
  
### Add User  
adduser -D -S -h /var/lib/otrs -s /sbin/nologin -G www-data otrs && \  
### Setup OTRS Directories  
mkdir -p /var/lib/otrs/var/run/ /var/lib/otrs/var/tmp && \  
mkdir -p /run/spawn-fcgi && \  
  
### Set Permissions  
/var/lib/otrs/bin/otrs.SetPermissions.pl --otrs-user=otrs --web-group=www-data
&& \  
  
### Setup Persistence  
mkdir -p /assets/otrs-config && \  
mv /var/lib/otrs/Kernel/ /assets/otrs-config/ && \  
  
### Cleanup  
rm -rf /var/cache/apk/*  
  
### Networking Configuration  
EXPOSE 80  
  
### Files Add  
ADD install /  
  

