FROM ubuntu:16.04  
MAINTAINER Carlos O'Ryan <coryan@users.noreply.github.com>  
  
RUN apt-get update && apt-get install -y \  
automake \  
clang \  
clang-format \  
cmake \  
doxygen \  
findutils \  
g++ \  
gcc \  
git \  
lcov \  
libboost-all-dev \  
libbz2-dev \  
libclang-dev \  
libclfft-dev \  
libfftw3-dev \  
libyaml-cpp-dev \  
llvm \  
lshw \  
make \  
ocl-icd-libopencl1 \  
ocl-icd-opencl-dev \  
opencl-headers \  
pkg-config \  
sudo \  
tar \  
time \  
wget \  
xz-utils \  
zlib1g-dev  
  
WORKDIR /var/tmp/install-autoconf-archive  
RUN wget -q http://ftpmirror.gnu.org/autoconf-archive/autoconf-
archive-2016.09.16.tar.xz  
RUN tar -xf autoconf-archive-2016.09.16.tar.xz  
RUN cd autoconf-archive-2016.09.16 && ./configure --prefix=/usr && make &&
make install  
  
WORKDIR /var/tmp/build-skye  
RUN wget -q
https://github.com/coryan/Skye/releases/download/v0.3.2/skye-0.3.2.tar.gz  
RUN tar -xf skye-0.3.2.tar.gz  
RUN cd skye-0.3.2 && \  
CXX=g++ CC=gcc CPPFLAGS=-D_GLIBCXX_USE_CXX11_ABI=1 ./configure --with-boost-
libdir=/usr/lib/x86_64-linux-gnu && \  
make check && \  
make install  
  
WORKDIR /var/tmp/build-pocl  
RUN wget -q http://portablecl.org/downloads/pocl-0.13.tar.gz  
RUN tar -zxf pocl-0.13.tar.gz  
RUN cd pocl-0.13 && ./configure && make && make install  
  
WORKDIR /var/tmp/build-boost-compute  
RUN wget -q https://github.com/boostorg/compute/archive/boost-1.62.0.tar.gz  
RUN tar -xf boost-1.62.0.tar.gz  
WORKDIR /var/tmp/build-boost-compute/compute-boost-1.62.0  
RUN cmake . && make && make DESTDIR=staging install  
RUN cp -r staging/usr/local/include/compute/boost/compute.hpp
/usr/include/boost/  
RUN cp -r staging/usr/local/include/compute/boost/compute/ /usr/include/boost/  
  
WORKDIR /root  
RUN /bin/rm -fr /var/tmp/build-skye /var/tmp/install-autoconf-archive  
RUN /bin/rm -fr /var/tmp/build-boost-compute /var/tmp/build-pocl  
  
COPY test-image.sh /root/test-image.sh  
CMD ["bash", "/root/test-image.sh"]  

