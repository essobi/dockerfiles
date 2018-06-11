FROM dclong/ubuntu_cn  
  
RUN apt-get update \  
&& apt-get install -y \  
sudo \  
vim git \  
wget \  
xfce4 xfce4-whiskermenu-plugin \  
terminator firefox \  
pelican \  
&& wget
http://download.nomachine.com/download/5.3/Linux/nomachine_5.3.12_10_amd64.deb
-O /nomachine.deb \  
&& dpkg -i /nomachine.deb \  
&& rm /nomachine.deb \  
&& mkdir /root/.config \  
&& apt-get autoremove \  
&& apt-get autoclean  
  
EXPOSE 4000  
COPY settings /settings  
COPY scripts /scripts  
  
ENTRYPOINT ["/scripts/init.sh"]  

