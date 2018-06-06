FROM ubuntu:14.04  
MAINTAINER "Joshua C. Randall" <jcrandall@alum.mit.edu>  
  
# Install prerequisite packages  
RUN \  
apt-get -q=2 update && \  
apt-get -q=2 upgrade && \  
apt-get install -qq -y \  
coreutils \  
autoconf \  
automake \  
libtool \  
make \  
pkg-config \  
git \  
libfuse-dev \  
zlib1g-dev  
  
# Install htslib from source  
RUN \  
mkdir -p /opt && \  
cd /opt && \  
git clone https://github.com/samtools/htslib.git && \  
cd htslib && \  
autoconf && \  
./configure && \  
make && \  
make install && \  
ldconfig  
  
# Build and install 13amp  
ADD . /opt/13amp  
WORKDIR /opt/13amp  
RUN \  
./autogen.sh && \  
mkdir build && \  
cd build && \  
../configure HTSLIB_LDFLAGS="$(pkg-config --libs htslib)" \  
HTSLIB_CFLAGS="$(pkg-config --cflags htslib)" \  
FUSE_LDFLAGS="$(pkg-config --libs fuse)" \  
FUSE_CFLAGS="$(pkg-config --cflags fuse)" && \  
make install  
  

