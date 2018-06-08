FROM alpine:3.4  
  
ENV NODE_VERSION=v6.5.0 \  
NPM_VERSION=3 \  
NODE_HOME=/usr/local  
  
RUN \  
apk add --no-cache --update --virtual .node-buildDeps \  
git \  
curl \  
make \  
gcc \  
g++ \  
binutils-gold \  
python \  
linux-headers \  
paxctl \  
libgcc \  
libstdc++ \  
&& curl -sSL
https://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}.tar.gz | tar -xz
\  
&& cd /node-${NODE_VERSION} \  
&& ./configure --prefix=${NODE_HOME} ${CONFIG_FLAGS} \  
&& make -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& make install \  
&& paxctl -cm ${NODE_HOME}/bin/node \  
&& cd / \  
&& if [ -x ${NODE_HOME}/bin/npm ]; then \  
npm install -g npm@${NPM_VERSION} && \  
find ${NODE_HOME}/lib/node_modules/npm -name test -o -name .bin -type d |
xargs rm -rf; \  
fi \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .rundeps $runDeps \  
&& apk del .node-buildDeps \  
&& rm -rf /node-${NODE_VERSION} \  
${NODE_HOME}/share/man /tmp/* /root/.npm /root/.node-gyp \  
${NODE_HOME}/lib/node_modules/npm/man ${NODE_HOME}/lib/node_modules/npm/doc
${NODE_HOME}/lib/node_modules/npm/html \  
&& adduser -S node  
  
CMD [ "npm", "start" ]  

