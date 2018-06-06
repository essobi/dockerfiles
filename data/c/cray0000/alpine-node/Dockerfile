FROM gliderlabs/alpine:3.2  
ENV VERSION=v0.12.4 CMD=node DOMAIN=nodejs.org  
  
ENV CONFIG_FLAGS="--fully-static" DEL_PKGS="" RM_DIRS=/usr/include  
  
RUN apk-install curl git make gcc g++ python linux-headers paxctl libgcc
libstdc++ && \  
curl -sSL https://${DOMAIN}/dist/${VERSION}/${CMD}-${VERSION}.tar.gz | tar -xz
&& \  
cd /${CMD}-${VERSION} && \  
./configure --prefix=/usr ${CONFIG_FLAGS} && \  
make -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \  
make install && \  
paxctl -cm /usr/bin/${CMD} && \  
cd / && \  
apk del linux-headers paxctl ${DEL_PKGS} && \  
rm -rf /etc/ssl /${CMD}-${VERSION} ${RM_DIRS} \  
/usr/share/man /tmp/* /root/.npm /root/.node-gyp \  
/usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc
/usr/lib/node_modules/npm/html  

