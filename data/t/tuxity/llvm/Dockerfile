FROM buildpack-deps:stretch  
LABEL maintainer="kevin.darcel@gmail.com"  
  
ENV LLVM_VERSION 4.0  
RUN set -ex; \  
wget -qO - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -; \  
echo "deb http://apt.llvm.org/stretch/ llvm-toolchain-stretch-${LLVM_VERSION}
main" > /etc/apt/sources.list.d/llvm.list;  
  
RUN set -ex; \  
apt-get update; \  
apt-get install -y \  
clang-${LLVM_VERSION} \  
; \  
rm -rf /var/lib/apt/lists/*  
  
RUN set -ex; \  
update-alternatives --install /usr/bin/clang clang
/usr/bin/clang-${LLVM_VERSION} 999; \  
update-alternatives --install /usr/bin/clang++ clang++
/usr/bin/clang++-${LLVM_VERSION} 999  
  
ENV CC clang  
ENV CXX clang++  

