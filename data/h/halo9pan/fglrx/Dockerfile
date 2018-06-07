# Start with build pack dependencies trusty image  
FROM buildpack-deps:trusty  
MAINTAINER Halo9Pan <halo9pan@gmail.com>  
  
# RUN sed -i 's/http:\/\/archive\\.ubuntu\\.com/http:\/\/mirrors\\.yun-
idc\\.com/g' /etc/apt/sources.list  
RUN apt-get update && apt-get install -y \  
build-essential unzip \  
cdbs fakeroot execstack dh-modaliases dkms \  
lib32gcc1 libc6-i386 \  
linux-headers-generic  
# linux-headers-3.19.0-32-generic  
RUN apt-get install -y \  
libqtcore4 libxfixes3 libxrandr2 qtcore4-l10n  
  
ENV FGLRX_VERSION=15.300-0ubuntu1_amd64_UB_14.01  
RUN cd /tmp && \  
wget -q http://www2.ati.com/drivers/linux/fglrx-core_${FGLRX_VERSION}.deb && \  
wget -q http://www2.ati.com/drivers/linux/fglrx_${FGLRX_VERSION}.deb && \  
wget -q http://www2.ati.com/drivers/linux/fglrx-dev_${FGLRX_VERSION}.deb  
  
# RUN cd /tmp && \  
# wget -q http://www2.ati.com/drivers/linux/radeon-
crimson-15.11-15.30.1025.zip && \  
# unzip radeon-crimson-15.11-15.30.1025.zip && cd fglrx-15.30.1025 && \  
# chmod +x amd-driver-installer-*.run && \  
# ./amd-driver-installer-15.30.1025-x86.x86_64.run --buildpkg Ubuntu/trusty
--NoXServer  
RUN cd /tmp && \  
dpkg -i fglrx-*.deb && \  
dpkg -i fglrx_*.deb  
  
RUN rm -rf fglrx_* fglrx-*  

