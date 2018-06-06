FROM zoobab/openwrt-base  
  
USER openwrt  
WORKDIR /home/openwrt  
RUN git clone \--quiet https://github.com/mirrors/openwrt.git  
WORKDIR /home/openwrt/openwrt  
RUN echo "CONFIG_TARGET_ar71xx=y" > .config  
RUN make defconfig  
RUN make prereq  
RUN make -j`nproc` tools/install || make -j1 V=s  
#RUN make -j`nproc` toolchain/install || mak -j1 V=s  

