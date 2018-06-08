FROM alpine:3.4  
MAINTAINER wengcan <wengcanvip@gmail.com>  
  
ENV DEPENDENCIES curl build-base gcc automake autoconf c-ares-dev libev-dev
libsodium-dev linux-headers mbedtls-dev pcre-dev libtool openssl-dev udns-dev  
ENV VERSION 3.1.3  
RUN apk add --update --no-cache --virtual .build-deps $DEPENDENCIES  
RUN curl -L -O https://github.com/shadowsocks/shadowsocks-
libev/releases/download/v$VERSION/shadowsocks-libev-$VERSION.tar.gz \  
&& tar zxvf shadowsocks-libev-$VERSION.tar.gz \  
&& cd shadowsocks-libev-$VERSION \  
&& ./configure --disable-documentation\  
&& make \  
&& make install \  
&& cd ../ \  
&& rm -rf shadowsocks-libev-$VERSION.tar.gz shadowsocks-libev-$VERSION \  
&& apk add --no-cache libcrypto1.0 pcre libev libsodium mbedtls c-ares\  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/*  
#ENTRYPOINT ["/usr/local/bin/ss-local"]  
CMD ["bash"]

