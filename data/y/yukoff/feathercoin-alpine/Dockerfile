FROM yukoff/alpine-bdb48:edge  
  
ENV HOME /feathercoin  
  
# add user with specified (or default) user/group ids  
ENV USERID ${USERID:-1000}  
ENV GROUPID ${GROUPID:-1000}  
RUN addgroup -g ${GROUPID} feathercoin && \  
adduser -u ${USERID} -G feathercoin -S -D -H -h /feathercoin feathercoin  
  
RUN apk --no-cache upgrade && \  
apk --no-cache add \  
git \  
build-base \  
ccache \  
autoconf \  
automake \  
boost-dev \  
boost-system \  
boost-filesystem \  
boost-program_options \  
boost-thread \  
libgcc \  
libressl-dev \  
libstdc++ \  
miniupnpc-dev \  
miniupnpc && \  
git clone --depth 50 https://github.com/feathercoin/feathercoin.git
/tmp/feathercoin && \  
cd /tmp/feathercoin && \  
./autogen.sh && \  
./configure --prefix=/usr \  
\--disable-shared \  
\--enable-static \  
\--disable-tests \  
\--without-gui && \  
make -j `grep -c ^processor /proc/cpuinfo` && \  
make install && \  
strip -s /usr/bin/*feathercoin* && \  
cd - && \  
apk del \  
miniupnpc-dev \  
libressl-dev \  
boost-dev \  
automake \  
autoconf \  
ccache \  
build-base \  
git && \  
rm -rf /tmp/feathercoin  
USER feathercoin  
VOLUME ["/feathercoin"]  
EXPOSE 9336 9337 19336 19337  
WORKDIR /feathercoin  
#ENTRYPOINT ["/usr/bin/feathercoind"]  

