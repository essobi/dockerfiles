# OpenWrt 14.07 Build System  
FROM yinping/openwrt:bb  
  
MAINTAINER yp_ren@hotmail.com  
  
USER ubuntu  
  
WORKDIR /home/ubuntu/openwrt  
#RUN make download  
RUN make prepare  
#RUN make compile  
#RUN make clean  
#RUN make index  
  
CMD ["sudo","/usr/sbin/sshd","-D"]  

