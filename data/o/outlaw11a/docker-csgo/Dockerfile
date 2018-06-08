FROM ubuntu:14.04  
MAINTAINER Alex Price <me@alexprice.io>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies  
RUN apt-get update &&\  
apt-get install -y curl lib32gcc1  
  
RUN useradd -m steam  
  
# Run commands as the steam user  
USER steam  
  
RUN mkdir -p /home/steam/steamcmd &&\  
cd /home/steam/steamcmd &&\  
curl -s http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar
-vxz  
  
ADD install.txt /home/steam/steamcmd/  
  
# Install CS:GO  
RUN mkdir /home/steam/csgo &&\  
cd /home/steam/steamcmd &&\  
#./steamcmd.sh \  
# +login anonymous \  
# +force_install_dir /home/steam/csgo/ \  
# +app_update 740 validate \  
# +quit  
./steamcmd.sh +runscript install.txt  
  
# Make server port available to host  
EXPOSE 27015  
# This container will be executable  
WORKDIR /home/steam/csgo  
ENTRYPOINT ["./srcds_run"]  

