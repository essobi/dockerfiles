FROM ubuntu  
MAINTAINER furiousgeorge <furiousgeorgecode@gmail.com>  
  
ENV COLLECTD_VERSION 5.6.1  
ENV COLLECTD_SHA256
c30ff644f91407b4dc2d99787b99cc45ec00e538bd1cc269429d3c5e8a4aee2c  
  
RUN buildDeps=" \  
curl \  
ca-certificates \  
bzip2 \  
build-essential \  
bison \  
flex \  
autotools-dev \  
libltdl-dev \  
pkg-config \  
librrd-dev \  
linux-libc-dev \  
" \  
runDeps=" \  
libltdl7 \  
librrd4 \  
libsnmp-dev \  
snmp-mibs-downloader \  
" \  
&& set -x \  
&& sed -i 's/universe/universe multiverse/' /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps $runDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -fSL "https://collectd.org/files/collectd-${COLLECTD_VERSION}.tar.bz2"
-o "collectd-${COLLECTD_VERSION}.tar.bz2" \  
&& echo "${COLLECTD_SHA256} *collectd-${COLLECTD_VERSION}.tar.bz2" | sha256sum
-c - \  
&& tar -xf "collectd-${COLLECTD_VERSION}.tar.bz2" \  
&& rm "collectd-${COLLECTD_VERSION}.tar.bz2" \  
&& ( \  
cd "collectd-${COLLECTD_VERSION}" \  
&& ./configure \  
\--prefix=/usr/local \  
\--sysconfdir=/etc \  
\--localstatedir=/var \  
\--disable-dependency-tracking \  
\--disable-static \  
&& make -j"$(nproc)" \  
&& make install \  
) \  
&& download-mibs \  
&& apt-get purge -y -o APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false $buildDeps \  
&& rm -fr "collectd-${COLLECTD_VERSION}"  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
CMD ["/entrypoint.sh"]  

