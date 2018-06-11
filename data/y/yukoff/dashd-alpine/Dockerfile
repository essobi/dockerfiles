FROM yukoff/alpine-bdb48:latest  
ENV VERSION ${VERSION:-0.12.2.1}  
ENV HOME /dash  
  
# add user with specified (or default) user/group ids  
ENV USERID ${USERID:-1000}  
ENV GROUPID ${GROUPID:-1000}  
RUN addgroup -g ${GROUPID} dash && \  
adduser -u ${USERID} -G dash -S -D -H -h /dash dash  
  
RUN apk --no-cache upgrade && \  
apk --no-cache add \  
git \  
build-base \  
ccache \  
autoconf \  
automake \  
boost-dev \  
boost \  
boost-system \  
boost-filesystem \  
boost-program_options \  
boost-thread \  
libevent-dev \  
libevent \  
libgcc \  
libressl-dev \  
libressl \  
libstdc++ \  
libtool \  
zeromq-dev \  
libzmq \  
miniupnpc-dev \  
miniupnpc && \  
git clone -b v${VERSION} --depth 50 https://github.com/dashpay/dash.git
/tmp/dash && \  
cd /tmp/dash && \  
./autogen.sh && \  
./configure --prefix=/usr \  
\--disable-shared \  
\--enable-static \  
\--disable-tests \  
\--without-gui && \  
make -j `grep -c ^processor /proc/cpuinfo` && \  
make install && \  
strip -s /usr/bin/*dash* && \  
cd - && \  
apk del \  
miniupnpc-dev \  
zeromq-dev \  
libtool \  
libressl-dev \  
libevent-dev \  
boost-dev \  
automake \  
autoconf \  
ccache \  
build-base \  
git && \  
rm -rf /tmp/dash  
USER dash  
VOLUME ["/dash"]  
EXPOSE 9998 9999 19998 19999  
WORKDIR /dash  
#ENTRYPOINT ["/usr/bin/dashd"]  

