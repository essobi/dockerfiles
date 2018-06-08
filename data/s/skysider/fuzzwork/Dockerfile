FROM phusion/baseimage:latest  
  
LABEL maintainer="junchaoluan@gmail.com"  
  
RUN apt-get -y update && apt-get install -y wget  
  
RUN wget -O- https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - && \  
apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-6.0
main" && \  
apt-get update && apt-get install -y clang-6.0 && \  
rm -rf /var/lib/apt/lists/* && \  
update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-6.0
1000 && \  
update-alternatives --install /usr/bin/clang clang /usr/bin/clang-6.0 1000  
WORKDIR /work  

