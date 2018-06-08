FROM ubuntu:latest  
  
ARG cmake_source=https://cmake.org/files/v3.10/cmake-3.10.2.tar.gz  
ARG
boost_source=https://dl.bintray.com/boostorg/release/1.66.0/source/boost_1_66_0.tar.gz  
ARG poco_source=https://pocoproject.org/releases/poco-1.8.1/poco-1.8.1.tar.gz  
  
RUN apt -y update && \  
apt -y dist-upgrade && \  
# Install build essential (use gcc-7)  
apt -y install build-essential software-properties-common && \  
add-apt-repository ppa:ubuntu-toolchain-r/test -y && \  
apt -y update && \  
apt -y install gcc-7 g++-7 && \  
update-alternatives \--install /usr/bin/gcc gcc /usr/bin/gcc-7 60 \--slave
/usr/bin/g++ g++ /usr/bin/g++-7 && \  
# Install additional build/helper tools  
apt -y install libssl-dev libtool autoconf automake curl git unzip && \  
# Build & install cmake  
mkdir /build && cd /build && \  
curl $cmake_source \--output cmake.tar.gz && \  
mkdir cmake && tar -xzf cmake.tar.gz -C cmake \--strip-components 1 && cd
cmake && \  
./bootstrap && make && make install && \  
cd .. && rm -r cmake cmake.tar.gz && \  
# Build & install boost  
curl -L $boost_source \--output boost.tar.gz && \  
mkdir boost && tar -xzf boost.tar.gz -C boost \--strip-components 1 && cd
boost && \  
./bootstrap.sh \--prefix=/usr/local/ \--with-
libraries=system,program_options,log,filesystem,thread,random && ./b2 install
&& \  
cd .. && rm -r boost boost.tar.gz && \  
# Build & install poco  
curl $poco_source \--output poco.tar.gz && \  
mkdir poco && tar -xzf poco.tar.gz -C poco \--strip-components 1 && cd poco &&
\  
cmake . -DCMAKE_BUILD_TYPE=Release && \  
make && make install && \  
cd .. && rm -r poco poco.tar.gz && \  
# Build & install gtest  
git clone https://github.com/google/googletest.git && cd googletest && \  
cmake . -DCMAKE_BUILD_TYPE=Release && \  
make && make install && \  
cd .. && rm -r googletest && \  
# Cleanup  
cd / && rm -r /build && \  
apt -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
# Refresh shared library cache  
ldconfig  
  

