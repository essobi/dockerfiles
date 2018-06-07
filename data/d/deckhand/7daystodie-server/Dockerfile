FROM debian  
  
MAINTAINER images@docker.li <images@docker.li>  
  
# update system and install dependencies  
RUN apt-get update && apt-get install -qy lib32gcc1 curl sudo  
  
# create steam user  
RUN groupadd steam && useradd -g steam -ms /bin/bash steam  
  
# create base dir for steamcmd and get latest steamcmd  
RUN sudo -u steam mkdir /home/steam/steamcmd/ && \  
cd /home/steam/steamcmd/ && \  
sudo -u steam curl -sqL
"https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" |
sudo -u steam tar zxvf -  
  
# install 7days to die server from steam  
RUN sudo -u steam /home/steam/steamcmd/steamcmd.sh \  
+login anonymous \  
+force_install_dir /home/steam/server/7d2d/ \  
+app_update 294420 \  
+quit  
  
# copy start script into image  
COPY startserver.sh /home/steam/server/7d2d/startserver.sh  
  
# copy config into image  
COPY serverconfig.xml /home/steam/server/7d2d/serverconfig.xml  
  
# set prober permissions  
RUN chown steam:steam /home/steam/server/7d2d/startserver.sh && \  
chown steam:steam /home/steam/server/7d2d/serverconfig.xml && \  
chmod +x /home/steam/server/7d2d/startserver.sh  
  
# expose needed ports  
EXPOSE 26900  
# start  
ENTRYPOINT ["/home/steam/server/7d2d/startserver.sh",
"-configfile=/home/steam/server/7d2d/serverconfig.xml"]  

