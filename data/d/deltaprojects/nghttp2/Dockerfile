FROM alpine:3.5  
MAINTAINER Delta Projects <no-reply@deltaprojects.com>  
  
ENV NGHTTP2_VERSION 1.18.0  
ENV BUILD_DEPS wget libc-dev gcc g++ make file  
ENV RUN_DEPS ca-certificates libstdc++ openssl-dev libev-dev zlib-dev jansson-
dev libxml2-dev jemalloc-dev c-ares-dev  
  
RUN apk --no-cache add $BUILD_DEPS $RUN_DEPS \  
&& cd /tmp \  
&& wget -qO-
"https://github.com/nghttp2/nghttp2/releases/download/v${NGHTTP2_VERSION}/nghttp2-${NGHTTP2_VERSION}.tar.gz"
| tar -xz \  
&& cd /tmp/nghttp2-$NGHTTP2_VERSION \  
&& ./configure --enable-app --enable-hpack-tools \  
&& make \  
&& make install-strip \  
&& apk del $BUILD_DEPS \  
&& rm -rf /tmp/*  

