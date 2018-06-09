# Build as  
#  
# $ docker build -t mesos-tidy -f mesos-tidy.Dockerfile .  
FROM debian:jessie  
MAINTAINER The Apache Mesos Developers <dev@mesos.apache.org>  
  
# Build Mesos-flavored `clang-tidy`.  
RUN apt-get update  
RUN apt-get install -qy --no-install-recommends \  
build-essential \  
cmake \  
git \  
ninja-build \  
python-dev &&\  
apt-get clean  
  
WORKDIR /tmp/build_clang  
  
RUN \  
git clone \--depth 1 -b release_38 http://llvm.org/git/llvm /tmp/llvm && \  
git clone \--depth 1 -b release_38 http://llvm.org/git/clang
/tmp/llvm/tools/clang && \  
\  
git config --global http.sslVerify false && \  
git clone \--depth 1 -b mesos_38 http://github.com/mesos/clang-tools-extra.git
/tmp/llvm/tools/clang/tools/extra && \  
rm ~/.gitconfig && \  
\  
cmake /tmp/llvm -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/opt/ && \  
make -j`nproc` install && \  
\  
cd / && \  
rm -rf /tmp/llvm && \  
rm -rf /tmp/build_clang  
  
ENV PATH /opt/bin:$PATH  
  
# Install Mesos dependencies  
RUN apt-get install -qy \  
autoconf \  
bear \  
jq \  
libapr1-dev \  
libcurl4-nss-dev \  
libev-dev \  
libevent-dev \  
libsasl2-dev \  
libsasl2-modules \  
libsvn-dev \  
libtool \  
maven \  
openjdk-7-jdk \  
python-dev \  
zlib1g-dev && \  
apt-get clean  
  
# Install parallel for clang-tidy invocation.  
RUN apt-get install -qy \  
parallel  
  
# Wire up the script which performs the actual work.  
WORKDIR /BUILD  
ADD ["entrypoint.sh", "entrypoint.sh"]  
CMD exec ./entrypoint.sh  

