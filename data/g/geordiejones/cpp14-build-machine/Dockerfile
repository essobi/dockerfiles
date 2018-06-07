FROM geordiejones/basic_debian_dev_machine  
MAINTAINER Gareth Jones (joneszone1975@gmail.com)  
  
WORKDIR /usr/src  
RUN apt-get update && apt-get install -y apt-utils wget  
RUN echo "deb http://llvm.org/apt/jessie/ llvm-toolchain-jessie main" >>
/etc/apt/sources.list  
RUN echo "deb-src http://llvm.org/apt/jessie/ llvm-toolchain-jessie main" >>
/etc/apt/sources.list  
RUN wget -O - http://llvm.org/apt/llvm-snapshot.gpg.key | apt-key add -  
  
RUN apt-get update  
RUN apt-get install -y clang-5.0 clang-5.0-doc libclang-common-5.0-dev  
RUN apt-get install -y libclang-5.0-dev libclang1-5.0 libclang1-5.0-dbg
libllvm-5.0-ocaml-dev  
RUN apt-get install -y libllvm5.0 libllvm5.0-dbg lldb-5.0 llvm-5.0
llvm-5.0-dev llvm-5.0-doc  
RUN apt-get install -y llvm-5.0-examples llvm-5.0-runtime clang-format-5.0
python-clang-5.0  
RUN apt-get install -y liblldb-5.0-dbg lld-5.0 libfuzzer-5.0-dev  
  
RUN git clone https://github.com/Microsoft/GSL.git  
  
RUN update-alternatives --install /usr/bin/clang clang /usr/bin/clang-5.0 100  
RUN update-alternatives --install /usr/bin/clang++ clang++
/usr/bin/clang++-5.0 100  
RUN update-alternatives --install /usr/bin/cc cc /usr/bin/clang 100  
RUN update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++ 100  

