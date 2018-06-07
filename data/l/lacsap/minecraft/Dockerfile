############################################################  
# Dockerfile to build a minecraft server  
############################################################  
  
from java:8  
  
# Change the memory limit and version of the minecraft server  
ENV MEMORY 1024  
ENV VERSION 1.10.2  
  
RUN apt-get update  
RUN apt-get --yes install curl  
  
COPY server_start /server_start  
  
WORKDIR /data/  
  
expose 25565  
volume ["/data"]  
cmd ["/server_start"]  

