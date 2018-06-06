FROM arnow117/ubuntu_base:latest  
  
MAINTAINER arnow117 "arnow117@gmail.com"  
ENV TOOLS_PATH /root/Tools  
ENV WORK_PATH /root/Workspace  
ENV LLVM_PATH /root/Tools/LLVM  
ENV AFL_PATH /root/Tools/AFL  
  
# install LibFuzzer  
RUN apt-get update -y && apt-get install -y build-essential make cmake ninja-
build  
RUN mkdir $LLVM_PATH  
WORKDIR $LLVM_PATH  
RUN mkdir $LLVM_PATH/src $LLVM_PATH/work  
RUN cd $LLVM_PATH/src && git clone \--depth 1 http://llvm.org/git/llvm.git  
RUN cd $LLVM_PATH/src/llvm/tools && git clone \--depth 1
http://llvm.org/git/clang.git  
RUN cd $LLVM_PATH/src/llvm/projects && git clone \--depth 1
http://llvm.org/git/compiler-rt.git  
RUN cd $LLVM_PATH/src/llvm/projects && git clone \--depth 1
http://llvm.org/git/libcxx.git  
RUN cd $LLVM_PATH/src/llvm/projects && git clone \--depth 1
http://llvm.org/git/libcxxabi.git  
RUN cd $LLVM_PATH/src/llvm/projects && git clone \--depth 1
http://llvm.org/git/lld.git  
WORKDIR $LLVM_PATH  
  
# install from clang src  
WORKDIR $LLVM_PATH  
RUN mkdir -p $LLVM_PATH/work/llvm && cd $LLVM_PATH/work/llvm  
RUN cmake -G "Ninja" -DCMAKE_BUILD_TYPE=Release -DLIBCXX_ENABLE_SHARED=OFF
-DLIBCXX_ENABLE_STATIC_ABI_LIBRARY=ON $LLVM_PATH/src/llvm

