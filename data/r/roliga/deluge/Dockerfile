FROM debian:latest  
  
RUN apt-get update && apt-get install -y \  
deluged deluge-web && \  
apt-get clean  
  
COPY entrypoint.sh /usr/local/bin/  
  
# Web UI  
EXPOSE 8112/tcp  
# Deluge remote access  
EXPOSE 58846/tcp  
  
ENTRYPOINT [ "entrypoint.sh" ]  

