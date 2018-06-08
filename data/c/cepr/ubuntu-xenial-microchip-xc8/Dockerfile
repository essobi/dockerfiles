FROM ubuntu:xenial  
RUN \  
dpkg \--add-architecture i386 && \  
apt-get update && \  
apt-get install -y \  
build-essential \  
git \  
ssh \  
libc6-i386 \  
libx11-dev:i386 \  
libxext-dev:i386 \  
libexpat1-dev:i386 \  
libstdc++6-4.7-dev:i386  
  
# A sync is needed after chmod, see https://github.com/moby/moby/issues/9547  
ADD http://ww1.microchip.com/downloads/en/DeviceDoc/xc8-v1.45-full-install-
linux-installer.run .  
RUN \  
chmod +x xc8-v1.45-full-install-linux-installer.run && \  
sync && \  
./xc8-v1.45-full-install-linux-installer.run \--mode unattended
--netservername localhost && \  
rm -f xc8-v1.45-full-install-linux-installer.run && \  
/opt/microchip/xc8/v1.45/bin/xc8 \--ver  
ADD http://ww1.microchip.com/downloads/en/DeviceDoc/MPLABX-v4.05-linux-
installer.tar .  
RUN \  
tar xf MPLABX-v4.05-linux-installer.tar && \  
rm MPLABX-v4.05-linux-installer.tar && \  
USER=root ./MPLABX-v4.05-linux-installer.sh \-- --mode unattended --ipe 0
--collectInfo 0 && \  
rm MPLABX-v4.05-linux-installer.sh  
  

