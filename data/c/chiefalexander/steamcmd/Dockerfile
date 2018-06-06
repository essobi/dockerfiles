FROM ubuntu:17.04  
  
WORKDIR /home/steam  
  
RUN set -xe \  
&& apt-get update \  
&& apt-get install -y lib32gcc1 curl \  
&& useradd -d /home/steam steam \  
&& chown -hvR steam /home/steam  
  
USER steam  
  
RUN set -xe \  
&& mkdir /home/steam/Steam \  
&& curl -sqL
"https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" | tar
zxvf - -C ./Steam \  
&& ./Steam/steamcmd.sh +login anonymous +quit  

