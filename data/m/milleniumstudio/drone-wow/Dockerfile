FROM debian:stretch  
MAINTAINER FAT <contact@fat.sh>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# System essentals  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
ca-certificates \  
wget \  
curl \  
build-essential \  
cmake \  
openssl \  
git \  
gdb \  
gnupg \  
libmysql++-dev \  
libreadline-dev \  
libace-dev \  
libssl1.0-dev \  
zlib1g-dev \  
libbz2-dev \  
libcurl4-openssl-dev \  
libtool \  
binutils-dev \  
libncurses-dev \  
automake \  
mutrace \  
ninja-build \  
ccache \  
linux-perf  
  
# Install llvm/clang repo  
ENV LLVM_VERSION 5.0  
RUN wget -qO - http://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \  
&& echo "deb http://apt.llvm.org/stretch/ llvm-toolchain-
stretch-${LLVM_VERSION} main" >> /etc/apt/sources.list.d/llvm.list \  
&& echo "deb-src http://apt.llvm.org/stretch/ llvm-toolchain-
stretch-${LLVM_VERSION} main" >> /etc/apt/sources.list.d/llvm.list  
RUN apt-get update && apt-get install -y \  
clang-${LLVM_VERSION}  
  
# Install percona packages from apt  
RUN wget -q https://repo.percona.com/apt/percona-release_0.1-5.stretch_all.deb
\  
&& dpkg -i percona-release_*_all.deb  
RUN apt-get update && apt-get install -y \  
percona-server-client-5.7 \  
libperconaserverclient20-dev  
  
# Install libboost  
RUN apt-get update && apt-get install -y \  
libboost-dev \  
libboost-thread-dev \  
libboost-system-dev \  
libboost-filesystem-dev \  
libboost-program-options-dev \  
libboost-iostreams-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN ln -s /usr/bin/clang-${LLVM_VERSION} /usr/bin/clang; \  
ln -s /usr/bin/clang++-${LLVM_VERSION} /usr/bin/clang++; \  
ln -s /usr/bin/llvm-symbolizer-${LLVM_VERSION} /usr/bin/llvm-symbolizer;  
  
ENV CC clang  
ENV CXX clang++

