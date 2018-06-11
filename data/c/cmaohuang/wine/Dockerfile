FROM ubuntu:14.04  
MAINTAINER James Huang  
  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/wine && \  
echo "wine:x:${uid}:${gid}:wine,,,:/home/wine:/bin/bash" >> /etc/passwd && \  
echo "wine:x:${uid}:" >> /etc/group && \  
echo "wine ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/wine && \  
chmod 0440 /etc/sudoers.d/wine && \  
chown ${uid}:${gid} -R /home/wine  
  
RUN dpkg --add-architecture i386 && \  
apt-get install -y software-properties-common && add-apt-repository -y
ppa:ubuntu-wine/ppa && \  
apt-get update && \  
apt-get install -y language-pack-zh-hant fonts-wqy-zenhei wine1.6 && \  
wget
https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks
-O /usr/local/bin/winetricks && \  
chmod +x /usr/local/bin/winetricks && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /var/cache/*  
  
ENV HOME /home/wine  
WORKDIR /home/wine  
  
USER wine  
ENV WINEPREFIX /home/wine/.wine  
ENV WINEARCH win32  
ENV LC_ALL zh_TW.UTF-8  
ENV LANG zh_TW.UTF-8  
ENV LANGUAGE zh_TW.UTF-8  

