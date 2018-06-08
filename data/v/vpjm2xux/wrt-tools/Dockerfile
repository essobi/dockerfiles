FROM debian  
  
RUN \  
dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y autoconf automake bc bison bzip2 ccache cmake flex \  
gcc gettext git libc6:i386 libstdc++6:i386 libtool make \  
net-tools pkg-config subversion tar wget \  
xz-utils patch libssl-dev zip p7zip gnupg libz-dev && \  
wget https://github.com/vpJm2Xux/wrt-
tools/releases/download/0.0.11/arm-v7a-musl.tar.xz && \  
tar xvf arm-v7a-musl.tar.xz && \  
rm arm-v7a-musl.tar.xz && \  
echo OK!  
  
ENV PATH="/opt/cross/arm-v7a/staging_dir/host/bin:${PATH}"  
ENV PATH="/opt/cross/arm-v7a/staging_dir/toolchain-
arm_cortex-a9_gcc-6.3.0_musl-1.1.16_eabi/bin:${PATH}"  
ENV STAGING_DIR="/opt/cross/arm-v7a/staging_dir/toolchain-
arm_cortex-a9_gcc-6.3.0_musl-1.1.16_eabi"  

