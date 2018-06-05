# Distro and Version  
FROM phusion/baseimage  
  
# Dockerfile Maintainer  
MAINTAINER Zeus Game Cloud "dev@zeus.cloud"  
# Environment Variables  
ENV DEBIAN_FRONTEND noninteractive  
ENV CLOUD_DEPENDENCIES lib32gcc1 curl wget  
ENV STEAM_URL
https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz  
  
# 32 Bit Steam Libraries Needed  
RUN dpkg --add-architecture i386  
  
# Run Update  
RUN apt-get -y update  
  
# Run Dependencies Install  
RUN apt-get -y install -y $CLOUD_DEPENDENCIES  
  
# Change Working Directory  
WORKDIR /etc/service/steamcmd  
  
# Download, Unpack and Remove  
RUN (wget http://media.steampowered.com/installer/steamcmd_linux.tar.gz) && \  
(tar -xzf steamcmd_linux.tar.gz) && (rm steamcmd_linux.tar.gz)  
  
# Install and Update SteamCMD  
RUN ./steamcmd.sh +login anonymous +quit  
  
# Clean Apt for future builds  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

