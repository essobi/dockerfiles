FROM ruby:2.3.1-alpine  
  
RUN apk add --no-cache \  
autoconf \  
automake \  
build-base \  
curl \  
git \  
gnupg \  
linux-headers \  
nasm \  
python \  
paxctl  
  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
# Download and build Node.js  
ENV NODE_VERSION=v6.2.1 NPM_VERSION=3  
RUN curl -o node-${NODE_VERSION}.tar.gz -sSL
https://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}.tar.gz \  
&& curl -o SHASUMS256.txt.asc -sSL
https://nodejs.org/dist/${NODE_VERSION}/SHASUMS256.txt.asc \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep node-${NODE_VERSION}.tar.gz SHASUMS256.txt.asc | sha256sum -c - \  
&& tar -zxf node-${NODE_VERSION}.tar.gz \  
&& cd node-${NODE_VERSION} \  
&& export GYP_DEFINES="linux_use_gold_flags=0" \  
&& ./configure --prefix=/usr ${CONFIG_FLAGS} \  
&& NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& make -j${NPROC} -C out mksnapshot BUILDTYPE=Release \  
&& paxctl -cm out/Release/mksnapshot \  
&& make -j${NPROC} \  
&& make install \  
&& paxctl -cm /usr/bin/node  
  
# See npm/npm#9863  
RUN cd $(npm root -g)/npm \  
&& npm install fs-extra \  
&& sed -i -e s/graceful-fs/fs-extra/ -e s/fs.rename/fs.move/
./lib/utils/rename.js  
  
# Install npm  
RUN cd / \  
&& npm install -g npm@${NPM_VERSION} \  
&& find /usr/lib/node_modules/npm -name test -o -name .bin -type d | xargs rm
-rf;  
  
# Cleanup Node.js build  
RUN rm -rf \  
/node-${NODE_VERSION}.tar.gz \  
/SHASUMS256.txt.asc \  
/node-${NODE_VERSION} \  
/root/.npm \  
/root/.node-gyp  
  
RUN gem install bundler  
  
EXPOSE 3000 3001  

