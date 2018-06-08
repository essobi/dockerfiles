FROM golang:1.7.1-alpine  
  
RUN \  
apk add --no-cache bzip2-dev coreutils curl gcc g++ linux-headers make musl-
dev perl snappy-dev zlib-dev  
  
RUN mkdir /src \  
&& (cd /src; curl -L
https://github.com/facebook/rocksdb/archive/v4.11.2.tar.gz | tar xzf -) \  
&& (cd /src/rocksdb-4.11.2; INSTALL_PATH=/usr make install-shared) \  
&& rm -r /src  

