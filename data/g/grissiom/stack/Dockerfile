FROM debian:latest  
  
MAINTAINER Grissiom <chaos.proton@gmail.com>  
  
ENV STACK_ROOT /stack-src  
  
COPY . /stack-src  
  
# rm the /var/lib/apt/lists/* to keep the image small.  
RUN apt-get update && apt-get install -y wget build-essential python autoconf
libtool && \  
rm -rf /var/lib/apt/lists/*  
  
# build custom llvm, installed to /usr/local  
RUN mkdir -p /build-llvm && cd /build-llvm && \  
wget http://llvm.org/releases/3.4/llvm-3.4.src.tar.gz \  
http://llvm.org/releases/3.4/clang-3.4.src.tar.gz \  
http://llvm.org/releases/3.4/clang-tools-extra-3.4.src.tar.gz \  
http://llvm.org/releases/3.4/compiler-rt-3.4.src.tar.gz && \  
tar xf llvm-3.4.src.tar.gz && \  
tar xf clang-3.4.src.tar.gz -C llvm-3.4/tools && \  
mv llvm-3.4/tools/clang-3.4 \  
llvm-3.4/tools/clang && \  
tar xf clang-tools-extra-3.4.src.tar.gz -C llvm-3.4/tools/clang/tools && \  
mv llvm-3.4/tools/clang/tools/clang-tools-extra-3.4 \  
llvm-3.4/tools/clang/tools/extra && \  
tar xf compiler-rt-3.4.src.tar.gz -C llvm-3.4/projects && \  
mv llvm-3.4/projects/compiler-rt-3.4 \  
llvm-3.4/projects/compiler-rt && \  
mkdir build && cd build && \  
../llvm-3.4/configure --enable-cxx11 --enable-targets=host \  
\--enable-bindings=none --enable-shared \  
\--disable-debug-symbols --enable-optimized \  
\--disable-docs && \  
make -j`cat /proc/cpuinfo | grep processor | wc -l` && \  
make install && \  
cd ~ && \  
rm -rf /build-llvm  
  
# build STACK  
RUN cd $STACK_ROOT && \  
autoreconf -fvi && \  
mkdir build && cd build && \  
../configure && make  
  
# use $STACK_ROOT/build/bin/stack/cc1 as CC  
CMD ["/bin/bash"]  

