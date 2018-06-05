FROM ubuntu:17.10  
LABEL maintainer="pfliegel.sebastian@gmail.com"  
  
ENV APPID=805140  
ENV PUBLICIP=0.0.0.0  
ENV DEBIAN_FRONTEND=noninteractive  
  
EXPOSE 7777-7780  
RUN apt-get update && \  
apt-get install -y curl lib32gcc1 xdg-user-dirs  
  
WORKDIR /  
RUN mkdir steamcmd && \  
curl -sqL \  
"https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" | \  
tar zxvf - -C ./steamcmd && \  
/steamcmd/steamcmd.sh +quit && \  
/steamcmd/steamcmd.sh \  
+login anonymous \  
+force_install_dir /battalion_tmp \  
+app_update ${APPID} validate \  
+quit && \  
mv /battalion_tmp/Linux /battalion && \  
mv /battalion_tmp/version.txt /battalion && \  
rm -rf /battalion_tmp && rm -rf /steamcmd && \  
rm -rf /root/.steam && rm -rf /root/Steam  
WORKDIR /battalion  
  
CMD ./Battalion/Binaries/Linux/BattalionServer \  
/Game/Maps/Final_Maps/Derailed?Game=/Script/ShooterGame.BombGameMode?listen \  
-broadcastip="${PUBLICIP}" \  
-PORT=7777 \  
-QueryPort=7780 \  
-log \  
-defgameini="../../../DefaultGame.ini"  

