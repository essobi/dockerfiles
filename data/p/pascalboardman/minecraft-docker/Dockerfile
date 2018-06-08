############################################################  
# Dockerfile to build a minecraft server that works with supervisor  
# Based on Debian  
############################################################  
  
from debian:latest  
  
MAINTAINER lacsap  
  
RUN apt-get update  
RUN apt-get --yes install curl openjdk-7-jre-headless supervisor  
  
  
  
#Load scripts in the image  
add ./etc/supervisor/supervisord.conf /etc/supervisor/supervisord.conf  
add ./etc/supervisor/conf.d/minecraft.conf
/etc/supervisor/conf.d/minecraft.conf  
add ./server_start /server_start  
  
  
  
# make the start script executable  
run chmod +x /server_start  
  
  
# check if the jar is up to date (for now it only check if
minecraft_server.jar exist) and start the server  
expose 25565  
volume ["/data"]  
cmd ["/server_start"]  

