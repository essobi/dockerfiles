FROM sequel7/csgo  
  
# SteamCMD should not be used as root, here we set up user and variables  
USER steam  
WORKDIR /opt/steamcmd  
  
# Install CS:GO  
RUN /opt/steamcmd/steamcmd.sh \  
+login anonymous \  
+force_install_dir /opt/server/ \  
+app_update 740 validate \  
+quit  
  
# Execution vector  
ENTRYPOINT /opt/steamcmd/start.sh  

