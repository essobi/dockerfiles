FROM ubuntu:16.04  
ENV STEAM_UID 1000  
RUN apt-get update -q \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -qy lib32gcc1 \  
&& useradd --create-home -u ${STEAM_UID} steam \  
&& mkdir -p /home/steam/steamcmd  
  
WORKDIR /home/steam/steamcmd  
  
# Download with ADD  
ADD https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz ./  
RUN tar -xvzf /home/steam/steamcmd/steamcmd_linux.tar.gz && chmod +x
/home/steam/steamcmd/steamcmd.sh  
  
USER steam  

