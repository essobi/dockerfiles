FROM phusion/baseimage  
  
MAINTAINER Luke Robles <lukelrobles@gmail.com>  
  
# Install packages  
RUN apt-get update && apt-get install -y wget unzip  
  
# Download and unzip OpenArena  
RUN wget https://www.dropbox.com/s/a1fadziu0vf8mf3/OpenArena-0.8.8.zip?dl=1 -O
/opt/OpenArena-0.8.8.zip  
RUN cd /opt && unzip OpenArena-0.8.8.zip -d /opt && rm
/opt/OpenArena-0.8.8.zip  
  
# Add config files  
ADD ./conf/server1.cfg /opt/openarena-0.8.8/baseoa/server1.cfg  
ADD ./conf/maprotation1.cfg /opt/openarena-0.8.8/baseoa/maprotation1.cfg  
  
# Expose ports  
EXPOSE 27950/udp  
EXPOSE 27960/udp  
  
# Run startup script  
ENTRYPOINT /opt/openarena-0.8.8/oa_ded.x86_64 +exec server1.cfg +set fs_game
corkscrew %1 %2 %3 %4 %5 %6 %7 %8 %9  
  
# Use this entry point for a vanilla server  
# ENTRYPOINT /opt/openarena-0.8.8/oa_ded.x86_64 +set dedicated 1 +exec
server1.cfg  

