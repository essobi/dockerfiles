#Use the last steamcmd image  
FROM kamaradeivanov/steamcmd  
  
MAINTAINER kamaradeivanov  
  
######################## Set environment variables
#############################  
# Server Name  
ENV SERVER_NAME "pzServer"  
# Admin DB Password (required for the first launch)  
ENV ADMIN_PASSWORD "pzPassword"  
# Game UDP port to accept new player  
ENV UDP_GAME_PORT 16261  
# Game UDP port to allow player to contact the server (by default : 10 player)  
ENV UDP_PLAYER_PORTS 16262-16272  
# Game name  
ENV GAME_NAME "projectzomboid"  
# Game folder  
ENV GAME_FOLDER "/home/steam/${GAME_NAME}"  
# Steam game id  
ENV STEAM_GAME_ID "380870"  
#### ######################################################################
####  
  
  
#################### install prerequisite for the game
#########################  
# Switch to root to use apt-get  
USER root  
  
# Stop apt-get asking to get Dialog frontend  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Install dependencies and clean  
RUN apt-get update && apt-get install -y \  
default-jre \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Select the server as entry point  
COPY ./entrypoint.sh /home/steam/  
RUN chmod u+x /home/steam/entrypoint.sh  
  
# Switch to user steam  
USER steam  
#### ######################################################################
####  
  
  
########################### install project-zomboid
############################  
# Create ProjectZomboid folders  
RUN mkdir -p /home/steam/Zomboid &&\  
chown -R steam:steam /home/steam/Zomboid  
RUN mkdir -p ${GAME_FOLDER} &&\  
chown -R steam:steam ${GAME_FOLDER}  
  
# Download the game ProjectZomboid  
RUN /home/steam/steamcmd/steamcmd.sh +login anonymous \  
+force_install_dir ${GAME_FOLDER} \  
+app_update ${STEAM_GAME_ID} \  
+quit  
#### ######################################################################
####  
  
  
######################### Specify docker configuration
#########################  
# Make server port available to host : (10 slots)  
EXPOSE ${UDP_GAME_PORT}/udp ${UDP_PLAYER_PORTS}/udp  
  
# Persistant folder withe server data : /home/steam/Zomboid  
VOLUME /home/steam/Zomboid /srv/${GAME_NAME}  
#### ######################################################################
####  
  
########################## Set the entrypoint
##################################  
# Switch to root to use apt-get  
USER root  
  
# Select the script as entry point  
COPY ./entrypoint.sh /home/steam/  
RUN chmod u+x /home/steam/entrypoint.sh &&\  
chown -R steam:steam /home/steam/entrypoint.sh  
  
# Switch to user steam  
USER steam  
#### ######################################################################
####  
  
  
ENTRYPOINT ["/home/steam/entrypoint.sh"]  

