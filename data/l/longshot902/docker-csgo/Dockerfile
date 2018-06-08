FROM longshot902/docker-steamcmd  
  
MAINTAINER Jeff Nelson <longshot902@gmail.com>  
  
## Create Environment Variables  
## Game Specific  
ENV GAME="csgo"  
ENV STEAM_APP="740"  
ENV STEAMCMD_USER="anonymous"  
ENV STEAMCMD_PASSWORD=""  
ENV STEAMCMD_AUTH_CODE=""  
## Steam Specific  
ENV USER steam  
ENV SERVER_DIRECTORY /home/$USER  
ENV GAME_DIRECTORY $SERVER_DIRECTORY/$GAME  
## Add files  
ADD start.sh $GAME_DIRECTORY/  
  
## Assign user permissions  
USER $USER  
RUN sudo chmod u+x -R $SERVER_DIRECTORY  
RUN sudo chown $USER:$USER -R $SERVER_DIRECTORY  
## Update to latest CSGO  
RUN $SERVER_DIRECTORY/steamcmd.sh +login $STEAMCMD_USER $STEAMCMD_PASSWORD
$STEAMCMD_AUTH_CODE +force_install_dir $GAME_DIRECTORY +app_update $STEAM_APP
+quit  
  
## Open default ports  
EXPOSE 27015/udp  
  
## Set working directory and normal start up process  
WORKDIR $SERVER_DIRECTORY/$GAME  
ENTRYPOINT ["./start.sh"]  
CMD ["+game_type", "0", "+game_mode", "0", "+mapgroup", "mg_active", "+map",
"de_dust2"]  

