FROM alpine:3.2  
  
ENV NODE_VERSION=v6.2.0 NPM_VERSION=3.8.9  
  
RUN apk add --update git curl make gcc g++ python linux-headers paxctl libgcc
libstdc++ && \  
curl -sSL https://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}.tar.gz
| tar -xz && \  
cd /node-${NODE_VERSION} && \  
./configure --prefix=/usr && \  
make && \  
make install && \  
paxctl -cm /usr/bin/node && \  
cd / && \  
npm install -g npm@${NPM_VERSION} && \  
find /usr/lib/node_modules/npm -name test -o -name .bin -type d | xargs rm
-rf; \  
apk del curl make gcc g++ python linux-headers paxctl && \  
rm -rf /node-${NODE_VERSION} \  
/usr/share/man /tmp/* /var/cache/apk/* /root/.npm /root/.node-gyp \  
/usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc
/usr/lib/node_modules/npm/html  
  
ENTRYPOINT ["node"]  

