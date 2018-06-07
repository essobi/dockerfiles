############################################################  
# Dockerfile to build a deluge-web server  
############################################################  
FROM debian:8  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \  
deluge-web \  
deluged  
  
# this is where the configs will be stored  
VOLUME /data  
  
# this is where the torrents will be downloaded  
VOLUME /torrent  
  
EXPOSE 8112  
CMD ["deluge-web", "-c", "/data/"]  

