FROM debian:stretch  
  
MAINTAINER rainbowdashboard  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
ADD steamcmd.tar.xz /  
ADD run-game.sh /  
  
EXPOSE 27015/tcp  
EXPOSE 27015/udp  
EXPOSE 27016/tcp  
EXPOSE 27016/udp  
EXPOSE 27017/tcp  
EXPOSE 27017/udp  
  
RUN dpkg --add-architecture i386; apt-get update; \  
apt-get install -y binutils ca-certificates libgcc1:i386 libstdc++6:i386
libtbb2:i386 libterm-ui-perl locales locales-all net-tools wine wine32 wine64
libwine libwine:i386 fonts-wine; \  
export WINEARCH='win64';wine wineboot --init; steamcmd +quit; steamcmd
+@sSteamCmdForcePlatformType windows +login anonymous +force_install_dir
/home/pixark +app_update 824360 validate +quit; \  
rm -rf /root/.steam/logs/* /var/lib/apt/lists/* /tmp/*  
RUN mv /run-game.sh /home/pixark/run-game.sh  
RUN chmod +x /home/pixark/run-game.sh  
  
CMD ["/home/pixark/run-game.sh"]  

