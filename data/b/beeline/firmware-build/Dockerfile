FROM ubuntu:16.04  
MAINTAINER Chetan Padia <chet@beeline.co>  
RUN apt-key update && \  
sh -c 'curl -sL https://deb.nodesource.com/setup_6.x | bash -' && \  
apt-get update && \  
apt-get install -y curl git unzip bzip2 build-essential gcc-multilib libssl-
dev srecord openocd pkg-config nodejs s3cmd python && \  
apt-get clean all  
  
# NRF51 SDK v10  
ADD
https://developer.nordicsemi.com/nRF5_SDK/nRF51_SDK_v10.x.x/nRF51_SDK_10.0.0_dc26b5e.zip
/nRF51_SDK_10.0.0_dc26b5e.zip  
RUN mkdir -p /nrf51/nRF51_SDK_10.0.0 && unzip -q
../../nRF51_SDK_10.0.0_dc26b5e.zip -d /nrf51/nRF51_SDK_10.0.0  
  
# GCC ARM toolchain 2016q2  
RUN curl -L -o /opt/gcc-arm-none-eabi-5.tar.bz2 https://launchpad.net/gcc-arm-
embedded/5.0/5-2016-q2-update/+download/gcc-arm-none-
eabi-5_4-2016q2-20160622-linux.tar.bz2 2>/dev/null && \  
tar xjf /opt/gcc-arm-none-eabi-5.tar.bz2 -C /opt && \  
rm /opt/gcc-arm-none-eabi-5.tar.bz2 && \  
ln -s /opt/gcc-arm-none-eabi-5_4-2016q2 /opt/gcc-arm-none-eabi-5  
ENV PATH="${PATH}:/opt/gcc-arm-none-eabi-5/bin"  

