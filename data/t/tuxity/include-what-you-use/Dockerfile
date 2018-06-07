FROM tuxity/llvm:4.0  
LABEL maintainer="kevin.darcel@gmail.com"  
  
ENV LLVM_VERSION 4.0  
RUN set -ex; \  
apt-get update; \  
apt-get install -y \  
cmake \  
libclang-${LLVM_VERSION}-dev \  
; \  
rm -rf /var/lib/apt/lists/*  
  
RUN set -ex; \  
git clone https://github.com/include-what-you-use/include-what-you-use.git &&
cd include-what-you-use; \  
git checkout clang_${LLVM_VERSION}; \  
mkdir build && cd build; \  
cmake \  
-G "Unix Makefiles" \  
-DIWYU_LLVM_ROOT_PATH=/usr/lib/llvm-${LLVM_VERSION} \  
.. \  
; \  
make && make install  

