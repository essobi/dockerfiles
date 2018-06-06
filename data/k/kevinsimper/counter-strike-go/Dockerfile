FROM ubuntu  
MAINTAINER Kevin Simper kevin.simper@gmail.com  
  
RUN apt-get update -y && apt-get upgrade -y && \  
apt-get install -y wget lib32gcc1  
  
RUN mkdir /steamcmd && cd /steamcmd && \  
wget http://media.steampowered.com/installer/steamcmd_linux.tar.gz && \  
tar -xvzf steamcmd_linux.tar.gz  
  
RUN /steamcmd/steamcmd.sh +login anonymous +force_install_dir
/steamcmd/csgoserver +app_update 740 validate +quit  
  
EXPOSE 27017  
WORKDIR /steamcmd

