FROM ubuntu:14.04  
MAINTAINER Andrew Schwartzmeyer <andschwa@microsoft.com>  
  
ENV LANG=en_US.UTF-8  
RUN locale-gen en_US.UTF-8 && update-locale  
  
RUN apt-get update && apt-get install -y git curl wget && \  
echo "deb http://llvm.org/apt/trusty/ llvm-toolchain-trusty-3.6 main" | tee
/etc/apt/sources.list.d/llvm.list && \  
wget -O - http://llvm.org/apt/llvm-snapshot.gpg.key | apt-key add - && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee
/etc/apt/sources.list.d/mono-xamarin.list && \  
apt-get update && apt-get install -y \  
mono-devel \  
ca-certificates-mono \  
nuget \  
gcc \  
g++ \  
llvm-3.5 \  
clang-3.5 \  
lldb-3.6 lldb-3.6-dev \  
strace \  
libicu-dev \  
libunwind8 libunwind8-dev \  
libssl-dev \  
libcurl4-openssl-dev \  
libpam0g-dev \  
make \  
cmake \  
gettext && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

