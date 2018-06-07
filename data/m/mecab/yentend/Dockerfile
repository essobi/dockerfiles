FROM alpine:3.6  
LABEL maintainer "mecab <mecab@misosi.ru>"  
  
RUN apk add --no-cache --virtual .build-requirements alpine-sdk autoconf
libtool automake boost-dev openssl-dev && \  
cd /tmp && \  
curl -L http://download.oracle.com/berkeley-db/db-4.8.30.NC.tar.gz -o
db-4.8.30.NC.tar.gz && \  
tar zxvf db-4.8.30.NC.tar.gz && \  
cd /tmp/db-4.8.30.NC && \  
cd build_unix && \  
../dist/configure --disable-shared --enable-cxx --disable-replication --with-
pic --prefix=/usr/local/ && \  
make libdb_cxx-4.8.a libdb-4.8.a && \  
make install_lib install_include && \  
\  
cd /tmp && \  
curl -L https://github.com/conan-equal-newone/yenten/archive/1.3.1.tar.gz -o
yenten-1.3.1.tar.gz && \  
tar -zxvf yenten-1.3.1.tar.gz && \  
cd /tmp/yenten-1.3.1 && \  
./autogen.sh && \  
./configure LDFLAGS=-L/usr/local/lib/ CPPFLAGS=-I/usr/local/include/ --enable-
upnp-default --without-gui --disable-tests && \  
make && \  
make install && \  
\  
rm -rf /tmp/db-4.8.30NC && \  
rm -rf /tmp/yenten-1.3.1.tar.gz && \  
apk del .build-requirements  
  
RUN apk add --no-cache boost boost-program_options openssl  
  
ENTRYPOINT ["/usr/local/bin/yentend"]  
VOLUME ["/data"]  
CMD ["-datadir=/data"]  

