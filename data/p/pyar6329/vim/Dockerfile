# vim  
# docker build -t pyar6329/vim:1.0 .  
# docker run -it --rm -v /home/core/share:/home/workspace pyar6329/docker-
vim:1.0 sh  
# docker rmi pyar6329/vim:1.0  
# alias dvim="docker run -it --rm -v $(pwd):/home/workspace pyar6329/vim:1.0"  
  
FROM alpine:latest  
MAINTAINER Tsukasa Arima  
  
ENV NODE_VERSION 4.4.0  
  
RUN set -ex \  
&& apk --no-cache add --virtual build-dependencies make gcc g++ linux-headers
binutils-gold python curl paxctl gpgme bash build-base git \  
&& apk --update --no-cache add lua ruby vim perl libgcc libstdc++ \  
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
gpg --keyserver keyserver.ubuntu.com --recv-keys "$key"; \  
done \  
&& mkdir -p /tmp/src \  
&& cd /tmp/src \  
&& curl --location \--show-error -O
https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}.tar.gz \  
&& curl --location \--show-error -O
https://nodejs.org/dist/v${NODE_VERSION}/SHASUMS256.txt.asc \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep " node-v${NODE_VERSION}.tar.gz\$" SHASUMS256.txt.asc | sha256sum -c -
\  
&& tar -xzf "node-v${NODE_VERSION}.tar.gz" \  
&& cd /tmp/src/node-v${NODE_VERSION} \  
&& ./configure \  
\--prefix=/opt/node \  
\--without-snapshot \  
\--fully-static \  
&& make -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& make install \  
&& git clone https://github.com/pyarbz/.vim.git ~/.vim \  
&& cd ~/.vim \  
&& ./install.sh \  
&& cd / \  
&& paxctl -cm /opt/node/bin/node \  
&& apk del --purge build-dependencies \  
&& rm -rf /tmp/* \  
/etc/ssl \  
/opt/node/include/ \  
/opt/node/share/man/ \  
/opt/node/lib/node_modules/npm/man \  
/opt/node/lib/node_modules/npm/doc \  
/opt/node/lib/node_modules/npm/html  
  
ENV PATH ${PATH}:/opt/node/bin \  
NODE_PATH /opt/node/lib/node_modules  
  
WORKDIR /home/workspace  
  
ENTRYPOINT ["vim"]  

