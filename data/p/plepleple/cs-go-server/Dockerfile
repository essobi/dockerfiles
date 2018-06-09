FROM ubuntu  
MAINTAINER Piotr "plepleple" Golan <piotr.golan@gmail.com>  
# System update and upgrade:  
RUN apt-get -q -y update && apt-get -q -y upgrade  
# Install basic tools:  
RUN apt-get -q -y install mc wget screen openssh-server  
# create user steamadmin:steamadmin  
RUN groupadd steamadmin  
RUN useradd -m -s /bin/bash -g steamadmin steamadmin  
RUN echo "steamadmin:steamadmin" | chpasswd  
# Install SteamCMD dependences  
RUN apt-get -q -y install lib32gcc1  
# Make directories for SteamCMD  
RUN mkdir /steamcmd  
RUN cd /steamcmd  
# Download and extract SteamCMD  
RUN wget
https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz  
RUN tar -xvzf steamcmd_linux.tar.gz -C /steamcmd  
# Install SteamCMD and CS:GO server  
RUN /steamcmd/steamcmd.sh +login anonymous +force_install_dir
/steamcmd/csgoserver +app_update 740 validate +quit  

