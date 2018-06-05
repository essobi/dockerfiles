FROM java:jre-alpine  
  
ENV LIBSODIUM_VERSION=1.0.11  
  
RUN apk add \--update build-base curl && \  
curl -LOs
https://github.com/jedisct1/libsodium/releases/download/$LIBSODIUM_VERSION/libsodium-$LIBSODIUM_VERSION.tar.gz
&& \  
tar -zxvf libsodium-$LIBSODIUM_VERSION.tar.gz && \  
(cd libsodium-$LIBSODIUM_VERSION && ./configure && make && make check && make
install) && \  
apk del build-base curl && \  
rm -rf /var/cache/apk/*  

