FROM alpine:3.4  
  
LABEL vendor=implements.io  
LABEL io.implements.version=0.1.0  
  
ENV S6_OVERLAY_VERSION=v1.17.2.0 \  
NODE_VERSION=v8.6.0 \  
NPM_VERSION=5.4.2 \  
HOME=/root  
  
RUN apk upgrade --update \  
&& apk add --update bind-tools git curl make gcc g++ python linux-headers
libgcc libstdc++ nginx \  
&& curl -sSL https://github.com/just-
containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz | tar xfz - -C / \  
&& curl -sSL
https://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}.tar.gz | tar -xz
\  
&& cd /node-${NODE_VERSION} \  
&& ./configure --prefix=/usr --without-snapshot \  
&& make -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& make install \  
&& cd / \  
&& npm install -g npm@${NPM_VERSION} \  
&& apk del gcc g++ linux-headers \  
&& rm -rf /etc/ssl /node-${NODE_VERSION} /usr/include \  
/usr/share/man /tmp/* /var/cache/apk/* /root/.npm /root/.node-gyp \  
/usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc
/usr/lib/node_modules/npm/html  

