#  
# Dockerfile for shadowsocks-libev-client  
#  
FROM gliderlabs/alpine:3.4  
MAINTAINER Andy Savage <andy@savage.hk>  
  
WORKDIR /  
  
# Change versions here  
ARG SS_VER="latest"  
ARG OBFS_VER="latest"  
# Repo Info  
ARG SS_REPO="shadowsocks/shadowsocks-libev"  
ARG SS_IPSET_REPO="shadowsocks/ipset"  
ARG SS_LIBCORK_REPO="shadowsocks/libcork"  
ARG SS_LIBBLOOM_REPO="shadowsocks/libbloom"  
ARG QRCODE_REPO="fukuchi/libqrencode"  
ARG OBFS_REPO="shadowsocks/simple-obfs"  
ARG DIG_DL_URL="https://github.com/sequenceiq/docker-alpine-
dig/releases/download/v9.10.2/dig.tgz"  
ARG ADD_QRCODE_SUPPORT="yes"  
ARG ADD_OBFS_SUPPORT="yes"  
# Location of config file - Keep to default unless you need to change  
ENV CONFIG_FILE "/config/ss_config.json"  
ENV QRCODE_FILE "/www/qrcode.png"  
ENV VERBOSE_LOGGING "yes"  
ENV SS_MODE "local"  
ENV GENERATE_QRCODE "yes"  
ENV ENABLE_OBFS "yes"  
ENV ADD_QRCODE_SUPPORT ${ADD_QRCODE_SUPPORT}  
ENV ADD_OBFS_SUPPORT ${ADD_OBFS_SUPPORT}  
# This sets the DNS addresses for the server, only applicable in
SS_MODE="server"  
ENV DNS_SERVER_ADDRS "8.8.8.8,8.8.4.4,208.67.222.222,208.67.220.220"  
ENV OBFS_PORT "8443"  
# right now tls or http is supported  
ENV OBFS_TYPE "tls"  
# If OBFS is enabled traffic looks like it is destined for this host  
ENV OBFS_HOST "www.bing.com"  
ENV OBFS_CONFIG_FILE ""  
# This is required if we are running as a server - We don't always know our
own IP  
# if this is not set, we will take our best guess  
ENV QR_SERVER_ADDR ""  
EXPOSE 1080/tcp  
EXPOSE 1080/udp  
EXPOSE 8080/tcp  
EXPOSE 8080/udp  
EXPOSE $OBFS_PORT/tcp  
  
RUN set -ex \  
&& apk add --no-cache bash \  
libcrypto1.0 \  
libev \  
libsodium \  
mbedtls \  
pcre \  
udns \  
jq \  
pwgen \  
&& apk add --no-cache \  
\--virtual TMP autoconf \  
automake \  
build-base \  
curl \  
gettext-dev \  
libpng-dev \  
libev-dev \  
libsodium-dev \  
libtool \  
libpng-dev \  
linux-headers \  
mbedtls-dev \  
openssl-dev \  
pcre-dev \  
tar \  
udns-dev  
  
# Download DIG - Used for QRCode Support when running as a server  
RUN if [ "$ADD_QRCODE_SUPPORT" == "yes" ]; then \  
curl -L "$DIG_DL_URL" | tar -xzv -C "/usr/local/bin/"; \  
fi;  
  
# Download Dependencies  
RUN mkdir -p "/tmp/deps" && cd "/tmp/deps" \  
&& mkdir -p "libipset" \  
&& curl -sSL "https://github.com/$SS_IPSET_REPO/archive/shadowsocks.tar.gz" |
tar xz --strip 1 -C libipset \  
&& mkdir -p "libcork" \  
&& curl -sSL "https://github.com/$SS_LIBCORK_REPO/archive/shadowsocks.tar.gz"
| tar xz --strip 1 -C libcork \  
&& mkdir -p "libbloom" \  
&& curl -sSL "https://github.com/$SS_LIBBLOOM_REPO/archive/master.tar.gz" |
tar xz --strip 1 -C libbloom  
  
RUN SS_VER=$(echo "$SS_VER" | tr -d "\n" | tr -d " " | sed "s/latest//g"); \  
if [ "$SS_VER" == "" ]; then \  
SS_VER=$(curl -s "https://api.github.com/repos/$SS_REPO/releases" | grep
"tag_name" | head -n 1 | tr -d "\"\",v" | cut -f2 -d ":" | tr -d " "); \  
fi; \  
SS_DIR="/tmp/shadowsocks-libev-$SS_VER"; \  
mkdir -p "/tmp" \  
&& cd "/tmp" \  
&& curl -sSL "https://github.com/$SS_REPO/archive/v$SS_VER.tar.gz" | tar xz \  
&& cd "$SS_DIR" \  
&& cp -R /tmp/deps/* "$SS_DIR" \  
&& ./autogen.sh \  
&& ./configure --disable-documentation \  
&& make install  
  
# Add OBFS Support  
RUN if [[ "$ADD_OBFS_SUPPORT" == "yes" ]]; then \  
mkdir -p "/tmp/obfs" && cd "/tmp/obfs" \  
&& curl -L "https://api.github.com/repos/$OBFS_REPO/tarball" | tar xz
--strip=1 \  
&& cp -R /tmp/deps/* "/tmp/obfs" \  
&& ./autogen.sh \  
&& ./configure --disable-documentation \  
&& make && make install; \  
else \  
echo "Skipping OBFS Support"; \  
fi;  
  
# Add QRCode Support  
RUN if [[ "$ADD_QRCODE_SUPPORT" == "yes" ]]; then \  
mkdir -p "/tmp/qrcode" && cd "/tmp/qrcode" \  
&& curl -L "https://api.github.com/repos/$QRCODE_REPO/tarball" | tar xz
--strip=1 \  
&& ./autogen.sh \  
&& ./configure --disable-documentation \  
&& make && make install; \  
else \  
echo "Skipping QRCode Support"; \  
fi;  
  
# Cleanup files  
RUN apk del TMP \  
&& rm -rfv /tmp/*  
  
# Copy files to container  
COPY root/ /  
  
VOLUME ["/config","/www"]  
  
ENTRYPOINT ["/entrypoint.sh"]  

