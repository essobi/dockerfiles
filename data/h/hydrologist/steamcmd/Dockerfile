# escape=`  
FROM ubuntu:16.04  
  
HEALTHCHECK NONE  
  
# add a new user  
RUN useradd -m -G games steam  
  
# install steamcmd  
RUN dpkg --add-architecture i386 &&`  
apt-get update &&`  
apt-get upgrade -y &&`  
apt-get install -y ca-certificates `  
lib32gcc1 `  
libstdc++6:i386 `  
tmux &&`  
echo debconf steam/question select I AGREE | debconf-set-selections &&`  
apt-get install -y steamcmd &&`  
apt-get clean &&`  
ln -s /usr/games/steamcmd /home/steam/steamcmd  
  
USER steam  
  
# Update steamcmd  
RUN /home/steam/steamcmd +quit  
  
ENTRYPOINT ["/bin/bash"]  
  
ONBUILD ENTRYPOINT ["/bin/bash"]  
  
ONBUILD USER root  

