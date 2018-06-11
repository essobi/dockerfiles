# A Base Ubuntu image suitable for general development  
FROM debian:jessie-backports  
MAINTAINER Ash <tuxdude.io@gmail.com>  
  
# Base Packages  
# apt-utils build-essential supervisor locales git tar vim-nox wget curl
dnsutils  
# netcat traceroute net-tools nmap  
# Java  
# openjdk8-jdk  
# Install a base set of packages which we will use  
# The httpredir.debian.org source redirects requests to different mirrors and  
# few fail transiently causing the builds to fail  
# Instead use mirrors.kernel.org source  
RUN export DEBIAN_FRONTEND=noninteractive && \  
find /etc/apt/sources.list* -type f -exec sed -i
's/httpredir.debian.org/mirrors.kernel.org/g' {} + && \  
apt-get clean && \  
apt-get -y update && \  
apt-get -y --no-install-recommends install \  
apt-utils \  
build-essential \  
supervisor \  
locales \  
git \  
tar \  
vim-nox \  
wget \  
curl \  
dnsutils \  
netcat \  
traceroute \  
net-tools \  
nmap \  
openjdk-8-jdk \  
maven \  
autoconf \  
automake \  
libtool \  
cmake \  
zlib1g-dev \  
pkg-config \  
libssl-dev \  
snappy \  
libsnappy-dev \  
bzip2 \  
libbz2-dev \  
libjansson-dev \  
fuse \  
libfuse-dev \  
&& \  
/var/lib/dpkg/info/ca-certificates-java.postinst configure && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Set UTF-8 locale  
RUN export DEBIAN_FRONTEND=noninteractive && \  
dpkg-reconfigure locales && \  
locale-gen C.UTF-8 && \  
/usr/sbin/update-locale LANG=C.UTF-8  
ENV LC_ALL C.UTF-8  
  
# Set JAVA_HOME  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
# Set LD_LIBRARY_PATH  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/lib  
  
# Optional Golang  
#RUN export GOLANG_VERSION="1.5.1" && \  
# export GOLANG_DOWNLOAD_URL="https://golang.org/dl/go$GOLANG_VERSION.linux-
amd64.tar.gz" && \  
# export GOLANG_DOWNLOAD_SHA1="46eecd290d8803887dec718c691cc243f2175fe0" && \  
# curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \  
# && echo "$GOLANG_DOWNLOAD_SHA1 golang.tar.gz" | sha1sum -c - \  
# && tar -C /usr/local -xzf golang.tar.gz \  
# && rm golang.tar.gz  
# ENV PATH /usr/local/go/bin:$PATH  
  
# apt-get Hadoop dependencies  
# maven autoconf automake libtool cmake zlib1g-dev pkg-config libssl-dev  
# snappy libsnappy-dev bzip2 libbz2-dev libjansson-dev fuse libfuse-dev  
  
# Download, Build and Install Protobufs (Hadoop Dependency) and Hadoop  
RUN bash -c 'export PROTOBUF_VERSION=2.5.0 && \  
export HADOOP_VERSION=2.7.2 && \  
export
PROTOBUF_SRC_URL="https://github.com/google/protobuf/releases/download/v$PROTOBUF_VERSION/protobuf-$PROTOBUF_VERSION.tar.gz"
&& \  
export
HADOOP_SRC_URL="http://download.nextag.com/apache/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION-
src.tar.gz" && \  
export
HADOOP_SRC_ASC_URL="https://dist.apache.org/repos/dist/release/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION-
src.tar.gz.asc" && \  
export
HADOOP_SRC_KEYS_URL="https://dist.apache.org/repos/dist/release/hadoop/common/KEYS"
&& \  
export
HADOOP_SRC_SHA256="7d48e61b5464a76543fecf5655d06215cf8674d248b28bc74f613bc8aa047d33"
&& \  
export MAVEN_CACHE="/root/.m2" && \  
export HADOOP_TEMP="/var/tmp/hadoop" && \  
export PROTOBUF_BUILD_DIR="$HADOOP_TEMP/protobuf-build" && \  
export PROTOBUF_SRC_TARBALL="protobuf-$PROTOBUF_VERSION.tar.gz" && \  
export PROTOBUF_SRC_DIR="protobuf-$PROTOBUF_VERSION" && \  
export HADOOP_BUILD_DIR="$HADOOP_TEMP/hadoop-build" && \  
export HADOOP_SRC_TARBALL="hadoop-$HADOOP_VERSION-src.tar.gz" && \  
export HADOOP_SRC_ASC="hadoop-$HADOOP_VERSION-src.tar.gz.asc" && \  
export HADOOP_SRC_DIR="hadoop-$HADOOP_VERSION-src" && \  
export HADOOP_DIST_TARBALL="$HADOOP_BUILD_DIR/$HADOOP_SRC_DIR/hadoop-
dist/target/hadoop-$HADOOP_VERSION.tar.gz" && \  
export HADOOP_DIST_EXTRACT_DIR="/opt" && \  
export HADOOP_DIST_TARGET_DIR="/opt/hadoop-$HADOOP_VERSION" && \  
export HADOOP_DIST_SYMLINK_DIR="/opt/hadoop" && \  
mkdir -p $PROTOBUF_BUILD_DIR && \  
pushd $PROTOBUF_BUILD_DIR && \  
wget $PROTOBUF_SRC_URL && \  
tar xvf $PROTOBUF_SRC_TARBALL && \  
pushd $PROTOBUF_SRC_DIR && \  
./configure && \  
make && \  
make check && \  
make install && \  
popd && \  
popd && \  
mkdir -p $HADOOP_BUILD_DIR && \  
pushd $HADOOP_BUILD_DIR && \  
wget $HADOOP_SRC_URL && \  
echo "$HADOOP_SRC_SHA256 $HADOOP_SRC_TARBALL" | shasum -a 256 -c && \  
wget $HADOOP_SRC_KEYS_URL && \  
wget $HADOOP_SRC_ASC_URL && \  
gpg --import KEYS && \  
gpg --verify $HADOOP_SRC_ASC && \  
tar xvf $HADOOP_SRC_TARBALL && \  
pushd $HADOOP_SRC_DIR && \  
mvn clean && \  
mvn package -Pdist,native -Dtar -Drequire.snappy -Drequire.openssl -DskipTests
&& \  
popd && \  
popd && \  
mkdir -p $HADOOP_DIST_EXTRACT_DIR && \  
pushd $HADOOP_DIST_EXTRACT_DIR && \  
tar xvf $HADOOP_DIST_TARBALL && \  
ln -sf $HADOOP_DIST_TARGET_DIR $HADOOP_DIST_SYMLINK_DIR && \  
popd && \  
rm -rf $PROTOBUF_BUILD_DIR $HADOOP_BUILD_DIR $HADOOP_TEMP $MAVEN_CACHE'  
  
# Setup HADOOP_PREFIX and add hadoop binaries to PATH  
ENV HADOOP_PREFIX /opt/hadoop  
ENV PATH $PATH:$HADOOP_PREFIX/bin  
  
CMD ["/bin/bash"]  

