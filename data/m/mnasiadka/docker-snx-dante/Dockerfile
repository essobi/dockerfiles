FROM ubuntu:16.04  
ADD scripts/snx_install.sh /root  
  
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y bzip2
kmod libstdc++5:i386 libpam0g:i386 libx11-6:i386 expect iptables net-tools
iputils-ping dante-server iproute2  
  
RUN cd /root && bash -x snx_install.sh  
  
ADD scripts/snx.sh /root  
RUN chmod +x /root/snx.sh  
  
ADD scripts/danted.conf /etc/danted.conf  
  
EXPOSE 1080  
CMD ["/root/snx.sh"]  

