FROM debian:stretch-slim  
  
ARG DEBIAN_FRONTEND=noninteractive  
ARG BUILD_CORES  
  
ARG SKALIBS_VER=2.6.4.0  
ARG EXECLINE_VER=2.5.0.0  
ARG S6_VER=2.7.1.1  
ARG RSPAMD_VER=1.7.4  
ARG GUCCI_VER=0.0.4  
ARG
SKALIBS_SHA256_HASH="30ac73f1e8da6387fcfa19cfe1e326a143b4d811aaf532988b280daefa56dcc7"  
ARG
EXECLINE_SHA256_HASH="f6993094766652041c21fde9c07ef53a3cd4b93a64123d9578fb4997a2cefca1"  
ARG
S6_SHA256_HASH="f37547f2890eb50bcb4cd46ffa38bad5ec9e6fd6bc7b73a8df0bdf0cf11f01a9"  
ARG
RSPAMD_SHA256_HASH="0513ebed75b3e4990ae699b868598ae27b27b9e50a20d65dfcca3b1245a1a664"  
ARG
GUCCI_SHA256_HASH="5b2c7cc7589ec760e30881e9bd4d806be0b8ecb71235ced5c190b5aaf88c46ae"  
LABEL description="s6 + rspamd image based on Debian" \  
maintainer="Hardware <contact@meshup.net>" \  
rspamd_version="Rspamd v$RSPAMD_VER built from source" \  
s6_version="s6 v$S6_VER built from source"  
  
ENV LC_ALL=C  
  
RUN NB_CORES=${BUILD_CORES-$(getconf _NPROCESSORS_CONF)} \  
&& BUILD_DEPS=" \  
cmake \  
gcc \  
make \  
ragel \  
wget \  
pkg-config \  
liblua5.1-0-dev \  
libluajit-5.1-dev \  
libglib2.0-dev \  
libevent-dev \  
libsqlite3-dev \  
libicu-dev \  
libssl-dev \  
libmagic-dev" \  
&& apt-get update && apt-get install -y -q --no-install-recommends \  
${BUILD_DEPS} \  
libevent-2.0-5 \  
libglib2.0-0 \  
libssl1.1 \  
libmagic1 \  
liblua5.1-0 \  
libluajit-5.1-2 \  
libsqlite3-0 \  
sqlite3 \  
openssl \  
ca-certificates \  
gnupg \  
dirmngr \  
&& cd /tmp \  
&& SKALIBS_TARBALL="skalibs-${SKALIBS_VER}.tar.gz" \  
&& wget -q https://skarnet.org/software/skalibs/${SKALIBS_TARBALL} \  
&& CHECKSUM=$(sha256sum ${SKALIBS_TARBALL} | awk '{print $1}') \  
&& if [ "${CHECKSUM}" != "${SKALIBS_SHA256_HASH}" ]; then echo
"${SKALIBS_TARBALL} : bad checksum" && exit 1; fi \  
&& tar xzf ${SKALIBS_TARBALL} && cd skalibs-${SKALIBS_VER} \  
&& ./configure --prefix=/usr --datadir=/etc \  
&& make && make install \  
&& cd /tmp \  
&& EXECLINE_TARBALL="execline-${EXECLINE_VER}.tar.gz" \  
&& wget -q https://skarnet.org/software/execline/${EXECLINE_TARBALL} \  
&& CHECKSUM=$(sha256sum ${EXECLINE_TARBALL} | awk '{print $1}') \  
&& if [ "${CHECKSUM}" != "${EXECLINE_SHA256_HASH}" ]; then echo
"${EXECLINE_TARBALL} : bad checksum" && exit 1; fi \  
&& tar xzf ${EXECLINE_TARBALL} && cd execline-${EXECLINE_VER} \  
&& ./configure --prefix=/usr \  
&& make && make install \  
&& cd /tmp \  
&& S6_TARBALL="s6-${S6_VER}.tar.gz" \  
&& wget -q https://skarnet.org/software/s6/${S6_TARBALL} \  
&& CHECKSUM=$(sha256sum ${S6_TARBALL} | awk '{print $1}') \  
&& if [ "${CHECKSUM}" != "${S6_SHA256_HASH}" ]; then echo "${S6_TARBALL} : bad
checksum" && exit 1; fi \  
&& tar xzf ${S6_TARBALL} && cd s6-${S6_VER} \  
&& ./configure --prefix=/usr --bindir=/usr/bin --sbindir=/usr/sbin \  
&& make && make install \  
&& cd /tmp \  
&& RSPAMD_TARBALL="${RSPAMD_VER}.tar.gz" \  
&& wget -q https://github.com/vstakhov/rspamd/archive/${RSPAMD_TARBALL} \  
&& CHECKSUM=$(sha256sum ${RSPAMD_TARBALL} | awk '{print $1}') \  
&& if [ "${CHECKSUM}" != "${RSPAMD_SHA256_HASH}" ]; then echo
"${RSPAMD_TARBALL} : bad checksum" && exit 1; fi \  
&& tar xzf ${RSPAMD_TARBALL} && cd rspamd-${RSPAMD_VER} \  
&& cmake \  
-DCMAKE_INSTALL_PREFIX=/usr \  
-DCONFDIR=/etc/rspamd \  
-DRUNDIR=/run/rspamd \  
-DDBDIR=/var/mail/rspamd \  
-DLOGDIR=/var/log/rspamd \  
-DPLUGINSDIR=/usr/share/rspamd \  
-DLIBDIR=/usr/lib/rspamd \  
-DNO_SHARED=ON \  
-DWANT_SYSTEMD_UNITS=OFF \  
-DENABLE_TORCH=ON \  
-DENABLE_HIREDIS=ON \  
-DINSTALL_WEBUI=ON \  
. \  
&& make -j${NB_CORES} \  
&& make install \  
&& cd /tmp \  
&& GUCCI_BINARY="gucci-v${GUCCI_VER}-linux-amd64" \  
&& wget -q
https://github.com/noqcks/gucci/releases/download/v${GUCCI_VER}/${GUCCI_BINARY}
\  
&& CHECKSUM=$(sha256sum ${GUCCI_BINARY} | awk '{print $1}') \  
&& if [ "${CHECKSUM}" != "${GUCCI_SHA256_HASH}" ]; then echo "${GUCCI_BINARY}
: bad checksum" && exit 1; fi \  
&& chmod +x ${GUCCI_BINARY} \  
&& mv ${GUCCI_BINARY} /usr/local/bin/gucci \  
&& apt-get purge -y ${BUILD_DEPS} \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/lib/apt/lists/* /var/cache/debconf/*-old  

