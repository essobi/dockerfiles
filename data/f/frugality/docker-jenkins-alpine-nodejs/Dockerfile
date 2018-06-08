FROM jenkins/jenkins:lts-alpine  
  
MAINTAINER Courtland Idstrom "ohmybees@gmail.com"  
  
ENV NODE_VERSION 8.5.0  
  
# Switch to root user  
USER root  
  
RUN apk add \--no-cache \  
libstdc++ \  
&& apk add \--no-cache --virtual .build-deps \  
binutils-gold \  
g++ \  
gcc \  
libgcc \  
linux-headers \  
make \  
python \  
&& cd /tmp \  
&& curl -SLO
"https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.xz" \  
&& tar -xf "node-v$NODE_VERSION.tar.xz" \  
&& cd "node-v$NODE_VERSION" \  
&& ./configure \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& apk del .build-deps \  
&& cd .. \  
&& rm -Rf "node-v$NODE_VERSION" \  
&& rm "node-v$NODE_VERSION.tar.xz"  
  
ENV YARN_VERSION 1.0.2  
  
RUN curl -fSL -o /usr/local/bin/yarn
"https://github.com/yarnpkg/yarn/releases/download/v$YARN_VERSION/yarn-$YARN_VERSION.js"
\  
&& chmod +x /usr/local/bin/yarn  
  
# Switch to jenkins user  
USER jenkins  

