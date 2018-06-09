FROM remind101/base-alpine  
MAINTAINER Ben Guillet <beng@remind101.com>  
  
ENV VERSION=v0.10.38  
ENV CFLAGS="-D__USE_MISC"  
RUN apk add --update curl make gcc g++ python paxctl libgcc libstdc++ && \  
curl -sSL https://nodejs.org/dist/${VERSION}/node-${VERSION}.tar.gz | tar -xz
&& \  
cd node-${VERSION} && \  
./configure --prefix=/usr && \  
make -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \  
make install && \  
paxctl -cm /usr/bin/node && \  
if [ -x /usr/bin/npm -a -z "$NO_NPM_UPDATE" ]; then \  
npm install -g npm && \  
find /usr/lib/node_modules/npm -name test -o -name .bin -type d | xargs rm
-rf; \  
fi && \  
apk del curl make gcc g++ python paxctl libgcc libstdc++ && \  
rm -rf /etc/ssl /node-${VERSION} \  
/usr/share/man /tmp/* /root/.npm /root/.node-gyp \  
/usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc
/usr/lib/node_modules/npm/html  
  
WORKDIR /home/app  
COPY ./build.sh /build  
ONBUILD COPY . /home/app  
ONBUILD RUN /build  
  
ONBUILD USER app  

