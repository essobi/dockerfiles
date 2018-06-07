FROM ubuntu:14.04  
RUN apt-get -y update  
RUN apt-get install -y clang-3.4 llvm-3.4  
RUN apt-get install -y emscripten  
  
ENV LLVM /usr/lib/llvm-3.4/bin  
VOLUME ["/build"]  
WORKDIR /build  
  

