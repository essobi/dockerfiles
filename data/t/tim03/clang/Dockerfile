FROM tim03/cmake  
LABEL maintainer Chen, Wenli <chenwenli@chenwenli.com＞  
  
WORKDIR /usr/local/src  
RUN \  
svn co http://llvm.org/svn/llvm-project/llvm/trunk llvm  
RUN \  
cd llvm/tools && \  
svn co http://llvm.org/svn/llvm-project/cfe/trunk clang && \  
cd ../..  
RUN \  
mkdir build && \  
cd build && \  
cmake -G "Unix Makefiles" ../llvm && \  
make  

