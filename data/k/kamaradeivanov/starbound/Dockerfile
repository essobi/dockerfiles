#Use the last steamcmd image  
FROM kamaradeivanov/steamcmd  
  
MAINTAINER kamaradeivanov  
  
######################## Set environment variables
#############################  
# Game TCP port to accept new player  
ENV TCP_GAME_PORT 21025  
# Game name  
ENV GAME_NAME "starbound"  
# Game folder  
ENV GAME_FOLDER "/home/steam/${GAME_NAME}"  
# Steam game id  
ENV STEAM_GAME_ID "211820"  
#### ######################################################################
####  
  
  
########################### install starbound ############################  
# Create Starbound folders  
RUN mkdir -p ${GAME_FOLDER} &&\  
chown -R steam:steam ${GAME_FOLDER}  
  
# Starbound dont have anonymous access on steamcmd,  
# game will be installed into the entrypoint script  
#### ######################################################################
####  
  
  
######################### Specify docker configuration
#########################  
# Make server port available to host  
EXPOSE ${TCP_GAME_PORT}/tcp  
  
# Persistant folder withe server data  
VOLUME ${GAME_FOLDER} /srv/${GAME_NAME}  
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

