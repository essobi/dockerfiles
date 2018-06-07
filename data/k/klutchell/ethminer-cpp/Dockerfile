# forked from https://github.com/ethereum/cpp-
ethereum/blob/develop/scripts/Dockerfile for miner support  
FROM alpine  
  
MAINTAINER Kyle Harding <kylemharding@gmail.com>  
  
RUN apk add --no-cache \  
libstdc++ \  
gmp \  
libcurl \  
libmicrohttpd \  
leveldb --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing/  
  
RUN apk add --no-cache --virtual .build-deps \  
git \  
cmake \  
g++ \  
make \  
linux-headers curl-dev libmicrohttpd-dev \  
leveldb-dev --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing/  
  
RUN sed -i -E -e 's|#warning|//#warning|' /usr/include/sys/poll.h && \  
git clone \--recursive https://github.com/ethereum/cpp-ethereum --branch
develop --single-branch --depth 1  
  
RUN mkdir /build && \  
cd /build && \  
cmake /cpp-ethereum -DCMAKE_BUILD_TYPE=RelWithDebInfo -DTESTS=Off && \  
make -j $(cat /proc/cpuinfo | grep processor | wc -l) && \  
make install  
  
RUN cd / && \  
rm /build -rf && \  
rm /cpp-ethereum -rf && \  
apk del .build-deps && \  
rm /var/cache/apk/* -f  
  
ENTRYPOINT [ "/usr/local/bin/ethminer" ]  

