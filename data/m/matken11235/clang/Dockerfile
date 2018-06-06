FROM ubuntu:16.04  
  
ENV DEBIAN_FRONTEND noninteractive  
  
  
# Install cmake-3.11.3  
RUN apt-get update -qq \  
&& apt-get install -y -qq wget libcurl4-gnutls-dev gcc build-essential \  
&& wget -q https://cmake.org/files/v3.11/cmake-3.11.3.tar.gz \  
&& tar -xzvf cmake-3.11.3.tar.gz \  
&& cd cmake-3.11.3 \  
&& ./bootstrap \  
&& make -j4 \  
&& make install  
  
# Install boost-1.67.0  
RUN apt-get update -qq \  
&& apt-get install -y -qq curl \  
&& curl -fsSLO
https://dl.bintray.com/boostorg/release/1.67.0/source/boost_1_67_0.tar.bz2 \  
&& tar -jxvf boost_1_67_0.tar.bz2 \  
&& cd boost_1_67_0 \  
&& ./bootstrap.sh \--prefix=/usr \  
&& ./b2 stage threading=multi link=shared \  
&& ./b2 install threading=multi link=shared  
  
  
# Install clang-5.0  
RUN apt-get update -qq \  
&& apt-get install -y -qq wget apt-file \  
&& apt-file update \  
&& apt-get install -y -qq software-properties-common \  
&& wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add \- \  
&& apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-
xenial-5.0 main" \  
&& apt-get update -qq \  
&& apt-get install -y -qq clang-5.0  
  
# Link clang  
RUN update-alternatives --install /usr/bin/clang clang /usr/bin/clang-5.0 999
\  
&& update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-5.0
999 \  
&& update-alternatives --install /usr/bin/cc cc /usr/bin/clang-5.0 999 \  
&& update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++-5.0 999  
  
ENV CC="clang" CXX="clang++" CMAKE_C_COMPILER="clang"
CMAKE_CXX_COMPILER="clang++"  

