FROM chcosta/dotnetcore:debian82_prereqs_2  
MAINTAINER "Chris Rummel <crummel@microsoft.com>"  
RUN echo deb http://apt.llvm.org/trusty/ llvm-toolchain-trusty-3.9 main >>
/etc/apt/sources.list  
RUN echo deb-src http://apt.llvm.org/trusty/ llvm-toolchain-trusty-3.9 main >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y curl  
RUN apt-get install -y clang-3.9  
RUN apt-get install -y llvm-3.9-dev  

