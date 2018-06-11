FROM alpine:edge AS build-env  
ENV BERKELEYDB_VERSION=db-4.8.30.NC \  
BERKELEYDB_PREFIX=/opt/${BERKELEYDB_VERSION} \  
YENTEN_USER=yenten \  
YENTEN_VERSION=1.3.1 \  
YENTEN_PREFIX=/opt/yenten-${YENTEN_VERSION} \  
YENTEN_DATA=/home/${YENTEN_USER}/.yenten \  
PATH=${YENTEN_PREFIX}/bin:$PATH \  
BUILD_DEPENDENCIES="git build-base autoconf automake libtool g++ make boost-
dev libressl-dev miniupnpc-dev protobuf-dev libqrencode-dev libevent-dev
build-base"  
RUN apk --no-cache --update add ${BUILD_DEPENDENCIES} && \  
mkdir -p /tmp/build && \  
mkdir -p /tmp/build/${YENTEN_VERSION} && \  
mkdir -p ${YENTEN_PREFIX} && \  
wget -O /tmp/build/${BERKELEYDB_VERSION}.tar.gz
http://download.oracle.com/berkeley-db/${BERKELEYDB_VERSION}.tar.gz && \  
tar -xzf /tmp/build/${BERKELEYDB_VERSION}.tar.gz -C /tmp/build/ && \  
sed s/__atomic_compare_exchange/__atomic_compare_exchange_db/g -i
/tmp/build/${BERKELEYDB_VERSION}/dbinc/atomic.h && \  
mkdir -p ${BERKELEYDB_PREFIX} && \  
cd /tmp/build/${BERKELEYDB_VERSION}/build_unix && \  
../dist/configure CPPFLAGS="-Wno-format-security" \  
\--enable-cxx --disable-shared --with-pic \  
\--prefix=${BERKELEYDB_PREFIX} && \  
make install && \  
cd /tmp/build/${YENTEN_VERSION} && \  
git clone https://github.com/conan-equal-newone/yenten.git && \  
cd yenten && \  
./autogen.sh && \  
./configure LDFLAGS=-L${BERKELEYDB_PREFIX}/lib/
CPPFLAGS=-I${BERKELEYDB_PREFIX}/include/ \  
\--prefix=${YENTEN_PREFIX} \  
\--enable-upnp-default --without-gui --disable-tests && \  
make -j2 && \  
make install  
  
FROM alpine:edge as runtime  
ENV YENTEN_VERSION=1.3.1 \  
YENTEN_USER=yenten \  
YENTEN_DATA=/home/${YENTEN_USER}/.yenten \  
SRC_YENTEN_PREFIX=/opt/yenten-${YENTEN_VERSION} \  
TARGET_YENTEN_PREFIX=/opt/yenten  
RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-
linux-x86-64.so.2 && \  
apk add --no-cache ca-certificates shadow \  
boost boost-program_options \  
libressl miniupnpc protobuf libqrencode libevent && \  
mkdir -p ${TARGET_YENTEN_PREFIX}/bin/ && \  
adduser -D ${YENTEN_USER}  
COPY \--from=build-env ${SRC_YENTEN_PREFIX}/bin/ ${TARGET_YENTEN_PREFIX}/bin/  
  
USER ${YENTEN_USER}  
ENV YENTEN_USER=yenten \  
YENTEN_DATA=/home/${YENTEN_USER}/.yenten \  
TARGET_YENTEN_PREFIX=/opt/yenten  
RUN mkdir -p ${YENTEN_DATA}  
  
VOLUME ${YENTEN_DATA}  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
EXPOSE 9981 9982  

