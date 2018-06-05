FROM dlord/minecraft:java8  
MAINTAINER John Paul Alcala jp@jpalcala.com  
  
ENV FTB_INFINITY_URL
http://ftb.cursecdn.com/FTB2/modpacks/FTBInfinity/2_6_0/FTBInfinityServer.zip  
ENV LAUNCHWRAPPER net/minecraft/launchwrapper/1.12/launchwrapper-1.12.jar  
  
RUN curl -SL $FTB_INFINITY_URL -o /tmp/infinity.zip && \  
unzip /tmp/infinity.zip -d /opt/minecraft && \  
mkdir -p /opt/minecraft/$(dirname libraries/${LAUNCHWRAPPER}) && \  
curl -S https://libraries.minecraft.net/$LAUNCHWRAPPER -o
/opt/minecraft/libraries/$LAUNCHWRAPPER && \  
find /opt/minecraft -name "*.log" -exec rm -f {} \; && \  
rm -rf /opt/minecraft/ops.* /opt/minecraft/whitelist.* /opt/minecraft/logs/*
/tmp/*  
  
ENV MINECRAFT_VERSION 1.7.10  
ENV MINECRAFT_OPTS -server -Xms2048m -Xmx3072m -XX:MaxPermSize=256m
-XX:+UseParNewGC -XX:+UseConcMarkSweepGC  
ENV MINECRAFT_STARTUP_JAR FTBServer-1.7.10-1614.jar  
  
VOLUME /opt/minecraft  

