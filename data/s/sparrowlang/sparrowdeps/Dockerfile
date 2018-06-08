FROM ubuntu:16.04  
# Common packages  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
RUN apt-get install -y build-essential  
RUN apt-get install -y zlib1g-dev  
  
RUN apt-get install -y llvm-5.0-dev llvm-5.0-dev libllvm5.0 llvm-5.0  
RUN apt-get install -y clang-5.0  
  
# Boost 1.58  
RUN apt-get install -y libboost-all-dev  
  
# Make clang the default compiler  
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/clang-5.0 60
--slave /usr/bin/g++ g++ /usr/bin/clang++-5.0  
  
RUN update-alternatives --config gcc  
  
#install latest cmake  
ADD https://cmake.org/files/v3.10/cmake-3.10.1-Linux-x86_64.sh
/cmake-3.10.1-Linux-x86_64.sh  
RUN sh /cmake-3.10.1-Linux-x86_64.sh --skip-license  
RUN rm -rf /cmake-3.10.1-Linux-x86_64.sh  
  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

