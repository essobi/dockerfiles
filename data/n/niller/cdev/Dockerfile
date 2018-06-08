FROM buildpack-deps:jessie-curl  
  
RUN curl http://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \  
&& printf "deb http://apt.llvm.org/jessie/ llvm-toolchain-jessie-4.0 main
\ndeb-src http://apt.llvm.org/jessie/ llvm-toolchain-jessie-4.0 main \n" >
/etc/apt/sources.list.d/llvm.list  
  
RUN apt-get update -y  
RUN apt-get install -y --no-install-recommends \  
make \  
lld-4.0 \  
lldb-4.0 \  
clang-4.0 \  
clang-format-4.0 \  
splint  
  

