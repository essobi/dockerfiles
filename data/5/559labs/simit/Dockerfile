FROM buildpack-deps:jessie  
  
MAINTAINER Andrew Marconi <andrew@559labs.com>  
  
ENV LLVM_CONFIG /simit/Release+Asserts/bin/llvm-config  
  
RUN apt-get update; \  
apt-get -y upgrade  
  
RUN apt-get -y install cmake git subversion  
  
RUN mkdir /simit && cd /simit && \  
svn co https://llvm.org/svn/llvm-project/llvm/branches/release_36/ llvm-3.6.1
&& \  
cd llvm-3.6.1 && \  
./configure --disable-terminfo --enable-optimized --enable-assertions
--enable-targets=x86 && \  
make -j8  

