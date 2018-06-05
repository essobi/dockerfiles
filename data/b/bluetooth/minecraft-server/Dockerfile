FROM openjdk:8-jre  
  
MAINTAINER BlueTooth  
  
RUN apt-get -y update && \  
apt-get -y install wget && \  
mkdir /data  
  
WORKDIR /data  
VOLUME /data  
  
EXPOSE 25565  
CMD wget -qN https://launchermeta.mojang.com/mc/game/version_manifest.json &&
\  
VER=`sed -n -e 's/.*release\":\"\\([1-9.]*\\).*/\1/p' < version_manifest.json`
&& \  
wget --output-document=minecraft_server.jar
https://s3.amazonaws.com/Minecraft.Download/versions/$VER/minecraft_server.$VER.jar
&& \  
echo eula=true > eula.txt && \  
java -Xmx4096M -Xms4096M -jar minecraft_server.jar  

