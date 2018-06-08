FROM vmlinz/docker-openwrt-buildroot  
  
# MAINTAINER Zaihceng Qi <vmlinz@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD cc.config /tmp/  
  
# RUN sudo -iu openwrt openwrt/scripts/feeds install –a  
RUN sudo -iu openwrt cp /tmp/cc.config /home/openwrt/openwrt/.config  
RUN cd /home/openwrt/openwrt && ls -la  
RUN cd /home/openwrt/openwrt && make oldconfig  
RUN cd /home/openwrt/openwrt && make  
  

