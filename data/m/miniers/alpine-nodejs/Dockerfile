FROM alpine:3.5  
  
MAINTAINER miniers <m@minier.cc>  
  
ENV S6_OVERLAY_VERSION=v1.19.1.1 \  
NODE_VERSION=v7.10.0  
  
RUN apk add \--update \--no-cache bind-tools curl libcap && \  
curl -sSL https://github.com/just-
containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz \  
| tar xfz - -C / && \  
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
echo "Asia/Shanghai" > /etc/timezone && \  
apk del curl && \  
rm -rf /var/cache/apk/*  
  
RUN apk add \--update git curl make gcc g++ python linux-headers libgcc
libstdc++ && \  
curl -sSL https://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}.tar.gz
| tar -xz && \  
cd /node-${NODE_VERSION} && \  
./configure \--prefix=/usr \--without-snapshot && \  
make -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \  
make install && \  
cd / && \  
npm install npm@latest -g && \  
apk del gcc g++ linux-headers && \  
rm -rf /etc/ssl /node-${NODE_VERSION} /usr/include \  
/usr/share/man /tmp/* /var/cache/apk/* /root/.npm /root/.node-gyp \  
/usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc
/usr/lib/node_modules/npm/html  
  
ADD root /  
  
ENTRYPOINT ["/init"]

