# Cross Compiler for aarch64, arm and armhf  
FROM ubuntu:trusty  
MAINTAINER Samuel Cozannet <samnco@gmail.com>  
  
# RUNTIME ENV VARIABLES  
# Architecture can be aarch64, arm or armhf  
ENV ARCH=aarch64  
  
# Copied from https://github.com/sdt/docker-raspberry-pi-cross-compiler/  
# The host can be aarch64-linux-gnu, arm-linux-gnueabi, or arm-linux-gnueabihf  
ENV HOST=aarch64-linux-gnu \  
TOOLCHAIN_ROOT=/opt/${HOST} \  
CROSS_COMPILE=${TOOLCHAIN_ROOT}/bin/${HOST}-  
ENV AS=${CROSS_COMPILE}as \  
AR=${CROSS_COMPILE}ar \  
CC=${CROSS_COMPILE}gcc \  
CPP=${CROSS_COMPILE}cpp \  
CXX=${CROSS_COMPILE}g++ \  
LD=${CROSS_COMPILE}ld  
  
# Install dependencies  
RUN apt-get update && \  
apt-get upgrade -yqq && \  
apt-get install -yqq curl \  
wget \  
git \  
nano \  
xz-utils \  
automake \  
bc \  
bison \  
cmake \  
curl \  
flex \  
lib32stdc++6 \  
lib32z1 \  
ncurses-dev \  
runit && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Download AARCH64 from linaro  
RUN cd /tmp && \  
wget -c
http://releases.linaro.org/14.11/components/toolchain/binaries/aarch64-linux-
gnu/gcc-linaro-4.9-2014.11-x86_64_aarch64-linux-gnu.tar.xz && \  
tar xf gcc-linaro-4.9-2014.11-x86_64_aarch64-linux-gnu.tar.xz && \  
mv gcc-linaro-4.9-2014.11-x86_64_aarch64-linux-gnu /opt/ && \  
rm -rf gcc-linaro-4.9-2014.11-x86_64_aarch64-linux-gnu.tar.xz && \  
ln -sf /opt/gcc-linaro-4.9-2014.11-x86_64_aarch64-linux-gnu
/opt/aarch64-linux-gnu  
  
# Download ARM from linaro  
RUN cd /tmp && \  
wget -c http://releases.linaro.org/14.11/components/toolchain/binaries/arm-
linux-gnueabi/gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabi.tar.xz && \  
tar xf gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabi.tar.xz && \  
mv gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabi /opt/ && \  
rm -rf gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabi.tar.xz && \  
ln -sf /opt/gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabi /opt/arm-linux-
gnueabi  
  
# Download ARMHF from linaro  
RUN cd /tmp && \  
wget -c http://releases.linaro.org/14.11/components/toolchain/binaries/arm-
linux-gnueabihf/gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf.tar.xz && \  
tar xf gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf.tar.xz && \  
mv gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf /opt/ && \  
rm -rf gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf.tar.xz && \  
ln -sf /opt/gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf /opt/arm-linux-
gnueabihf  
  
# Create symlinks to /usr/local/bin  
RUN for arch in aarch64-linux-gnu arm-linux-gnueabi arm-linux-gnueabihf; do \  
for binary in addr2line ar as c++ c++filt cpp elfedit g++ gcc \  
gcc-4.9.3 gcc-ar gcc-nm gcc-ranlib gcov gdb gfortran gprof ld \  
ld.bfd nm objcopy objdump ranlib readelf size strings strip gdbserver runtest
; do \  
ln -sf /opt/${arch}/bin/${arch}-${binary} /usr/local/bin/${arch}-${binary}; \  
done ; \  
done ;  
  
RUN mkdir -p /build  
  

