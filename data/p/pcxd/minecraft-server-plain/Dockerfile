FROM java:8  
MAINTAINER pcxd  
  
ENV APT_GET_UPDATE 2016-04-23  
RUN apt-get update  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
imagemagick \  
lsof \  
nano \  
sudo \  
vim \  
jq \  
&& apt-get clean  
  
RUN mkdir /data \  
&& mkdir /plugins \  
&& chown bin:bin /data /plugins  
  
EXPOSE 25565 25575  
ADD
https://github.com/itzg/restify/releases/download/1.0.3/restify_linux_amd64
/usr/local/bin/restify  
COPY start.sh /start  
COPY start-minecraft.sh /start-minecraft  
RUN chmod +x /usr/local/bin/*  
RUN chmod +x /start  
RUN chmod +x /start-minecraft  
  
VOLUME ["/data","/plugins"]  
COPY server.properties /tmp/server.properties  
WORKDIR /data  
#COPY /plugins /plugins  
ENTRYPOINT [ "/start" ]  
  
ENV UID=2 GID=2 \  
MOTD="Play now" \  
RAM_OPTS="-Xmx2048M -Xms1024M" \  
JVM_OPTS="-XX:+UseG1GC -XX:+UnlockExperimentalVMOptions
-XX:MaxGCPauseMillis=100 -XX:+DisableExplicitGC -XX:TargetSurvivorRatio=90
-XX:G1NewSizePercent=50 -XX:G1MaxNewSizePercent=80
-XX:InitiatingHeapOccupancyPercent=10 -XX:G1MixedGCLiveThresholdPercent=50
-XX:+AggressiveOpts -XX:+AlwaysPreTouch" \  
TYPE=SPIGOT VERSION=LATEST MAX_PLAYERS=60 \  
ONLINE_MODE=TRUE CONSOLE=false EULA=TRUE ENABLE_QUERY=true ENABLE_RCON=true  

