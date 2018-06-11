FROM yobasystems/alpine:amd64  
LABEL maintainer "Dominic Taylor <dominic@yobasystems.co.uk>"
architecture="AMD64/x86_64" version="6.11.3"  
  
ARG NODE_VER=6.11.3  
ARG NPM_VER=3  
  
RUN apk -U add curl git make gcc g++ python linux-headers paxctl libgcc
libstdc++ binutils-gold ca-certificates \  
&& cd /tmp \  
&& curl --silent --ssl
https://nodejs.org/dist/v$NODE_VER/node-v$NODE_VER.tar.gz | tar zxf - \  
&& cd node-v$NODE_VER \  
&& ./configure --prefix=/usr \  
&& make -j1 && make install \  
&& paxctl -cm /usr/bin/node \  
&& npm install -g npm@$NPM_VER \  
&& find /usr/lib/node_modules/npm -name test -o -name .bin -type d \  
| xargs rm -rf \  
&& apk del \  
curl \  
git \  
make \  
gcc \  
g++ \  
python \  
linux-headers \  
paxctl \  
grep \  
binutils-gold \  
ca-certificates \  
&& rm -rf \  
/tmp/* \  
/var/cache/apk/* \  
/root/.npm \  
/root/.node-gyp \  
/usr/lib/node_modules/npm/man \  
/usr/lib/node_modules/npm/doc \  
/usr/lib/node_modules/npm/html \  
/usr/share/man  
  
CMD ["node", "-v"]  

