FROM alpine  
  
RUN apk add --no-cache --progress gcc g++ cmake make perl wget gfortran ca-
certificates \  
git libev-dev openssl-dev \  
python python-dev py-pip openjdk8-jre  
  
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h  
  
ENV LDFLAGS -Wl,-rpath=/app/lib  
  
RUN cd /tmp && \  
mkdir libcouchbase && \  
wget -O - https://github.com/couchbase/libcouchbase/archive/2.6.2.tar.gz | tar
xz && \  
cd libcouchbase-2.6.2 && \  
mkdir build && \  
cd build && \  
../cmake/configure --prefix=/usr && \  
sed -i.bak 's/#define LCB_VERSION 0x000000/#define LCB_VERSION 0x020602/'
generated/libcouchbase/configuration.h && \  
make install && \  
cd /tmp && \  
rm -rf libcouchbase-2.6.2  
  
RUN wget -O /tmp/CouchbaseMock-LATEST.jar
http://packages.couchbase.com/clients/c/mock/CouchbaseMock-LATEST.jar  
  
RUN pip install virtualenv  
  
WORKDIR /src  
  
RUN virtualenv /app && /app/bin/pip install couchbase numpy && cp -av
/usr/lib/libcouchbase.so* /app/lib/  
  
RUN tar czf /app.tgz /app && rm -rf /app  
  
ENTRYPOINT ["sh", "-c", "tar xzf /app.tgz -C / && /src/build.sh"]  

