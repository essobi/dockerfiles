FROM rigormortiz/ubuntu-supervisor:0.1  
MAINTAINER Mike Ortiz <mike@jellydice.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y && \  
apt-get install -y xrdp && \  
apt-get autoclean && apt-get autoremove && \  
rm -rf /var/lib/apt/lists/* && \  
useradd -ms /bin/bash desktop && \  
sed -i '/TerminalServerUsers/d' /etc/xrdp/sesman.ini && \  
sed -i '/TerminalServerAdmins/d' /etc/xrdp/sesman.ini && \  
xrdp-keygen xrdp auto && \  
echo "desktop:desktop" | chpasswd  
  
ADD xrdp.conf /etc/supervisor/conf.d/xrdp.conf  
  
EXPOSE 3389  

