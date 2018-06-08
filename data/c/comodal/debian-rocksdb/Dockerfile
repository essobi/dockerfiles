FROM debian:sid  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
ARG ROCKSDB_REPO='https://github.com/facebook/rocksdb.git'  
ARG ROCKSDB_VERSION='5.2.1'  
ARG ROCKSDB_TAG="rocksdb-${ROCKSDB_VERSION}"  
  
LABEL org.label-schema.build-date=$BUILD_DATE\  
org.label-schema.vcs-url="https://github.com/comodal/debian-rocksdb.git"\  
org.label-schema.vcs-ref=$VCS_REF\  
org.label-schema.name="RocksDB on Debian"\  
org.label-schema.description="Base image with RocksDB on Debian Linux."\  
org.label-schema.schema-version="1.0.0-rc.1"  
  
RUN set -x\  
&& echo 'deb http://deb.debian.org/debian experimental main' >
/etc/apt/sources.list.d/experimental.list\  
&& apt-get update && apt-get install -y\  
build-essential\  
git\  
libbz2-dev\  
libgflags-dev\  
libjemalloc-dev\  
libsnappy-dev\  
libtbb-dev\  
libzstd-dev\  
zlib1g-dev\  
&& git clone $ROCKSDB_REPO /tmp/rocksdb\  
&& cd /tmp/rocksdb\  
&& git checkout tags/${ROCKSDB_TAG}\  
&& make -j$(nproc) shared_lib\  
&& make install-shared\  
&& strip /usr/local/lib/librocksdb.so.${ROCKSDB_VERSION}\  
&& rm -rf /tmp/rocksdb\  
&& apt-get purge -y\  
build-essential\  
git\  
libbz2-dev\  
libgflags-dev\  
libjemalloc-dev\  
libsnappy-dev\  
libtbb-dev\  
libzstd-dev\  
zlib1g-dev\  
&& apt-get install -y\  
libbz2-1.0\  
libjemalloc1\  
libsnappy1v5\  
libtbb2\  
libzstd1\  
zlib1g  

