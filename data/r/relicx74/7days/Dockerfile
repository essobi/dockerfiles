FROM relicx74/steamcmd  
ENV APP=294420  
ENV BETA_VERSION=alpha16.4  
ENV APP_DIR=/game  
ENV STEAM_DIR=/steamcmd  
  
WORKDIR /$APP_DIR  
RUN $STEAM_DIR/steamcmd.sh +login anonymous \  
+force_install_dir $APP_DIR \  
+app_update 294420 \  
+quit  
VOLUME sevendays-experimental:/game/Data  
EXPOSE 8080/udp 26900/udp  
ENTRYPOINT ["/game/startserver.sh", "-configfile=serverconfig.xml"]  
  
#Volume mounts are shared between containers when used across a scaled docker
service - containers running on multiple hosts should be able to make
modifications visible on another active container immediately  
#Outside of a Docker swarm, unsure,  
#Also more efficient (native host I/O) as opposed to bind mounts (eg: docker
run -v [hostpath]:[containerpath] [imagename] )  
#1 UDP game port 26900  
#Control Panel port 8080  
#Web port = CP +1 ??  
#docker run -v $PWD:/data -p 26900:26900/udp -p 8080:8080/udp -d --name
"7days" --restart="always" relicx74/7days  
#docker-compose up will launch this as a service with scale=1 (run on a single
host). may require docker swarm init (even if you have a 'swarm' of one)  
#Versions - List of release/prerelease builds  
#https://steamdb.info/app/251570/depots/ versions

