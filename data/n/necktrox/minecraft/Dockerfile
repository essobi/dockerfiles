FROM openjdk:7-jre-alpine  
  
ENV MINECRAFT_VERSION 1.11.2  
RUN apk add --no-cache \  
wget \  
ca-certificates  
  
# Download Minecraft Server components  
RUN wget -q
https://s3.amazonaws.com/Minecraft.Download/versions/$MINECRAFT_VERSION/minecraft_server.$MINECRAFT_VERSION.jar
-O minecraft_server.jar  
  
# Sets working directory for the CMD instruction  
WORKDIR /data  
VOLUME /data  
  
# Expose the container's network port: 25565 during runtime.  
EXPOSE 25565  
# Automatically accept Minecraft EULA, and start Minecraft server  
CMD echo eula=true > /data/eula.txt && java -Xms1G -Xmx4G -XX:MaxPermSize=128M
-XX:+UseConcMarkSweepGC -jar /minecraft_server.jar  

