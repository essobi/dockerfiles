FROM debian:stretch-slim  
LABEL maintainer "zcsevcik@gmail.com"  
  
RUN export DEBIAN_FRONTEND='noninteractive' && \  
apt-get update && \  
apt-get install --no-install-recommends -y \  
make \  
pkg-config \  
gcc-mingw-w64-x86-64 \  
g++-mingw-w64-x86-64 \  
gdb-mingw-w64 \  
gdb-mingw-w64-target \  
mingw-w64-tools \  
mingw-w64-x86-64-dev \  
mingw-w64-common \  
libgcrypt-mingw-w64-dev \  
libgpg-error-mingw-w64-dev \  
libz-mingw-w64-dev \  
win-iconv-mingw-w64-dev \  
&& \  
apt clean && rm -fr /var/lib/apt/lists/*  

