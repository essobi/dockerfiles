FROM ubuntu:16.04  
  
MAINTAINER Atilim Cetin <atilim.cetin@gmail.com>  
  
RUN export LLVM_CONFIG=/tmp/clang/bin/llvm-config && \  
export CLANG=/tmp/clang/bin/clang && \  
apt-get update && apt-get install -y wget xz-utils git make gcc g++ zlib1g-dev
&& \  
cd /tmp && \  
wget http://llvm.org/releases/3.9.0/clang+llvm-3.9.0-x86_64-linux-gnu-
ubuntu-16.04.tar.xz && \  
tar xf clang+llvm-3.9.0-x86_64-linux-gnu-ubuntu-16.04.tar.xz && \  
mv clang+llvm-3.9.0-x86_64-linux-gnu-ubuntu-16.04 clang && \  
git clone --depth 1 \--no-single-branch https://github.com/halide/Halide.git
/tmp/Halide && \  
cd /tmp/Halide && \  
git checkout master && \  
mkdir /root/halide_master && \  
cd /root/halide_master && \  
make -f /tmp/Halide/Makefile && \  
make -f /tmp/Halide/Makefile install && \  
rm -rf /root/halide_master && \  
mv /usr/local/share/halide/ /root/halide_master && \  
mv /usr/local/lib/ /root/halide_master/bin && \  
mv /usr/local/include/ /root/halide_master/include && \  
cd /tmp/Halide && \  
git checkout auto_scheduler && \  
mkdir /root/halide_auto_scheduler && \  
cd /root/halide_auto_scheduler && \  
make -f /tmp/Halide/Makefile && \  
make -f /tmp/Halide/Makefile install && \  
rm -rf /root/halide_auto_scheduler && \  
mv /usr/local/share/halide/ /root/halide_auto_scheduler && \  
mv /usr/local/lib/ /root/halide_auto_scheduler/bin && \  
mv /usr/local/include/ /root/halide_auto_scheduler/include && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

