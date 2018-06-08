FROM ubuntu:18.04  
MAINTAINER <https://github.com/mogemimi>  
  
RUN \  
apt update && \  
apt upgrade -y && \  
apt install -y wget && \  
echo "deb http://apt.llvm.org/artful/ llvm-toolchain-artful-5.0 main" | tee
/etc/apt/sources.list.d/llvm.list && \  
echo "deb-src http://apt.llvm.org/artful/ llvm-toolchain-artful-5.0 main" |
tee -a /etc/apt/sources.list.d/llvm.list && \  
wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - && \  
apt update && \  
apt install -y \  
clang-5.0 \  
lldb-5.0 \  
libclang-common-5.0-dev \  
libclang-5.0-dev \  
libclang1-5.0 \  
libllvm5.0 \  
llvm-5.0 \  
llvm-5.0-dev \  
llvm-5.0-runtime \  
clang-format-5.0 && \  
apt install -y \  
build-essential \  
software-properties-common \  
byobu \  
curl \  
git \  
htop \  
man \  
unzip \  
make \  
cmake \  
python2.7 \  
libc++-dev \  
libc++abi-dev \  
mesa-common-dev \  
libglu1-mesa-dev \  
freeglut3-dev \  
libopenal1 \  
libopenal-dev && \  
apt clean && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /root  
CMD ["bash"]  

