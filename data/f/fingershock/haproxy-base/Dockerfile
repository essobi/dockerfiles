FROM alpine:3.3  
MAINTAINER Bryan Talbot <bryan.talbot@ijji.com>  
  
# haproxy version to use  
ENV HAPROXY_MAJOR=1.6 \  
HAPROXY_VERSION=1.6.3 \  
HAPROXY_SHA256=fd06b45054cde2c69cb3322dfdd8a4bcfc46eb9d0c4b36d20d3ea19d84e338a7  
  
# download, compile and install haproxy  
RUN apk update && \  
BUILD_DEPS="gcc libc-dev pcre-dev linux-headers openssl-dev lua5.3-dev make"
&& \  
apk add ${BUILD_DEPS} socat pcre lua5.3 ca-certificates wget && \  
mkdir -p /usr/src && \  
wget -q -O /usr/src/haproxy-${HAPROXY_VERSION}.tar.gz
http://www.haproxy.org/download/${HAPROXY_MAJOR}/src/haproxy-${HAPROXY_VERSION}.tar.gz
&& \  
echo "${HAPROXY_SHA256} /usr/src/haproxy-${HAPROXY_VERSION}.tar.gz" |
sha256sum -c - && \  
tar -xzf /usr/src/haproxy-${HAPROXY_VERSION}.tar.gz -C /usr/src && \  
rm /usr/src/haproxy-${HAPROXY_VERSION}.tar.gz && \  
make -C /usr/src/haproxy-${HAPROXY_VERSION} TARGET=linux2628 USE_PCRE=1
USE_PCRE_JIT=1 USE_OPENSSL=1 USE_ZLIB=1 USE_TFO=1 USE_NS=1 USE_LUA=1
LUA_LIB=/usr/lib/lua5.3 LUA_INC=/usr/include/lua5.3 all install-bin && \  
make -C /usr/src/haproxy-${HAPROXY_VERSION}/contrib/halog halog && \  
install -d /usr/local/bin && \  
install /usr/src/haproxy-${HAPROXY_VERSION}/contrib/halog/halog /usr/local/bin
&& \  
rm -rf /usr/src/haproxy-${HAPROXY_VERSION} && \  
mkdir -p /usr/local/etc/haproxy && \  
apk del --purge ${BUILD_DEPS} && \  
rm -rf /var/cache/apk/*  
  
VOLUME ["/usr/local/etc/haproxy", "/dev/log"]  

