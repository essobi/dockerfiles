FROM chiefalexander/steamcmd  
  
EXPOSE 7787 7788 27165 27166  
RUN set -xe \  
&& ./Steam/steamcmd.sh +login anonymous +force_install_dir ~/squad +app_update
403240 +quit  
  
ENTRYPOINT ["./squad/SquadServer.sh", "MULTIHOME=0.0.0.0", "Port=7787",
"QueryPort=27165"]  

