FROM ubuntu:16.04  
MAINTAINER robert-xie@foxmail.com  
RUN apt-get update && apt-get install -y \  
libc6 \  
libpcap0.8 \  
apparmor \  
libssl1.0.0 \  
libssl-dev \  
net-tools \  
traceroute \  
iptables \  
arping \  
ipcalc \  
inetutils-ping \  
curl dnsutils wget vim ethtool tcpdump \  
&& apt clean  
CMD ["bash"]  

