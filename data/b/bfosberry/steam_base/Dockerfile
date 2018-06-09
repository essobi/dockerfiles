# SteamCmd Base  
#  
# VERSION 0.1  
FROM bfosberry/gamekick_base  
MAINTAINER bfosberry  
  
USER root  
# install prerequisites  
RUN apt-get -y install lib32gcc1 lib32z1 lib32ncurses5 lib32bz2-1.0
lib32stdc++6 gdb  
  
USER appuser  
# set up env  
RUN mkdir -p /opt/steam  
RUN mkdir -p /opt/server  
RUN mkdir -p /opt/data  
  
ENV STEAMDIR /opt/steam  
ENV SERVERDIR /opt/server  
RUN mkdir -p $STEAMDIR  
  
ENV PATH /opt/server/scripts/:$PATH  
  
# download steamcmd  
RUN wget -O - http://media.steampowered.com/client/steamcmd_linux.tar.gz | tar
-C $STEAMDIR -xvz  
  
# install steamcmd  
RUN $STEAMDIR/steamcmd.sh +quit  
RUN mkdir -p $HOME/.steam/sdk32  
RUN ln -s $STEAMDIR/linux32/steamclient.so /$HOME/.steam/sdk32/steamclient.so  

