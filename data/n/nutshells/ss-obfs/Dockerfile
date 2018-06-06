FROM nutshells/base:centos  
LABEL maintainer="Chao QU <mail@quchao.com>"  
  
ARG SS_VERSION="3.1.1"  
ARG
SS_SHA256="24a002c100fbe9b4481e3134273cb1a2f25a4026eb030760e7e7eb57f8466ef6"  
ARG OBFS_VERSION='0.0.5'  
ARG
OBFS_SHA256='0de9b551b67ec82d0af9d09bcb74c9e8d047f0082ae07db8e4f5f3defeb2ce4c'  
ARG LIBSODIUM_VERSION="1.0.12"  
ARG
LIBSODIUM_SHA256="b8648f1bb3a54b0251cf4ffa4f0d76ded13977d4fa7517d988f4c902dd8e2f95"  
ARG LIBMBEDTLS_VERSION="2.4.2"  
ARG
LIBMBEDTLS_SHA256="b7afab6a0f86e29c6055848b70d183c4e2531cb0ec955b66c0e4e1b7e4954bf4"  
ARG LIBUDNS_VERSION="0.4"  
ARG
LIBUDNS_SHA256="115108dc791a2f9e99e150012bcb459d9095da2dd7d80699b584ac0ac3768710"  
ARG LIBCORK_COMMIT='29d7cba'  
ARG
LIBCORK_SHA256='52be7bddaf4cbcf8635c616b69c1b89e776ad2b19458a3e8c80fc1c30b13f79d'  
ENV WITH_OBFS='true'  
  
WORKDIR /usr/local/src/  
# Dev Tools & Deps  
RUN set -ex; \  
# build & runtime deps  
yum install -y \  
gcc \  
autoconf \  
automake \  
libtool \  
make \  
pcre-devel \  
c-ares-devel \  
libev-devel; \  
# libsodium (v1.0.8+) \  
curl -sSLO
"https://github.com/jedisct1/libsodium/releases/download/${LIBSODIUM_VERSION}/libsodium-${LIBSODIUM_VERSION}.tar.gz";
\  
echo "${LIBSODIUM_SHA256} libsodium-${LIBSODIUM_VERSION}.tar.gz" | sha256sum
-c -; \  
tar xvf "libsodium-${LIBSODIUM_VERSION}.tar.gz"; \  
pushd "libsodium-${LIBSODIUM_VERSION}"; \  
env CFLAGS=-Ofast ./configure --disable-dependency-tracking --prefix=/usr; \  
#make; \  
#make check; \  
make install; \  
#make installcheck; \  
popd; \  
#ldconfig; \  
rm -f "libsodium-${LIBSODIUM_VERSION}.tar.gz"; \  
rm -rf "libsodium-${LIBSODIUM_VERSION}"; \  
# libmbedtls  
curl -sSLO
"https://github.com/ARMmbed/mbedtls/archive/mbedtls-${LIBMBEDTLS_VERSION}.tar.gz";
\  
echo "${LIBMBEDTLS_SHA256} mbedtls-${LIBMBEDTLS_VERSION}.tar.gz" | sha256sum
-c -; \  
tar xvf "mbedtls-${LIBMBEDTLS_VERSION}.tar.gz"; \  
pushd "mbedtls-mbedtls-${LIBMBEDTLS_VERSION}"; \  
make SHARED=1 CFLAGS=-fPIC; \  
make DESTDIR=/usr install; \  
popd; \  
#ldconfig; \  
rm -f "mbedtls-${LIBMBEDTLS_VERSION}.tar.gz"; \  
rm -rf "mbedtls-mbedtls-${LIBMBEDTLS_VERSION}"; \  
# shadowsocks-libev  
curl -sSLO "https://github.com/shadowsocks/shadowsocks-
libev/releases/download/v${SS_VERSION}/shadowsocks-
libev-${SS_VERSION}.tar.gz"; \  
echo "${SS_SHA256} shadowsocks-libev-${SS_VERSION}.tar.gz" | sha256sum -c -; \  
tar xvf "shadowsocks-libev-${SS_VERSION}.tar.gz"; \  
pushd "shadowsocks-libev-${SS_VERSION}"; \  
#autoreconf --install --force; \  
./configure --disable-documentation; \  
make; \  
#make check; \  
#make install; \  
cp src/ss-server src/ss-local /usr/local/bin/; \  
#make installcheck; \  
popd; \  
rm -f "shadowsocks-libev-${SS_VERSION}.tar.gz"; \  
rm -rf "shadowsocks-libev-${SS_VERSION}"; \  
if [ "${WITH_OBFS}" = 'true' ]; then \  
# simple-obfs  
curl -sSLO "https://github.com/shadowsocks/simple-
obfs/archive/v${OBFS_VERSION}.tar.gz"; \  
echo "${OBFS_SHA256} v${OBFS_VERSION}.tar.gz" | sha256sum -c; \  
tar xvf "v${OBFS_VERSION}.tar.gz"; \  
pushd "simple-obfs-${OBFS_VERSION}"; \  
# libcork  
curl -sSLO
"https://github.com/shadowsocks/libcork/archive/${LIBCORK_COMMIT}.tar.gz"; \  
echo "${LIBCORK_SHA256} ${LIBCORK_COMMIT}.tar.gz" | sha256sum -c; \  
tar xvf "${LIBCORK_COMMIT}.tar.gz"; \  
rm -rf libcork; \  
mv libcork-* libcork; \  
./autogen.sh; \  
./configure --disable-documentation; \  
make; \  
#make check; \  
#make install; \  
cp src/obfs-server src/obfs-local /usr/local/bin/; \  
#make installcheck; \  
popd; \  
rm -f "v${OBFS_VERSION}.tar.gz"; \  
rm -rf "simple-obfs-${OBFS_VERSION}"; \  
fi; \  
# do some cleanup  
yum remove -y \  
gcc \  
autoconf \  
automake \  
libtool \  
make; \  
yum clean all; \  
rm -rf /tmp/* /var/tmp/* /usr/local/src/*;  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
RUN set -ex; \  
# Use GoSU instead  
sed -i 's/su-exec/gosu/' /usr/local/bin/docker-entrypoint.sh; \  
chmod +x /usr/local/bin/docker-entrypoint.sh; \  
chown "${RUN_AS_USER}":"${RUN_AS_USER}" /usr/local/bin/ss-*; \  
chown "${RUN_AS_USER}":"${RUN_AS_USER}" /usr/local/bin/obfs-*;  
  
ENV LISTEN_PORT='12345' \  
SERVER_ADDRESS='' \  
SERVER_PORT='' \  
PASSWORD='' \  
KEY_IN_BASE64='' \  
ENCRYPT_METHOD='xchacha20-ietf-poly1305' \  
TCP_RELAY='true' \  
UDP_RELAY='true' \  
REUSE_PORT='true' \  
TCP_FAST_OPEN='true' \  
OBFS_PLUGIN='http' \  
OBFS_HOST='bing.com'  
#HEALTHCHECK --interval=1m --timeout=3s \  
# CMD [[ "$(curl -f http://localhost:"${LISTEN_PORT}" 2>&1 | grep 'curl: (52)'
| wc -l)" -eq 1 ]] || exit 1  
  
EXPOSE ${LISTEN_PORT}/tcp ${LISTEN_PORT}/udp  
  
WORKDIR /usr/local/var/ss-obfs  
ENTRYPOINT [ "docker-entrypoint.sh" ]  

