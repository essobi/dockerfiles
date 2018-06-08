FROM alpine:latest  
  
ENV VERSION 4.1.1  
LABEL maintainer="support@opensvc.com"  
  
RUN \  
apk --update add \--no-cache boost lua musl bash libstdc++ file openssl && \  
apk add \--no-cache --virtual .build-deps curl build-base wget boost-dev \  
lua-dev autoconf automake bison flex g++ libtool make ragel \  
boost-program_options boost-serialization openssl-dev && \  
curl -sS https://downloads.powerdns.com/releases/pdns-
recursor-$VERSION.tar.bz2 | \  
tar xjf - -C . && \  
cd pdns-* && \  
./configure && \  
make && \  
make install && \  
cd .. && rm -fr pdns-* && \  
apk del curl build-base wget boost-dev autoconf automake bison \  
flex g++ libtool make ragel openssl-dev && \  
apk del .build-deps  
  
EXPOSE 53/udp 53/tcp  
  
ENTRYPOINT ["/usr/local/sbin/pdns_recursor"]  

