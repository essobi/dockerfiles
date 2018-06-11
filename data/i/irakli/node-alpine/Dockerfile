FROM alpine:3.6  
MAINTAINER Irakli Nadareishvili  
  
ENV REFRESHED_AT 2017-11-13_2123  
  
ENV NODE_VERSION=v8.9.1  
  
RUN apk upgrade \--update \  
&& apk add \--no-cache curl make gcc g++ linux-headers paxctl musl-dev \  
libgcc libstdc++ binutils-gold python openssl-dev zlib-dev \  
&& mkdir -p /root/src \  
&& cd /root/src \  
&& curl -sSL
https://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}.tar.gz | tar -xz
\  
&& cd /root/src/node-* \  
&& ./configure \--prefix=/usr \--without-snapshot \  
&& make -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& make install \  
&& paxctl -cm /usr/bin/node \  
&& npm cache clean \  
&& apk del make gcc g++ python linux-headers \  
&& rm -rf /root/src /tmp/* /usr/share/man /var/cache/apk/* \  
/root/.npm /root/.node-gyp /usr/lib/node_modules/npm/man \  
/usr/lib/node_modules/npm/doc /usr/lib/node_modules/npm/html \  
&& apk search \--update  
### RUNIT  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& apk \--update upgrade && apk add runit && rm -rf /var/cache/apk/* && apk
\--update search  
ADD runit_init /sbin/  
RUN chmod u+x /sbin/runit_init  
  
CMD ["/sbin/runit_init"]  

