FROM alpine:latest  
  
MAINTAINER unoexperto <unoexperto.support@mailnull.com>  
  
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing"
>>/etc/apk/repositories  
  
# python is necessary for ssdb-cli  
RUN apk update && \  
apk add gcc python && \  
apk add --virtual .build-deps autoconf make g++ linux-headers git && \  
apk add ca-certificates && \  
update-ca-certificates && \  
apk add openssl  
  
RUN apk add --update --no-cache zlib zlib-dev bzip2 bzip2-dev  
  
RUN mkdir -p /usr/src/ardb  
  
RUN git clone \--depth 1 https://github.com/yinqiwen/ardb.git /usr/src/ardb &&
\  
sed -e 's@JEMALLOC_VER=.*@JEMALLOC_VER=4.5.0@' -e
's@ROCKSDB_VER=.*@ROCKSDB_VER=5.0.2@' -i /usr/src/ardb/src/Makefile && \  
storage_engine=rocksdb make noopt -C /usr/src/ardb  
  
RUN apk del .build-deps  
  
RUN mkdir /ardb_home  
  
RUN sed -e 's@home .*@home /ardb_home@' -i /usr/src/ardb/ardb.conf  
  
EXPOSE 16379  
VOLUME /ardb_home  
WORKDIR /ardb_home  
  
CMD ["/usr/src/ardb/src/ardb-server", "/usr/src/ardb/ardb.conf"]  

