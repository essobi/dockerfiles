FROM ubuntu:xenial  
  
MAINTAINER Augment  
  
ENV LLVM_VERSION=5.0 \  
CMAKE_VERSION=3.9.4 \  
CC=clang \  
CXX=clang++ \  
CMAKE_C_COMPILER=clang \  
CMAKE_CXX_COMPILER=clang++ \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US:en \  
LC_ALL=en_US.UTF-8  
# Install Clang and dependencies  
RUN echo "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-5.0 main" >>
/etc/apt/sources.list.d/llvm.list \  
&& apt-key adv --fetch-keys http://apt.llvm.org/llvm-snapshot.gpg.key \  
&& apt-get -qq update  
# Install Clang and dependencies  
RUN apt-get -qq install -y locales nano python-dev sudo wget git vim
clang-${LLVM_VERSION} llvm-${LLVM_VERSION} llvm-${LLVM_VERSION}-dev
llvm-${LLVM_VERSION}-runtime llvm make valgrind g++-multilib libgmp-dev
libmpfr-dev libmpc-dev nasm dh-autoreconf libffi-dev libssl-dev ninja-build
libc6-dev libc++-dev libc++abi-dev build-essential  
RUN apt-get upgrade -y libc++-dev  
# Update locales  
RUN locale-gen en_US.UTF-8 \  
&& dpkg-reconfigure -f noninteractive locales  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Update Clang name  
RUN update-alternatives --install /usr/bin/clang++ clang++
/usr/bin/clang++-${LLVM_VERSION} 100 \  
&& update-alternatives --install /usr/bin/clang clang
/usr/bin/clang-${LLVM_VERSION} 100 \  
&& update-alternatives --install /usr/bin/cc cc /usr/bin/clang-${LLVM_VERSION}
100 \  
&& update-alternatives --install /usr/bin/c++ c++
/usr/bin/clang++-${LLVM_VERSION} 100  
# Install CMake  
RUN wget
https://cmake.org/files/v3.9/cmake-${CMAKE_VERSION}-Linux-x86_64.tar.gz --no-
check-certificate -q \  
&& tar -xzf cmake-${CMAKE_VERSION}-Linux-x86_64.tar.gz \  
&& cp -fR cmake-${CMAKE_VERSION}-Linux-x86_64/* /usr \  
&& rm -rf cmake-${CMAKE_VERSION}-Linux-x86_64 \  
&& rm cmake-${CMAKE_VERSION}-Linux-x86_64.tar.gz  
# Install python pip  
RUN wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate -q \  
&& python get-pip.py \  
&& pip install -q -U pip  
# Install conan  
RUN pip install -q conan  
# Create User  
RUN groupadd 1001 -g 1001 \  
&& groupadd 1000 -g 1000 \  
&& groupadd 2000 -g 2000 \  
&& groupadd 999 -g 999 \  
&& useradd -ms /bin/bash conan -g 1001 -G 1000,2000,999 \  
&& echo "conan:conan" | chpasswd \  
&& adduser conan sudo \  
&& echo "conan ALL= NOPASSWD: ALL\n" >> /etc/sudoers  
  
USER conan  
WORKDIR /home/conan  
RUN mkdir -p /home/conan/.conan  

