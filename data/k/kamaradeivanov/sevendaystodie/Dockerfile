#Use the last steamcmd image  
FROM kamaradeivanov/steamcmd  
  
MAINTAINER kamaradeivanov  
  
######################## Set environment variables
#############################  
# Server Name  
ENV SERVER_NAME "sdtdServer"  
# Admin DB Password (required for the first launch)  
ENV ADMIN_PASSWORD "sdtdPassword"  
# Game port  
ENV TCP_GAME_PORT 26900  
ENV UDP_GAME_PORT 26900-26902  
# Game name  
ENV GAME_NAME "sevendaystodie"  
# Game folder  
ENV GAME_FOLDER "/home/steam/${GAME_NAME}"  
# Steam game id  
ENV STEAM_GAME_ID "294420"  
#### ######################################################################
####  
  
  
###################### install prerequisite for the game
#######################  
# Switch to root to use apt-get  
USER root  
  
# Stop apt-get asking to get Dialog frontend  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Install dependencies and clean  
RUN apt-get update && apt-get install -y \  
libvorbisfile3\  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Select the server as entry point  
COPY ./entrypoint.sh /home/steam/  
RUN chmod u+x /home/steam/entrypoint.sh  
  
# Switch to user steam  
USER steam  
#### ######################################################################
####  
  
  
################### install the game server with steamcmd
######################  
# Create game folders  
RUN mkdir -p ${GAME_FOLDER} &&\  
chown -R steam:steam ${GAME_FOLDER}  
  
# Download the game  
RUN /home/steam/steamcmd/steamcmd.sh +login anonymous \  
+force_install_dir ${GAME_FOLDER} \  
+app_update ${STEAM_GAME_ID} \  
+quit  
#### ######################################################################
####  
  
  
######################### Specify docker configuration
#########################  
# Make server port available to host  
EXPOSE ${TCP_GAME_PORT}/tcp ${UDP_GAME_PORT}/udp  
  
# Persistant folder withe server data  
VOLUME ${GAME_FOLDER} /srv/${GAME_NAME}  
#### ######################################################################
####  
  
# Select the server as entry point  
COPY ./entrypoint.sh /home/steam/  
  
ENTRYPOINT ["/home/steam/entrypoint.sh"]  

