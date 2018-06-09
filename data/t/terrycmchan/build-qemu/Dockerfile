# Rockchip development environment based on Ubuntu 17.04 LTS.  
# version 0.0.1  
# Start with Ubuntu 17.04 LTS.  
#FROM debian:stretch  
FROM ubuntu:17.04  
  
MAINTAINER Terry Chan <terrygarbie@yahoo.com.hk>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
# First, install add-apt-repository and bzip2  
RUN apt-get update && apt-get install -y \  
make \  
gcc \  
g++ \  
wget \  
python \  
unzip \  
bc \  
automake \  
cpio \  
bison \  
flex \  
texinfo \  
\  
binutils \  
build-essential \  
gzip \  
locales \  
mercurial \  
patch \  
perl \  
sed \  
tar \  
\  
git \  
pkg-config \  
zlib1g-dev \  
libglib2.0-dev \  
libpixman-1-dev \  
libfdt-dev \  
\  
git-email \  
libaio-dev libbluetooth-dev libbrlapi-dev libbz2-dev \  
libcap-dev libcap-ng-dev libcurl4-gnutls-dev libgtk-3-dev \  
libibverbs-dev libjpeg8-dev libncurses5-dev libnuma-dev \  
librbd-dev librdmacm-dev \  
libsasl2-dev libsdl1.2-dev libseccomp-dev libsnappy-dev libssh2-1-dev \  
libvde-dev libvdeplug-dev libvte-2.91-dev libxen-dev liblzo2-dev \  
valgrind xfslibs-dev  
  
# Sometimes Buildroot need proper locale, e.g. when using a toolchain  
# based on glibc.  
RUN locale-gen en_US.utf8  
  

