FROM ubuntu:14.04  
# UPGRADE  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip vim wget && \  
apt-get install -y x11-xserver-utils && \  
rm -rf /var/lib/apt/lists/*  
  
RUN sudo apt-get update  
RUN sudo apt-get -y upgrade  
RUN mkdir -p /etc/init/  
RUN touch /etc/init/lxdm.conf  
RUN adduser --disabled-password --gecos "" ubuntu  
RUN adduser --disabled-password --gecos "" hedge  
  
RUN sudo apt-get update && apt-get -y --force-yes --no-install-recommends
install lxde joe mc strace fastjar awscli ruby2.0 xrdp tightvncserver
supervisor xfonts-base adduser libfontconfig  
  
# VI a  
RUN apt-get install vim  
RUN sed -i '/exit 0/c\\\n' /etc/rc.local  
  
# PORTS  
# 22 ssh, 80 http, 443 https, 1194 vpn, 5900 tightVNC  
EXPOSE 22/tcp 80/tcp 443/tcp 1194/udp 5900/tcp  
  
CMD ["/etc/rc.local"]  

