FROM ubuntu:16.04  
MAINTAINER Thomas Schmitz <agrar.pfurtz@gmail.com>  
  
RUN mkdir -p /opt/steamcmd  
  
# Install steamcmd + srcds_linux dependencies  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
lib32gcc1 \  
gcc \  
lib32stdc++6 \  
libstdc++6 \  
gdb \  
ca-certificates \  
net-tools \  
lib32z1 \  
zlib1g \  
zlibc \  
curl  
  
# Install steamcmd to /opt/steamcmd/  
ADD https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz
/tmp/  
# Untar, create user steamcmd and chown  
RUN tar -xvf /tmp/steamcmd_linux.tar.gz -C /opt/steamcmd/ && \  
rm /tmp/steamcmd_linux.tar.gz && \  
useradd -m steam && \  
chown -R steam /opt && \  
chmod -R 744 /opt  
  
# Switch to steam user  
USER steam  
# First SteamCMD run  
RUN /opt/steamcmd/steamcmd.sh +login anonymous +quit  
  
ENTRYPOINT ["/opt/steamcmd/steamcmd.sh"]

