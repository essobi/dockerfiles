FROM alpine:edge  
MAINTAINER SgrAlpha <admin@mail.sgr.io>  
  
EXPOSE 8888  
  
RUN set -ex && \  
echo 'http://dl-cdn.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories && \  
apk --update add --no-cache \  
curl \  
privoxy \  
libsodium \  
mbedtls \  
libcrypto1.0 \  
udns \  
pcre \  
libev \  
shadowsocks-libev && \  
mkdir -p /etc/shadowsocks-libev  
  
CMD ss-server -u --fast-open -c /etc/shadowsocks-libev/config.json

