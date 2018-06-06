FROM ubuntu:15.04  
ADD scrics/snx_install.sh /root  
  
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y bzip2
openjdk-8-jdk kmod libstdc++5:i386 libpam0g:i386 libx11-6:i386 expect iptables
net-tools iputils-ping  
  
RUN cd /root && bash -x snx_install.sh  
  
ADD scrics/snx.sh /root  
RUN chmod +x /root/snx.sh  
  
CMD ["/root/snx.sh"]  

