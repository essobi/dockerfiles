FROM ubuntu:16.04  
  
MAINTAINER DEFENSATIVE Docker Mantainers "docker-maint@defensative.com"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV MAINPACKAGES libpcre3 libdumbnet1 libjson0 libuuid1 libpcap0.8 sqlite3
libcurl3-gnutls \  
curl libmaxminddb0 libesmtp6 libfastjson4 libestr0 libyaml-0-2  
ENV DEVPACKAGES build-essential checkinstall automake autoconf pkg-config
libtool git procps \  
libpcre3-dev libdumbnet-dev libpcap-dev libjson0-dev libcurl4-gnutls-dev \  
dh-autoreconf uuid-dev libsqlite3-dev libmaxminddb-dev libesmtp-dev \  
libjson-c-dev libfastjson-dev libestr-dev libyaml-dev libbsd-dev  
  
COPY docker_update.sh /root/docker_update.sh  
COPY liblognorm5_2.0.3-0adiscon1xenial1ubuntu1_amd64.deb /root/  
COPY liblognorm-dev_2.0.3-0adiscon1xenial1ubuntu1_amd64.deb /root/  
RUN echo deb http://ppa.launchpad.net/maxmind/ppa/ubuntu xenial main >
/etc/apt/sources.list.d/maxmind.list && \  
echo deb http://ppa.launchpad.net/adiscon/v8-stable/ubuntu xenial main >
/etc/apt/sources.list.d/rsyslog.list && \  
apt-get update && \  
cd /usr/local/src && \  
dpkg -i /root/liblognorm5_2.0.3-0adiscon1xenial1ubuntu1_amd64.deb
/root/liblognorm-dev_2.0.3-0adiscon1xenial1ubuntu1_amd64.deb ; \  
apt-mark hold liblognorm5 liblognorm-dev && \  
apt-get install -y --force-yes -f && \  
apt-get install -y --force-yes $MAINPACKAGES && \  
/root/docker_update.sh && \  
apt-get install -y --force-yes $DEVPACKAGES && \  
\  
mkdir -p /usr/share/GeoIP && \  
cd /usr/share/GeoIP && \  
curl -z Geo-Country.mmdb.gz --silent --location -o Geo-Country.mmdb.gz
http://geolite.maxmind.com/download/geoip/database/GeoLite2-Country.mmdb.gz &&
\  
gzip -fqdk /usr/share/GeoIP/Geo-Country.mmdb.gz && \  
\  
cd /usr/local/src && \  
git clone https://github.com/beave/sagan -b master && \  
\  
cd /usr/local/src/sagan && \  
./autogen.sh --disable-libdnet --disable-libpcap --enable-geoip2 --disable-
snortsam --disable-syslog --enable-system-strstr && \  
./configure --disable-libdnet --disable-libpcap --enable-geoip2 --disable-
snortsam --disable-syslog --enable-system-strstr && \  
\  
cd /usr/local/src/sagan && \  
make && \  
make install && \  
cp /usr/local/src/sagan/etc/sagan.yaml /usr/local/etc/sagan.yaml && \  
\  
mkdir -p /var/log/sagan && \  
mkdir -p /var/run/sagan && \  
useradd sagan --shell /sbin/nologin --home / && \  
chown -R nobody:sagan /var/log/sagan && \  
chown -R nobody:sagan /var/run/sagan && \  
\  
apt-get --force-yes remove -y `cat /tmp/remove` && \  
apt-get purge -y man && \  
apt-get clean autoclean && \  
apt-get autoremove -y && \  
(dpkg -l | grep ^rc | awk '{print $2}' | xargs dpkg -P || true) && \  
rm -Rf /tmp/* && \  
rm -Rf /usr/local/src/* -Rf && \  
rm -Rf /var/lib/apt/lists/*.gz && \  
rm -Rf /var/lib/cache/* && \  
rm -Rf /var/lib/log/* && \  
rm -Rf /var/log/* && \  
rm -Rf /var/cache/*  
  
  
  
  
COPY docker/run.sh /root/run.sh  
  
ENTRYPOINT ["/root/run.sh"]  

