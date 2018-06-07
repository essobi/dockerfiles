# builder stage  
FROM alpine:3.7 AS builder  
  
# install build dependencies  
RUN apk add --no-cache \  
alpine-sdk \  
git \  
libressl-dev \  
libevent-dev \  
sqlite-dev \  
postgresql-dev \  
linux-headers  
  
# fetch source code  
ARG COTURN_GIT_URL=https://github.com/coturn/coturn.git  
ARG COTURN_VERSION=4.5.0.7  
RUN git clone \--recursive "$COTURN_GIT_URL" /src \  
&& cd /src && git checkout "${COTURN_VERSION}"  
  
# configure and build  
RUN cd /src && ./configure \  
\--sysconfdir=/etc \  
\--turndbdir=/db \  
\--prefix=/target \  
\--localstatedir=/var  
  
RUN cd /src && make -j$(nproc)  
RUN cd /src && make install  
  
###  
# Final image  
FROM alpine:3.7  
# install runtime dependencies  
RUN apk add --no-cache \  
libressl2.6-libcrypto \  
libevent \  
sqlite-libs \  
postgresql-libs  
  
# copy built files from builder stage  
COPY \--from=builder /target/ /usr/local/  
  
STOPSIGNAL TERM  
  
ENTRYPOINT ["turnserver"]  

