FROM ubuntu:16.04  
  
MAINTAINER StarWolf Development GmbH, <support@wolfpanel.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Setup OS with all dependencies  
RUN dpkg --add-architecture i386 && apt-get update && apt-get upgrade -y  
RUN apt-get install -qq -y \  
curl \  
gcc \  
g++ \  
lib32gcc1 \  
lib32stdc++6 \  
lib32tinfo5 \  
libtinfo5:i386 \  
lib32z1 \  
libncurses5:i386 \  
libcurl3-gnutls:i386 \  
net-tools  
  
# Add default gameserver user  
RUN useradd -m wolfpanel  
ENV HOME /home/wolfpanel  
WORKDIR /home/wolfpanel  
  
USER wolfpanel  
  
# Install SteamCMD  
RUN curl -sqL
"https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" | tar
zxvf -  
RUN ./steamcmd.sh +login anonymous +quit  
  
RUN mkdir -p ~/.steam/sdk32  
RUN ln -s ./linux32/steamclient.so ~/.steam/sdk32/steamclient.so  
  
# Create directory for the server  
RUN mkdir -p serveractive  

