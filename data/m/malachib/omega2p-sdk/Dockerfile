# Linux dev environment for LEDE project  
# Based on borromeotlhs' dockerfile  
FROM ubuntu:14.04  
LABEL maintainer="joseluis.canovas@outlook.com"  
LABEL description="Dockerfile for Onion Omega2 SDK environment. It can be
modified for Omega2+."  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
subversion g++ zlib1g-dev build-essential git python libncurses5-dev gawk
gettext unzip file libssl-dev wget \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install CMake 3.7.2  
RUN mkdir ~/temp &&\  
cd ~/temp &&\  
wget https://cmake.org/files/v3.7/cmake-3.7.2.tar.gz &&\  
tar xzvf cmake-3.7.2.tar.gz &&\  
cd cmake-3.7.2/ &&\  
./bootstrap &&\  
make &&\  
make install &&\  
rm -rf ~/temp  
  
RUN git clone https://github.com/lede-project/source.git lede  
  
RUN adduser omega && echo 'omega:omega' | chpasswd && chown -R omega:omega
lede  
WORKDIR lede  
USER omega  
  
RUN ./scripts/feeds update -a && ./scripts/feeds install -a  
  
# Set SDK environment for Omega2  
# For Omega2+ change the third echo line with: (notice the 'p' for plus)  
# echo "CONFIG_TARGET_ramips_mt7688_DEVICE_omega2p=y" > .config && \  
RUN echo "CONFIG_TARGET_ramips=y" > .config && \  
echo "CONFIG_TARGET_ramips_mt7688=y" >> .config && \  
echo "CONFIG_TARGET_ramips_mt7688_DEVICE_omega2=y" >> .config && \  
make defconfig  
  
# RUN make  
# ENV PATH "$PATH:/lede/staging_dir/toolchain-
mipsel_24kc_gcc-5.4.0_musl-1.1.15/bin:/lede/staging_dir/toolchain-
mipsel_24kc_gcc-5.4.0_musl-1.1.15/bin"  
# Use this command to run with shared directory:  
# docker run -it -v /my_host_dir:/remote jlcs/omega2-sdk bash  

