FROM alpine:3.6  
MAINTAINER Filipe Ferreira <admin@itsfilipoficial.com>  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 8.9.1  
ENV YARN_VERSION 1.3.2  
RUN addgroup -g 1000 node \  
&& adduser -u 1000 -G node -s /bin/sh -D node \  
&& apk add --no-cache libstdc++ \  
&& apk add --no-cache --virtual .build-deps binutils-gold curl g++ gcc gnupg
libgcc linux-headers make python \  
&& curl -SLO
"https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.xz" \  
&& curl -SLO --compressed
"https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& tar -xf "node-v$NODE_VERSION.tar.xz" \  
&& cd "node-v$NODE_VERSION" \  
&& ./configure \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& apk del .build-deps \  
&& cd .. \  
&& rm -Rf "node-v$NODE_VERSION" \  
&& rm "node-v$NODE_VERSION.tar.xz"  
  
RUN apk add --no-cache --virtual .build-deps-yarn curl gnupg tar \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \  
&& mkdir -p /opt/yarn \  
&& tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/yarn --strip-components=1 \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpkg \  
&& rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz \  
&& apk del .build-deps-yarn  
  
RUN apk add --no-cache --virtual .gyp python make g++ bash ca-certificates
mongodb  
  
RUN npm i -g npm  
  
CMD [ "node" ]  

