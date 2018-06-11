FROM ubuntu:xenial  
  
ARG NODE_VER=8.11.2  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y build-essential python wget && \  
mkdir tmp/node && \  
wget https://nodejs.org/dist/v$NODE_VER/node-v$NODE_VER.tar.gz -P tmp/node &&
\  
(cd tmp/node && tar \--strip-components=1 -zxf node-v$NODE_VER.tar.gz) && \  
(cd tmp/node && ./configure \--with-intl=full-icu --download=all) && \  
(cd tmp/node && make -j8) && \  
(cd tmp/node && make install) && \  
apt-get purge -y build-essential python wget $(apt-mark showauto) && \  
apt-get autoremove -y && \  
apt-get clean -y && \  
rm -rf tmp/node && \  
rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["node"]

