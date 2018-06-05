FROM area51/alpine  
MAINTAINER Peter Mount <peter@retep.org>  
  
# Current V8 needed for http/2 support  
ENV VERSION=v8.2.1  
  
RUN apk add --no-cache \  
curl \  
make \  
gcc \  
g++ \  
python \  
linux-headers \  
paxctl \  
libgcc \  
libstdc++ && \  
cd /tmp &&\  
curl -o node-${VERSION}.tar.gz -sSL
https://nodejs.org/dist/${VERSION}/node-${VERSION}.tar.gz && \  
tar -zxf node-${VERSION}.tar.gz && \  
cd node-${VERSION} && \  
export GYP_DEFINES="linux_use_gold_flags=0" && \  
./configure --prefix=/usr ${CONFIG_FLAGS} && \  
NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \  
make -j${NPROC} -C out mksnapshot BUILDTYPE=Release && \  
paxctl -cm out/Release/mksnapshot && \  
make -j${NPROC} && \  
make install && \  
paxctl -cm /usr/bin/node && \  
cd / && \  
apk del \  
curl \  
make \  
gcc \  
g++ \  
python \  
linux-headers \  
paxctl && \  
rm -rf /etc/ssl \  
/usr/share/man \  
/tmp/* \  
/var/cache/apk/* \  
/root/.npm \  
/root/.node-gyp \  
/root/.gnupg \  
/usr/lib/node_modules/npm/man \  
/usr/lib/node_modules/npm/doc \  
/usr/lib/node_modules/npm/html  

