############################################################  
# Dockerfile to build a forge minecraft server  
############################################################  
  
from java:8  
  
# Change the memory limit and version of the minecraft server  
ENV MEMORY 1024  
ENV MCVERSION 1.8  
ENV FORGEVERSION recommended  
  
RUN apt-get update  
RUN apt-get --yes install curl  
  
# Load scripts in the image  
COPY server_start /server_start  
  
WORKDIR /data/  
  
expose 25565  
volume ["/data"]  
cmd ["/server_start"]  

