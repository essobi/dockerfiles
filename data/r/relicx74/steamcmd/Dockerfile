#Base image with /steamcmd/steamcmd.sh  
#Game specific image will install/launch game by ID via ENV vars  
FROM debian:stretch-slim  
  
RUN mkdir /steamcmd && \  
apt-get update && \  
apt-get install -y \  
wget \  
lib32gcc1 \  
gettext-base && \  
rm -rf /var/lib/apt/lists/* && \  
wget -qO- http://media.steampowered.com/client/steamcmd_linux.tar.gz | tar xvz
-C /steamcmd/ && \  
chown root:root /steamcmd/* -R;  

