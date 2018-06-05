FROM alpine:3.4  
MAINTAINER Baptiste Assmann <bedis9@gmail.com>  
  
ARG HAPROXY_VER=  
  
ENV DEL_PKGS="libgcc libstdc++ lua5.3-dev openssl-dev pcre-dev zlib-dev" \  
RM_DIRS="/usr/src/* /var/cache/apk/*" \  
HAPROXY_BUILD_DEPENDENCY="lua5.3 lua5.3-dev openssl openssl-dev pcre pcre-dev
zlib zlib-dev"  
COPY ./installer/ /usr/src/  
  
RUN apk add -U bash socat curl util-linux make gcc libc-dev linux-headers
libgcc ${HAPROXY_BUILD_DEPENDENCY} \  
&& cd /root \  
&& curl https://get.acme.sh | sh \  
&& cd /usr/src \  
&& if [ ! -f haproxy-${HAPROXY_VER}.tar.gz ]; then \  
curl -L -v -o haproxy-${HAPROXY_VER}.tar.gz
http://www.haproxy.org/download/${HAPROXY_VER}/src/snapshot/haproxy-ss-
LATEST.tar.gz ; \  
fi \  
&& tar xzf haproxy-${HAPROXY_VER}.tar.gz \  
&& rm -f haproxy-${HAPROXY_VER}.tar.gz \  
&& cd /usr/src/haproxy-* \  
&& make TARGET=linux2628 USE_LUA=1 LUA_LIB=/usr/lib/lua5.3/
LUA_INC=/usr/include/lua5.3 USE_OPENSSL=1 USE_PCRE=1 USE_ZLIB=1 \  
&& cp haproxy /usr/sbin/ \  
&& apk del make gcc libc-dev linux-headers libgcc ${DEL_PKGS} \  
&& rm -rf ${RM_DIRS} \  
&& addgroup -S -g 101 haproxy \  
&& adduser -S -H -D -u 100 -s /sbin/nologin haproxy haproxy  
  
ADD letsencryptforhaproxy.sh letsencryptocspforhaproxy.sh start_haproxy.sh /  
  
ENTRYPOINT /start_haproxy.sh  

