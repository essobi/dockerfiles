FROM xdrum/openwrt:latest  
  
MAINTAINER Alessio Cassibba (x-drum) <swapon@gmail.com>  
  
RUN opkg update  
RUN opkg install umurmur-openssl && rm -rf /var/opkg-lists  
  
EXPOSE 64738:64738 64738:64738/udp  
  
CMD ["/usr/bin/umurmurd","-d","-c","/etc/umurmur.conf"]  

