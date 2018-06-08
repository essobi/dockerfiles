FROM alpine:3.3  
MAINTAINER Orbweb Inc. <engineering@orbweb.com>  
  
ENV VERSION 1.7.2  
COPY src/pgbouncer /opt/src/pgbouncer  
RUN apk --no-cache add --virtual .build-deps \  
build-base automake autoconf libtool pkgconfig \  
libevent-dev \  
openssl-dev \  
c-ares-dev && \  
apk --no-cache add --virtual .run-deps \  
libevent \  
openssl \  
c-ares && \  
cd /opt/src/pgbouncer && \  
./autogen.sh && \  
./configure --prefix=/usr/local \  
\--with-libevent=libevent-prefix \  
\--with-cares=prefix \  
\--with-openssl=prefix && \  
make && \  
make install && \  
rm -rf /opt/src/pgbouncer && \  
apk del .build-deps  
RUN mkdir -p /etc/pgbouncer  
  
EXPOSE 6432/tcp  
ENTRYPOINT ["pgbouncer"]  
CMD ["/etc/pgbouncer/pgbouncer.ini"]  

