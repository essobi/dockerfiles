FROM debian:stretch  
  
ENV COLLECTD_VERSION 5.8.0  
ENV COLLECTD_SHA256
b06ff476bbf05533cb97ae6749262cc3c76c9969f032bd8496690084ddeb15c9  
  
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
librrd8 \  
" \  
&& set -x \  
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
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false $buildDeps \  
&& rm -fr "collectd-${COLLECTD_VERSION}"  
  
CMD ["collectd", "-f"]  

