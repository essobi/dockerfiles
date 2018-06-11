FROM kiasaki/alpine-golang  
  
RUN apk update  
RUN apk add zsh git curl make gcc g++ python linux-headers paxctl libgcc
libstdc++  
  
# INSTALL IPFS  
RUN go get -v -u github.com/ipfs/go-ipfs/cmd/ipfs  
  
# Install NODEJS  
ENV VERSION=v4.0.0  
# For base builds  
# ENV CONFIG_FLAGS="--without-npm" RM_DIRS=/usr/include  
ENV CONFIG_FLAGS="--fully-static" DEL_PKGS="libgcc libstdc++"
RM_DIRS=/usr/include  
  
RUN curl -sSL https://nodejs.org/dist/${VERSION}/node-${VERSION}.tar.gz | tar
-xz && \  
cd /node-${VERSION} && \  
./configure --prefix=/usr ${CONFIG_FLAGS} && \  
make -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \  
make install && \  
paxctl -cm /usr/bin/node && \  
cd / && \  
if [ -x /usr/bin/npm ]; then \  
npm install -g npm && \  
find /usr/lib/node_modules/npm -name test -o -name .bin -type d | xargs rm
-rf; \  
fi && \  
apk del curl make gcc g++ python linux-headers paxctl ${DEL_PKGS} && \  
rm -rf /etc/ssl /node-${VERSION} ${RM_DIRS} \  
/usr/share/man /tmp/* /var/cache/apk/* /root/.npm /root/.node-gyp \  
/usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc
/usr/lib/node_modules/npm/html  
  
EXPOSE 3000 4001 5001 8080  
COPY . /app  
  
CMD ./app/startup.sh  

