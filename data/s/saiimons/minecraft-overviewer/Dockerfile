# To use this Docker image, make sure you set up the mounts properly.  
#  
# The Minecraft server files are expected at  
# /home/minecraft/server  
#  
# The Minecraft-Overviewer render will be output at  
# /home/minecraft/render  
FROM debian:latest  
  
MAINTAINER Mark Ide Jr (https://www.mide.io)  
  
RUN apt-get update && \  
apt-get install -y wget gnupg cron && \  
echo "deb http://overviewer.org/debian ./" >> /etc/apt/sources.list && \  
wget -O - https://overviewer.org/debian/overviewer.gpg.asc | apt-key add - &&
\  
apt-get update && \  
apt-get install -y minecraft-overviewer && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
mkdir -p /home/minecraft/render /home/minecraft/server /home/minecraft/scripts  
  
COPY config/config.py /home/minecraft/config.py  
COPY entrypoint.sh /home/minecraft/entrypoint.sh  
COPY faithful.zip /home/minecraft/texture.zip  
COPY scripts/* /home/minecraft/scripts/  
  
WORKDIR /home/minecraft/  
  
EXPOSE 8080  
VOLUME ["/home/minecraft/render", "/home/minecraft/server"]  
  
CMD ["bash", "/home/minecraft/entrypoint.sh"]  

