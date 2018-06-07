FROM debian:jessie  
  
# Install build dependencies  
RUN apt-get update && apt-get install -y \  
bc \  
build-essential \  
curl \  
git-core \  
libncurses5-dev \  
module-init-tools  
  
# Install crosscompile toolchain for ARM64/aarch64  
RUN mkdir -p /opt/linaro && \  
curl -sSL
https://releases.linaro.org/components/toolchain/binaries/7.1-2017.08/arm-
linux-gnueabihf/gcc-linaro-7.1.1-2017.08-x86_64_arm-linux-gnueabihf.tar.xz |
tar xfJ - -C /opt/linaro  
ENV CROSS_COMPILE=/opt/linaro/gcc-linaro-7.1.1-2017.08-x86_64_arm-linux-
gnueabihf/bin/arm-linux-gnueabihf-  
ENV ARCH=arm  
  
# Create working directory  
RUN mkdir -p /workdir  
WORKDIR /workdir  
ENV WORKDIR /workdir  
ENV BUILD_DEST /workdir/build  
  
# Add the build script and set it as default command  
COPY build-rpi3-kernel /opt/bin/build-rpi3-kernel  
CMD ["/opt/bin/build-rpi3-kernel"]  

