FROM ubuntu:14.04  
  
ENV MINECRAFT_URL=https://s3.amazonaws.com/Minecraft.Download/versions  
ENV MINECRAFT_VERSION=1.12.2  
ENV
MINECRAFT_DOWNLOAD_URL=${MINECRAFT_URL}/${MINECRAFT_VERSION}/${MINECRAFT_VERSION}.jar  
ENV RENDER=true  
ENV POI=true  
RUN apt-get update && \  
apt-get install -y wget && \  
echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list && \  
echo "deb http://overviewer.org/debian ./" >> /etc/apt/sources.list && \  
apt-get update  
  
RUN apt-get install -y --force-yes \  
minecraft-overviewer  
  
COPY start-overviewer.sh /  
RUN chmod 766 start-overviewer.sh  
  
RUN wget ${MINECRAFT_DOWNLOAD_URL} -P /versions/  
  
ENTRYPOINT ["bin/bash", "-c", "/start-overviewer.sh"]  

