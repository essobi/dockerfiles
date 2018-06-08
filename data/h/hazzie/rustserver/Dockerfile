FROM phusion/baseimage:latest  
MAINTAINER Hazzie  
EXPOSE 28015/tcp  
EXPOSE 28015/udp  
EXPOSE 28016/tcp  
ENV DEBIAN_FRONTEND noninteractive  
CMD bash  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y lib32gcc1 libstdc++6:i386 curl tmux bsdmainutils wget
mailutils postfix ca-certificates file libstdc++6 python git nano && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/* && \  
useradd -m rustserver && \  
chown rustserver:rustserver /home/rustserver -R && \  
echo "rustserver ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \  
curl
https://raw.githubusercontent.com/dgibbs64/linuxgsm/master/Rust/rustserver >
/home/rustserver/rustserver && \  
chmod a+x /home/rustserver/rustserver && \  
chown rustserver:rustserver /home/rustserver/rustserver && \  
echo "rustserver ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
USER rustserver  
WORKDIR /home/rustserver  
RUN ./rustserver auto-install

