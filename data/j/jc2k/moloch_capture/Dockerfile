FROM ubuntu:16.04 AS builder  
  
ENV GLIB 2.52.3  
ENV YARA 3.6.3  
ENV GEOIP 1.6.11  
ENV PCAP 1.8.1  
ENV CURL 7.55.0  
ENV LUA 5.3.4  
ENV DAQ 2.0.6  
RUN \  
apt-get update && \  
apt-get -y install wget curl libpcre3-dev uuid-dev libmagic-dev pkg-config g++
flex bison zlib1g-dev libffi-dev gettext libgeoip-dev make libjson-perl
libbz2-dev libwww-perl xz-utils libssl-dev libyaml-dev libmount-dev dh-
autoreconf libreadline-dev  
  
RUN mkdir /thirdparty  
  
RUN \  
cd /thirdparty && \  
wget http://ftp.gnome.org/pub/gnome/sources/glib/2.52/glib-$GLIB.tar.xz && \  
xzcat glib-$GLIB.tar.xz | tar xf - && \  
cd glib-$GLIB && \  
./configure --disable-xattr --disable-shared --enable-static --disable-libelf
--disable-selinux && \  
make  
  
RUN \  
cd /thirdparty && \  
wget https://github.com/VirusTotal/yara/archive/v$YARA.tar.gz -O
yara-$YARA.tar.gz && \  
tar zxf yara-$YARA.tar.gz && \  
cd yara-$YARA && \  
./bootstrap.sh && \  
./configure --enable-static && \  
make  
  
RUN \  
cd /thirdparty && \  
wget https://github.com/maxmind/geoip-
api-c/releases/download/v$GEOIP/GeoIP-$GEOIP.tar.gz && \  
tar zxf GeoIP-$GEOIP.tar.gz && \  
cd GeoIP-$GEOIP && \  
./configure --enable-static && \  
make  
  
RUN \  
cd /thirdparty && \  
wget http://www.tcpdump.org/release/libpcap-$PCAP.tar.gz && \  
tar zxf libpcap-$PCAP.tar.gz && \  
cd libpcap-$PCAP && \  
./configure --disable-dbus --disable-usb --disable-canusb --disable-bluetooth
&& \  
make  
  
RUN \  
cd /thirdparty && \  
wget http://curl.haxx.se/download/curl-$CURL.tar.gz && \  
tar zxf curl-$CURL.tar.gz && \  
cd curl-$CURL && \  
./configure --disable-ldap --disable-ldaps --without-libidn --without-librtmp
&& \  
make  
  
RUN \  
cd /thirdparty && \  
wget https://www.lua.org/ftp/lua-$LUA.tar.gz && \  
tar zxf lua-$LUA.tar.gz && \  
cd lua-$LUA && \  
make MYCFLAGS=-fPIC linux  
  
RUN \  
cd /thirdparty && \  
wget https://www.snort.org/downloads/snort/daq-$DAQ.tar.gz && \  
tar zxf daq-$DAQ.tar.gz && \  
cd daq-$DAQ && \  
./configure --with-libpcap-includes=/thirdparty/libpcap-$PCAP/ --with-libpcap-
libraries=/thirdparty/libpcap-$PCAP && \  
make && \  
make install  
  
RUN \  
mkdir -p /app/etc && \  
curl
http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
| gzip -d > /app/etc/GeoIP.dat && \  
curl http://www.maxmind.com/download/geoip/database/asnum/GeoIPASNum.dat.gz |
gzip -d > /app/etc/GeoIPASNum.dat && \  
curl https://www.iana.org/assignments/ipv4-address-space/ipv4-address-
space.csv > /app/etc/ipv4-address-space.csv  
  
RUN \  
mkdir -p /app/bin && \  
curl -L
https://github.com/kelseyhightower/confd/releases/download/v0.13.0/confd-0.13.0-linux-
amd64 -o /app/bin/confd && \  
chmod +x /app/bin/confd  
  
COPY aclocal.m4 compile config.guess config.sub configure configure.ac
install-sh Makefile.am Makefile.in missing /src/  
COPY db /src/db  
COPY capture /src/capture  
COPY tests /src/tests  
COPY viewer /src/viewer  
COPY release /src/release  
  
RUN \  
cd /src && \  
./configure LDFLAGS="-static" \--prefix=/data --with-
libpcap=/thirdparty/libpcap-$PCAP \--with-yara=/thirdparty/yara-$YARA \--with-
GeoIP=/thirdparty/GeoIP-$GEOIP \--with-glib2=/thirdparty/glib-$GLIB \--with-
curl=/thirdparty/curl-$CURL \--with-lua=/thirdparty/lua-$LUA && \  
make  
  
FROM ubuntu:16.04  
RUN \  
apt-get update && \  
apt-get -y install libpcre3 uuid libmagic1 zlib1g libffi6 libgeoip1 libbz2-1.0
libssl1.0.0 libyaml-0-2 libmount1 libreadline5 gosu curl libjson-perl libwww-
perl  
  
RUN mkdir -p /app/var/raw && chown -R nobody: /app/var/raw  
  
COPY \--from=builder /app/etc /app/etc  
COPY \--from=builder /app/bin/confd /app/bin/confd  
COPY \--from=builder /src/capture/moloch-capture /app/bin/moloch-capture  
COPY \--from=builder /src/db /app/db  
COPY \--from=builder /src/capture/plugins/*.so /app/plugins/  
COPY \--from=builder /src/capture/parsers/*.so /app/parsers/  
  
COPY docker/capture/config.ini.toml /app/etc/confd/conf.d/config.ini.toml  
COPY docker/capture/config.ini /app/etc/confd/templates/config.ini  
COPY docker/capture/docker-entrypoint.sh /docker-entrypoint.sh  
  
VOLUME /app/var/raw  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

