FROM debian:stable  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
  
# compilers  
RUN apt-get install -y g++  
  
# tools  
RUN apt-get install -y \  
scons \  
gengetopt \  
wget \  
xz-utils \  
qemu  
  
# dependencies  
RUN apt-get install -y \  
libtool \  
intltool \  
autoconf \  
automake \  
make \  
cmake  
  
RUN TOOLCHAIN="arm-linux-gnueabihf"; \  
RELEASE="4.9-2016.02"; \  
ARCHIVE="gcc-linaro-${RELEASE}-x86_64_${TOOLCHAIN}"; \  
MIRROR="http://releases.linaro.org/components/toolchain/binaries"; \  
mkdir -p /opt/toolchains && \  
wget -O - "${MIRROR}/${RELEASE}/${TOOLCHAIN}/${ARCHIVE}.tar.xz" | \  
tar -C /opt/toolchains -xJf - && \  
mv /opt/toolchains/${ARCHIVE} /opt/toolchains/${TOOLCHAIN} && \  
cp -a /opt/toolchains/${TOOLCHAIN}/${TOOLCHAIN}/libc/lib/* \  
/opt/toolchains/${TOOLCHAIN}/${TOOLCHAIN}/lib  

