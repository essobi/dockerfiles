# RocksDB with Java bindings on CentOS 7  
  
# #####################################  
# BUILD #  
# #####################################  
FROM centos:7 as builder  
  
ARG ROCKSDB_VERSION=5.9.2  
  
# Install build dependencies  
RUN rm -rf /var/cache/yum \  
&& yum install -y epel-release \  
&& yum update -y \  
&& yum install -y \  
bzip2 \  
bzip2-devel \  
gcc-c++ \  
gflags \  
git \  
java-1.8.0-openjdk \  
java-1.8.0-openjdk-devel \  
libzstd \  
make \  
snappy \  
snappy-devel \  
which \  
zlib \  
zlib-devel \  
zstd \  
&& rm -rf /var/cache/yum  
  
# Download, build, and install RocksDB and the Java bindings  
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0  
WORKDIR /usr/local/src/rocksdb  
RUN git clone --branch "v${ROCKSDB_VERSION}" \  
\--depth 1 https://github.com/facebook/rocksdb.git . \  
&& export DEBUG_LEVEL=0 \  
&& export INSTALL_PATH=/build/usr/local \  
&& make clean static_lib install-shared \  
&& make jclean rocksdbjava \  
&& cd java/target \  
&& ln -s rocksdbjni-*.jar rocksdbjni.jar \  
&& mkdir -p /build/usr/lib/java/ && cp rocksdbjni-*.jar /build/usr/lib/java/ \  
&& mkdir -p /build/usr/local/lib64/ && cp librocksdbjni-*.so
/build/usr/local/lib64/ \  
&& cd / && rm -rf /usr/local/src/rocksdb  
  
# #####################################  
# RUN #  
# #####################################  
FROM centos:7  
  
# Install runtime dependencies  
RUN rm -rf /var/cache/yum \  
&& yum install -y epel-release \  
&& yum update -y \  
&& yum install -y \  
bzip2 \  
java-1.8.0-openjdk \  
snappy \  
which \  
zlib \  
zstd \  
&& rm -rf /var/cache/yum  
  
# Copy build output and startup script  
WORKDIR /usr/lib/java  
COPY --from=builder /build/ /  
COPY scripts/docker-entrypoint.sh /  
  
# Default to intercepting any java command and injecting the RocksDB  
# java bindings jar into the classpath.  
ENTRYPOINT ["/docker-entrypoint.sh"]  

