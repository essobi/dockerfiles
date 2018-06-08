FROM xataz/alpine:3.4  
MAINTAINER xataz <https://github.com/xataz/>  
  
ARG NODE_VER=v6.3.1  
ARG NPM_VER=3  
ARG CORES_BUILD  
  
LABEL description="nodejs based on alpine" \  
tags="latest 6.3.1 6.3 6" \  
build_ver="2016080901"  
  
ENV UID=997 \  
GID=991  
  
RUN export BUILD_DEPS="git \  
wget \  
make \  
gcc \  
g++ \  
python \  
linux-headers \  
paxctl \  
binutils-gold" \  
&& apk add --update libgcc libstdc++ ${BUILD_DEPS} \  
&& cd /tmp \  
&& wget https://nodejs.org/dist/${NODE_VER}/node-${NODE_VER}.tar.gz \  
&& tar xzf node-${NODE_VER}.tar.gz \  
&& cd /tmp/node-${NODE_VER} \  
&& NB_CORES=${CORES_BUILD-$(grep -c "processor" /proc/cpuinfo)} \  
&& ./configure --prefix=/usr \  
&& make -j ${NB_CORES} \  
&& make install && paxctl -cm /usr/bin/node \  
&& npm install -g npm@${NPM_VER} \  
&& find /usr/lib/node_modules/npm -name test -o -name .bin -type d | xargs rm
-rf \  
&& cd / \  
&& apk del ${BUILD_DEPS} \  
&& rm -rf /tmp/* \  
/var/cache/apk/* \  
/root/.npm \  
/root/.node-gyp \  
/usr/lib/node_modules/npm/man \  
/usr/lib/node_modules/npm/doc \  
/usr/lib/node_modules/npm/html \  
/usr/share/man  
  
ENTRYPOINT ["su-exec", "${UID}:${GID}", "node"]  
CMD ["-v"]  

