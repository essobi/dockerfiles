FROM alpine:3.5  
MAINTAINER leafney "babycoolzx@126.com"  
  
ENV SS_LIBEV_VERSION=3.0.5  
ENV SS_DIR=shadowsocks-libev-${SS_LIBEV_VERSION}  
  
RUN set -ex && \  
apk add --no-cache libcrypto1.0 \  
libev \  
libsodium \  
mbedtls \  
pcre \  
udns \  
&& apk add --no-cache --virtual TMP autoconf \  
automake \  
build-base \  
curl \  
gettext-dev \  
libev-dev \  
libsodium-dev \  
libtool \  
linux-headers \  
mbedtls-dev \  
openssl-dev \  
pcre-dev \  
tar \  
udns-dev && \  
cd /tmp && \  
curl -SL -k https://github.com/shadowsocks/shadowsocks-
libev/releases/download/v${SS_LIBEV_VERSION}/shadowsocks-
libev-${SS_LIBEV_VERSION}.tar.gz | tar xz && \  
cd $SS_DIR && \  
./configure --prefix=/usr --disable-documentation && \  
make install && \  
apk del TMP && \  
rm -rf /tmp/* && \  
rm -rf /var/cache/apk/*  
  
COPY ./docker-entrypoint.sh /usr/local/bin/  
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh && \  
chmod +x usr/local/bin/docker-entrypoint.sh  
  
EXPOSE 8388/tcp  
EXPOSE 8388/udp  
  
CMD ["docker-entrypoint.sh"]

