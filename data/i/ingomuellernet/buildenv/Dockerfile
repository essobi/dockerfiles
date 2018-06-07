FROM ingomuellernet/buildenv:gold-builder-stage2 as gold-builder  
FROM ingomuellernet/cppcheck as cppcheck-builder  
  
FROM ubuntu:xenial  
MAINTAINER Ingo Müller <ingo.mueller@inf.ethz.ch>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
build-essential \  
clang-3.5 \  
clang-format-3.5 \  
clang-modernize-3.5 \  
clang-3.6 \  
clang-format-3.6 \  
clang-modernize-3.6 \  
clang-tidy-3.6 \  
clang-3.7 \  
clang-format-3.7 \  
clang-modernize-3.7 \  
clang-tidy-3.7 \  
clang-3.8 \  
clang-format-3.8 \  
clang-tidy-3.8 \  
cmake \  
gcc-4.7 \  
g++-4.7 \  
gcc-4.8 \  
g++-4.8 \  
gcc-4.9 \  
g++-4.9 \  
gcc-5 \  
g++-5 \  
git \  
libboost-all-dev \  
wget \  
xz-utils \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /opt/clang+llvm-3.9.1/ && \  
cd /opt/clang+llvm-3.9.1/ && \  
wget http://releases.llvm.org/3.9.1/clang+llvm-3.9.1-x86_64-linux-gnu-
ubuntu-16.04.tar.xz -O - \  
| tar -x -I xz --strip-components=1 && \  
for file in bin/*; \  
do \  
ln -s $PWD/$file /usr/bin/$(basename $file)-3.9; \  
done  
  
RUN mkdir /opt/clang+llvm-4.0.0/ && \  
cd /opt/clang+llvm-4.0.0/ && \  
wget http://releases.llvm.org/4.0.0/clang+llvm-4.0.0-x86_64-linux-gnu-
ubuntu-16.04.tar.xz -O - \  
| tar -x -I xz --strip-components=1 && \  
for file in bin/*; \  
do \  
ln -s $PWD/$file /usr/bin/$(basename $file)-4.0; \  
done  
  
RUN mkdir /opt/clang+llvm-5.0.0/ && \  
cd /opt/clang+llvm-5.0.0/ && \  
wget
http://releases.llvm.org/5.0.0/clang+llvm-5.0.0-linux-x86_64-ubuntu16.04.tar.xz
-O - \  
| tar -x -I xz --strip-components=1 && \  
for file in bin/*; \  
do \  
ln -s $PWD/$file /usr/bin/$(basename $file)-5.0; \  
done  
  
# Copy llvm gold plugin over from builder  
COPY \--from=gold-builder /tmp/llvm-5.0.0.src/build/lib/LLVMgold.so
/opt/clang+llvm-5.0.0/lib  
  
RUN mkdir /opt/cmake-3.6.3/ && \  
cd /opt/cmake-3.6.3/ && \  
wget https://cmake.org/files/v3.6/cmake-3.6.3-Linux-x86_64.tar.gz -O - \  
| tar -xz --strip-components=1 && \  
for file in bin/*; \  
do \  
ln -s $PWD/$file /usr/bin/$(basename $file)-3.6; \  
done  
  
RUN mkdir /opt/cmake-3.7.2/ && \  
cd /opt/cmake-3.7.2/ && \  
wget https://cmake.org/files/v3.7/cmake-3.7.2-Linux-x86_64.tar.gz -O - \  
| tar -xz --strip-components=1 && \  
for file in bin/*; \  
do \  
ln -s $PWD/$file /usr/bin/$(basename $file)-3.7; \  
done  
  
RUN mkdir /opt/cmake-3.8.2/ && \  
cd /opt/cmake-3.8.2/ && \  
wget https://cmake.org/files/v3.8/cmake-3.8.2-Linux-x86_64.tar.gz -O - \  
| tar -xz --strip-components=1 && \  
for file in bin/*; \  
do \  
ln -s $PWD/$file /usr/bin/$(basename $file)-3.8; \  
done  
  
RUN mkdir /opt/cmake-3.9.6/ && \  
cd /opt/cmake-3.9.6/ && \  
wget https://cmake.org/files/v3.9/cmake-3.9.6-Linux-x86_64.tar.gz -O - \  
| tar -xz --strip-components=1 && \  
for file in bin/*; \  
do \  
ln -s $PWD/$file /usr/bin/$(basename $file)-3.9; \  
done  
  
RUN mkdir /opt/cmake-3.10.6/ && \  
cd /opt/cmake-3.10.6/ && \  
wget https://cmake.org/files/v3.10/cmake-3.10.0-Linux-x86_64.tar.gz -O - \  
| tar -xz --strip-components=1 && \  
for file in bin/*; \  
do \  
ln -s $PWD/$file /usr/bin/$(basename $file)-3.10; \  
done  
  
# Copy cppcheck over from builder  
COPY \--from=cppcheck-builder /opt/ /opt/  
  
RUN for bin in /opt/cppcheck-1.*/bin/cppcheck-1.*; do \  
ln -s $bin /usr/bin/; \  
done  

