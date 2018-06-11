FROM playn/alpine:edge  
  
ARG version=0.3  
  
RUN set -xe && \  
apk \--update add \--no-cache \--virtual .run-deps \  
libevent \  
libsodium && \  
apk \--update add \--no-cache \--virtual .build-deps \  
autoconf \  
bsd-compat-headers \  
build-base \  
libevent-dev \  
libexecinfo-dev \  
libsodium-dev && \  
wget https://github.com/cofyc/dnscrypt-wrapper/archive/v${version}.tar.gz && \  
tar zxvf v${version}.tar.gz && \  
cd dnscrypt-wrapper-${version} && \  
make configure && \  
./configure && \  
make install && \  
cd .. && \  
rm -rf dnscrypt-wrapper-${version} v${version}.tar.gz && \  
apk del .build-deps && \  
mkdir -p /var/lib/dnscrypt-wrapper/dnskey && \  
rm -rf /var/cache/apk/*

