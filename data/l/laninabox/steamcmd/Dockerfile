FROM ubuntu:latest  
  
MAINTAINER laninabox <info@utopit.be>  
  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y lib32gcc1 curl  
RUN useradd -m steam  
  
USER steam  
  
WORKDIR /home/steam/  
RUN mkdir -p steamcmd_linux  
RUN curl -sqL
'https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz' | tar
zxvf - -C steamcmd_linux  
  
CMD ["steamcmd_linux/steamcmd.sh","+login","anonymous"]  

