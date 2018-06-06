FROM ubuntu:rolling  
  
RUN apt-get update && apt-get dist-upgrade -y && apt-get install -y wget
clang-5.0 cmake git curl  
  
RUN cd /tmp && \  
git clone \--depth 1 https://github.com/llvm-mirror/llvm && \  
cd /tmp/llvm/projects && \  
git clone \--depth 1 https://github.com/llvm-mirror/libcxx.git && \  
git clone \--depth 1 https://github.com/llvm-mirror/libcxxabi.git && \  
cd /tmp/llvm && mkdir build && cd build && \  
cmake -DCMAKE_CXX_COMPILER=/usr/bin/clang++-5.0 .. && \  
make -j cxx && \  
make install-cxx install-cxxabi && \  
cp -v /tmp/llvm/projects/libcxxabi/include/* /usr/local/include/c++/v1/ && \  
cd /tmp && \  
rm -rf llvm  
  
RUN echo /usr/local/lib/ > /etc/ld.so.conf.d/local.conf && ldconfig  

