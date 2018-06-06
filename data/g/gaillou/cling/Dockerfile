FROM debian:sid  
MAINTAINER Antoine Gaillard <antoine.gaillard13@gmail.com>  
  
RUN apt-get update && apt-get install -y libc++-dev libc6-dev \--no-install-
recommends \  
&& rm -rf /var/lib/apt/lists/*  
RUN buildDeps=' \  
clang-3.7 \  
git \  
libc++abi-dev \  
libffi-dev \  
make \  
pkg-config \  
python \  
' \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir /src \  
&& cd /src \  
&& git clone \--depth 1 http://root.cern.ch/git/llvm.git \--branch cling-
patches \  
&& git clone \--depth 1 http://root.cern.ch/git/clang.git \--branch cling-
patches \  
&& git clone \--depth 1 http://root.cern.ch/git/cling.git \--branch master \  
&& ln -s /src/clang llvm/tools \  
&& ln -s /src/cling llvm/tools \  
&& mkdir build \  
&& cd build \  
&& CXX=/usr/bin/clang++-3.7 CC=/usr/bin/clang-3.7
CXXFLAGS=-I/usr/include/libcxxabi/ ../llvm/configure \  
\--prefix="/usr/local" \  
\--enable-optimized \  
\--enable-cxx1y \  
\--enable-libcpp \  
\--enable-libffi \  
\--enable-targets=x86_64 \  
\--disable-docs \  
&& make -j $(nproc) \  
&& make -C tools/clang install \  
&& make -C tools/cling install \  
&& rm -rf /src \  
&& apt-get purge -y $buildDeps \--auto-remove \  
&& update-alternatives \--install /usr/bin/clang++-3.7 clang++-3.7
/usr/local/bin/clang++ 1  
  
ENTRYPOINT [ "cling" ]  

