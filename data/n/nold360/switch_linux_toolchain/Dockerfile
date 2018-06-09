# Simple container including nintendo-swtich / nvidia tegra linux toolchain  
FROM debian:sid  
  
ENV GCC_64
https://releases.linaro.org/components/toolchain/binaries/latest-7/aarch64-linux-
gnu/gcc-linaro-7.2.1-2017.11-x86_64_aarch64-linux-gnu.tar.xz  
ENV GCC_ARM
https://releases.linaro.org/components/toolchain/binaries/latest-7/arm-linux-
gnueabi/gcc-linaro-7.2.1-2017.11-x86_64_arm-linux-gnueabi.tar.xz  
  
# Dont change this  
ENV PATH $PATH:/opt/toolchain/aarch64-linux-gnu/bin:/opt/toolchain/arm-linux-
gnueabi/bin  
# Software requirements  
RUN sed -i 's/sid\ main/sid\ main\ non-free/' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -yq --no-install-recommends install \  
build-essential \  
libssl-dev \  
swig \  
bison \  
flex \  
python3 \  
python-dev \  
python3-usb \  
libusb-1.0-0-dev \  
zlib1g-dev \  
bc \  
firmware-linux \  
firmware-brcm80211 \  
cmake \  
libpci-dev \  
git \  
pkg-config \  
ca-certificates \  
wget && \  
apt-get clean  
  
# Download / Install toolchain  
RUN mkdir /opt/toolchain && cd /opt/toolchain && \  
wget -O gcc_aarch64-linux-gnu.tar.gz -nv "$GCC_64" && \  
wget -O gcc_arm-linux-gnueabi.tar.gz -nv "$GCC_ARM" && \  
tar -xf gcc_aarch64-linux-gnu.tar.gz && \  
tar -xf gcc_arm-linux-gnueabi.tar.gz && \  
ln -s gcc*aarch64-linux-gnu aarch64-linux-gnu && \  
ln -s gcc*arm-linux-gnueabi arm-linux-gnueabi && \  
rm *.tar.gz  
  
COPY brcmfmac4356-pcie.txt /lib/firmware/brcm/brcmfmac4356-pcie.txt  
  
VOLUME /source  
WORKDIR /source  
CMD bash  

