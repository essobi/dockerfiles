FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get install -y lib32gcc1 wget  
RUN wget -q
https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz  
WORKDIR /data  
VOLUME /data  
EXPOSE 27015  
CMD tar -xvzf /steamcmd_linux.tar.gz  
CMD steamcmd +login anonymous +force_install_dir /data +app_update 376030
+quit  
CMD ./ShooterGameServer TheIsland?listen?SessionName=Another ARK
Server?ServerPassword=123?ServerAdminPassword=456 -server -log

