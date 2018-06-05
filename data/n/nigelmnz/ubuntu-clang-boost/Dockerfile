FROM ubuntu:bionic  
  
# Install required dependencies  
RUN apt-get update && apt-get -y install wget software-properties-common g++
git curl unzip python-dev  
  
# Install Clang  
RUN wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add  
RUN apt-add-repository "deb http://apt.llvm.org/bionic/ llvm-toolchain-
bionic-6.0 main"  
RUN apt-get update && apt-get install -y clang-6.0  
RUN update-alternatives --install /usr/bin/clang++ clang++
/usr/bin/clang++-6.0 1000  
  
# Install CMake  
RUN apt-get install -y cmake  
  
WORKDIR /app  
  
### Install Boost  
RUN wget -c
'http://sourceforge.net/projects/boost/files/boost/1.67.0/boost_1_67_0.tar.bz2/download'  
RUN tar --bzip -xf download  
RUN cd boost_1_67_0 && ./bootstrap.sh && ./b2 install --without-log -j 8  
RUN rm download && rm -rf boost_1_67_0  
  
# Set Clang as the default cpp compiler  
RUN export CXX=/usr/bin/clang++

