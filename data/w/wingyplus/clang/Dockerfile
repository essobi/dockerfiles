FROM ubuntu  
MAINTAINER Thanabodee Charoenpiriyakij <wingyminus@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
cmake make valgrind \  
binutils libc-dev libgcc-5-dev libstdc++-5-dev \  
curl ca-certificates xz-utils \  
&& rm -rf /var/lib/apt/lists/*  
RUN curl -s http://llvm.org/releases/3.8.1/clang+llvm-3.8.1-x86_64-linux-gnu-
ubuntu-16.04.tar.xz | tar xJv  
ENV PATH=/clang+llvm-3.8.0-x86_64-linux-gnu-ubuntu-16.04/bin:$PATH  
CMD ["/bin/bash"]  

