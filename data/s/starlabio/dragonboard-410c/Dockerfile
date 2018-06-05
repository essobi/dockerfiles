FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get --quiet --yes update && \  
apt-get --quiet --yes install wget build-essential git bc device-tree-compiler
libncurses-dev python libfdt-dev  
  
# Grab the linaro tool chain we want  
RUN mkdir -p /opt/linaro/aarch64 && cd /opt/linaro/aarch64 && wget --quiet
--output-document linaro-cross.tar.xz
https://releases.linaro.org/14.11/components/toolchain/binaries/aarch64-linux-
gnu/gcc-linaro-4.9-2014.11-x86_64_aarch64-linux-gnu.tar.xz && tar xf linaro-
cross.tar.xz --strip-components=1 && rm linaro-cross.tar.xz  
  
# Grab the dtbTool  
RUN mkdir -p /opt/codeaurora/ && cd /opt/codeaurora/ && git clone
git://codeaurora.org/quic/kernel/skales  
  
RUN mkdir -p /opt/codeaurora/ && cd /opt/codeaurora/ && git clone
git://codeaurora.org/platform/prebuilts/gcc/linux-x86/arm/arm-eabi-4.8.git -b
LA.BR.1.1.3.c4-01000-8x16.0  
  
# clean up apt items  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir /source  
  
env PATH /opt/linaro/aarch64/bin:/opt/codeaurora/skales:/opt/codeaurora/arm-
eabi-4.8/bin:$PATH  
env CROSS_COMPILE=aarch64-linux-gnu-  
  
VOLUME ["/source"]  
WORKDIR /source  
CMD ["/bin/bash"]  

