FROM yangliu/arch-base:2015.06.01  
MAINTAINER yangliu <i@yangliu.name>  
  
ADD shadowsocks /opt/shadowsocks  
ADD start-ssr /root/  
  
# install python2 python2-m2crypto and libsodium  
RUN pacman -Sy --needed --noconfirm python2-m2crypto libsodium \  
&& pacman -Scc --noconfirm  
  
RUN chmod +x /root/start-ssr  
  
EXPOSE 8989  
CMD ["/root/start-ssr"]

