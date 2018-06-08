FROM ubuntu:trusty  
  
ENV USER=steam  
ENV HOME=/home/$USER  
  
RUN dpkg --add-architecture i386 && \  
apt-get update -y && \  
apt-get install -y curl lib32gcc1 lib32stdc++6 libstdc++6:i386 && \  
useradd -m $USER  
  
USER $USER  
WORKDIR $HOME  
RUN curl -sqL
"https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" | tar
zxvf - && \  
$HOME/steamcmd.sh +quit && \  
ln -s $HOME/linux32 $HOME/.steam/sdk32  

