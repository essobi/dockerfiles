FROM debian:buster  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
gcc \  
libc6-dev \  
make \  
pkg-config \  
g++-arm-linux-gnueabihf \  
libc6-dev-armhf-cross && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV CARGO_TARGET_ARMV7_UNKNOWN_LINUX_GNUEABIHF_LINKER=arm-linux-gnueabihf-gcc
\  
CC_armv7_unknown_linux_gnueabihf=arm-linux-gnueabihf-gcc \  
CXX_armv7_unknown_linux_gnueabihf=arm-linux-gnueabihf-g++ \  
PATH=/root/.cargo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  

