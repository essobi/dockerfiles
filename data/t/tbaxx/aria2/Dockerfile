FROM alpine:3.7  
  
RUN apk add --no-cache \  
ca-certificates \  
openssl-dev \  
expat-dev \  
libssh2-dev \  
zlib-dev \  
nettle-dev \  
g++ \  
make \  
automake \  
autoconf \  
libtool \  
gettext-dev \  
git && \  
git clone https://github.com/aria2/aria2 && \  
cd /aria2 && \  
git checkout tags/release-1.34.0 && \  
autoreconf -i && \  
./configure ARIA2_STATIC=yes \  
\--disable-nls \  
\--disable-bittorrent \  
\--disable-metalink \  
\--with-ca-bundle='/etc/ssl/certs/ca-certificates.crt' && \  
make && \  
make install && \  
cd / && \  
rm -rf /aria2 && \  
apk del \  
openssl-dev \  
expat-dev \  
libssh2-dev \  
zlib-dev \  
nettle-dev \  
g++ \  
make \  
automake \  
autoconf \  
libtool \  
gettext-dev \  
git  
  
EXPOSE 6800  
ENTRYPOINT ["aria2c"]

