# SteamCMD  
#  
# Version 1.0.0  
FROM ubuntu:latest  
MAINTAINER Thomas Ingvarsson <ingvarsson.thomas@gmail.com>  
  
RUN apt-get -y update && \  
apt-get -y install curl lib32gcc1 lib32stdc++6 && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV USER steam  
ENV HOME /home/$USER  
env STEAMCMD_DIR $HOME/steamcmd  
  
RUN useradd $USER && \  
mkdir -p $STEAMCMD_DIR && \  
chown -R $USER:$USER $HOME  
  
RUN cd $STEAMCMD_DIR && \  
curl -s http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar
-vxz  
  
USER $USER  
WORKDIR $STEAMCMD_DIR  
  
CMD ["./steamcmd.sh"]

