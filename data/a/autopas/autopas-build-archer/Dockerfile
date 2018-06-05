FROM ubuntu:16.04  
# install base requirements  
RUN true \  
&& apt-get -qq update \  
&& apt-get -qq install -y --no-install-recommends \  
build-essential \  
cmake \  
ninja-build \  
wget \  
gdb \  
git \  
&& rm -rf /var/lib/apt/lists/*  
  
# add llvm repository  
#RUN echo "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-5.0 main\n\  
#deb-src http://apt.llvm.org/xenial/ llvm-toolchain-xenial-5.0 main" >
/etc/apt/sources.list.d/llvm.list  
# add llvm repo key  
#RUN wget --no-check-certificate -O - https://apt.llvm.org/llvm-
snapshot.gpg.key|apt-key add -  
ENV CLANGVERSION 4.0  
# install llvm  
RUN true \  
&& apt-get -qq update \  
&& apt-get -qq install -y --no-install-recommends \  
clang-${CLANGVERSION} \  
lldb-${CLANGVERSION} \  
&& rm -rf /var/lib/apt/lists/*  
  
# generate links to clang  
RUN ln -s /usr/bin/clang-${CLANGVERSION} /usr/bin/clang  
RUN ln -s /usr/bin/clang++-${CLANGVERSION} /usr/bin/clang++  
RUN ln -s /usr/bin/llvm-config-${CLANGVERSION} /usr/bin/llvm-config  
  
# build everything in /ArcherBuild  
ENV ARCHER_BUILD /ArcherBuild  
RUN mkdir $ARCHER_BUILD  
WORKDIR $ARCHER_BUILD  
  
# disable git https check  
RUN git config --global http.sslVerify false  
  
#get, build and install openmp runtime  
RUN git clone https://github.com/llvm-mirror/openmp.git openmp  
ENV OPENMP_INSTALL /usr  
WORKDIR openmp  
RUN mkdir build  
WORKDIR build  
RUN cmake -G Ninja \  
-D CMAKE_C_COMPILER=clang \  
-D CMAKE_CXX_COMPILER=clang++ \  
-D CMAKE_BUILD_TYPE=DEBUG \  
-D CMAKE_INSTALL_PREFIX:PATH=$OPENMP_INSTALL \  
-D LIBOMP_OMPT_SUPPORT=on \  
-D LIBOMP_OMPT_BLAME=on \  
-D LIBOMP_OMPT_TRACE=on \  
..  
RUN ninja  
RUN ninja install  
  
# get, build and install archer v1.0.0  
WORKDIR $ARCHER_BUILD  
RUN git clone https://github.com/PRUNERS/archer.git archer  
ENV ARCHER_INSTALL /usr  
WORKDIR archer  
RUN git checkout de89c1e  
RUN mkdir build  
WORKDIR build  
RUN cmake -G Ninja \  
-D CMAKE_C_COMPILER=clang \  
-D CMAKE_CXX_COMPILER=clang++ \  
-D CMAKE_INSTALL_PREFIX:PATH=${ARCHER_INSTALL} \  
-D OMP_PREFIX:PATH=$OPENMP_INSTALL \  
..  
RUN ninja  
RUN ninja install  
  

