FROM ubuntu:17.04  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
autoconf \  
autotools-dev \  
automake \  
ca-certificates \  
clang-3.8 \  
clang-format-3.8 \  
cmake \  
curl \  
git \  
libtool \  
libssl-dev \  
llvm-3.8-dev \  
libc++abi-dev \  
libc++-dev \  
make \  
openssl \  
openssh-client \  
python3 \  
unzip \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN update-alternatives --install /usr/bin/cc cc /usr/bin/clang-3.8 999 \  
&& update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++-3.8 999  

