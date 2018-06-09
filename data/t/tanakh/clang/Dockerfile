FROM centos:7.2.1511  
MAINTAINER Hideyuki Tanaka  
  
RUN yum install -y file gcc gcc-c++ make  
  
RUN curl -O https://cmake.org/files/v3.6/cmake-3.6.2.tar.gz; \  
tar -xf cmake-3.6.2.tar.gz; \  
cd cmake-3.6.2; ./configure; make -j8; make install; cd ..; \  
curl -O http://llvm.org/releases/3.9.0/llvm-3.9.0.src.tar.xz; \  
curl -O http://llvm.org/releases/3.9.0/cfe-3.9.0.src.tar.xz; \  
tar -xf llvm-3.9.0.src.tar.xz; \  
tar -xf cfe-3.9.0.src.tar.xz; \  
mv cfe-3.9.0.src llvm-3.9.0.src/tools/; \  
mkdir llvm-3.9.0.src/build; \  
cd llvm-3.9.0.src/build; cmake .. -DCMAKE_BUILD_TYPE=Release; make -j8; make
install; cd .. \  
rm -rf *.tar.gz *.tar.xz cmake-3.6.2 llvm-3.9.0.src  

