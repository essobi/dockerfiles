# Docker image for developing/compiling for the Omega2 and Omega2+ boards in C
and C++  
# Based on jlc's and borromeotlhs' dockerfiles  
FROM ubuntu:14.04  
LABEL maintainer="shivanshvij@outlook.com"  
LABEL description="Dockerfile to install a prebuilt environment for Omega2 and
Omega2 Development in C and C++"  
  
# Install prerequisites  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
subversion g++ zlib1g-dev build-essential git python libncurses5-dev gawk
gettext unzip file libssl-dev wget nano automake autoconf gcc curl libtool\  
&& rm -rf /var/lib/apt/lists/*  
  
# Install CMake to build the Cross-Compiler  
RUN mkdir ~/temp &&\  
cd ~/temp &&\  
wget https://cmake.org/files/v3.7/cmake-3.7.2.tar.gz &&\  
tar xzvf cmake-3.7.2.tar.gz &&\  
cd cmake-3.7.2/ &&\  
./bootstrap &&\  
make &&\  
make install &&\  
rm -rf ~/temp  
  
# Clone the lede-project git in order to begin coding  
RUN git clone https://github.com/lede-project/source.git lede  
  
# The next commands are done inside the lede directory as the omega user so
that the install can run without root  
RUN adduser omega && echo 'omega:omega' | chpasswd && chown -R omega:omega
lede  
WORKDIR lede  
USER omega  
  
# Install all the packages for the Omega2  
RUN ./scripts/feeds update -a && ./scripts/feeds install -a  
  
# Setup the cross-compiler config file  
RUN echo "CONFIG_TARGET_ramips=y" > .config && \  
echo "CONFIG_TARGET_ramips_mt7688=y" >> .config && \  
echo "CONFIG_TARGET_ramips_mt7688_DEVICE_omega2=y" >> .config && \  
echo "CONFIG_PACKAGE_libugpio=y" >> .config && \  
make defconfig  
  
# Compile the cross-compiler with debugging enabled  
RUN make -j1 -d V=s  
  
# Set the environment paths to make life easier  
ENV PATH "$PATH:/lede/staging_dir/toolchain-
mipsel_24kc_gcc-5.5.0_musl/bin:/lede/staging_dir/toolchain-
mipsel_24kc_gcc-5.5.0_musl/bin"  
RUN export STAGING_DIR="/lede/staging_dir/"  
  
# Create a working directory and set user to root  
USER root  
RUN mkdir WorkingDirectory  
WORKDIR WorkingDirectory  
ENV PATH "$PATH:/lede/staging_dir/toolchain-
mipsel_24kc_gcc-5.5.0_musl/bin:/lede/staging_dir/toolchain-
mipsel_24kc_gcc-5.5.0_musl/bin"  
RUN export STAGING_DIR="/lede/staging_dir/"  

