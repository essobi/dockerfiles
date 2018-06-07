############################################################  
# Dockerfile to build a Starbound server  
############################################################  
  
FROM ubuntu:14.04  
  
ENV STEAM_USERNAME username  
ENV STEAM_PASSWORD password  
  
# Install Dependacy  
RUN apt-get update  
RUN apt-get -y install lib32gcc1 lib32z1 lib32ncurses5 lib32bz2-1.0 wget
supervisor lib32stdc++6  
  
# SteamCMD startup and update files  
COPY ./server/steamcmd/starbound_update.txt /server/steamcmd/  
COPY ./server/steamcmd/server_start /server/steamcmd/  
  
# Get steamCMD  
RUN wget -O - http://media.steampowered.com/client/steamcmd_linux.tar.gz | tar
-C /server/steamcmd/ -xvz  
  
# Installing the starbound server  
RUN mkdir /server/steamcmd/starbound  
  
EXPOSE 21025  
VOLUME ["/server/steamcmd/starbound"]  
ENTRYPOINT ["/server/steamcmd/server_start"]  

