FROM alpine:edge  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION=8.9.4 YARN_VERSION=latest  
ENV CONFIG_FLAGS="--fully-static"  
# --without-npm  
  
RUN adduser -D -u 1000 node \  
&& apk add --no-cache \  
bash git python make gnupg curl \  
libstdc++ \  
&& apk add --no-cache --virtual .build-deps \  
binutils-gold \  
curl \  
g++ \  
gcc \  
gnupg \  
libgcc \  
linux-headers \  
make \  
python \  
&& curl -SLO
"https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& tar -xf "node-v$NODE_VERSION.tar.xz" \  
&& cd "node-v$NODE_VERSION" \  
&& ./configure --prefix=/usr ${CONFIG_FLAGS} \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& apk del .build-deps \  
&& cd .. \  
&& rm -Rf "node-v$NODE_VERSION" \  
&& rm "node-v$NODE_VERSION.tar.xz" SHASUMS256.txt.asc \  
&& echo http://dl-4.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories \  
&& apk add --no-cache mongodb \  
&& rm /usr/bin/mongoperf \  
&& apk add --no-cache g++ \  
&& mkdir -p /data/db \  
&& chown -R mongodb:mongodb /data/db \  
&& chown -R mongodb /data/db \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
6A010C5166006599AA17F08146C2130DFD2497F5 \  
&& curl -sSL -O https://yarnpkg.com/${YARN_VERSION}.tar.gz -O
https://yarnpkg.com/${YARN_VERSION}.tar.gz.asc \  
&& gpg --batch --verify ${YARN_VERSION}.tar.gz.asc ${YARN_VERSION}.tar.gz \  
&& mkdir /usr/local/share/yarn \  
&& tar -xf ${YARN_VERSION}.tar.gz -C /usr/local/share/yarn --strip 1 \  
&& ln -s /usr/local/share/yarn/bin/yarn /usr/local/bin/ \  
&& ln -s /usr/local/share/yarn/bin/yarnpkg /usr/local/bin/ \  
&& rm ${YARN_VERSION}.tar.gz* \  
&& yarn global add node-gyp gulp  
  
#RUN npm install -g yarn  
#RUN yarn global add node-gyp gulp  
  
ENTRYPOINT [ "node" ]  
  

