FROM dlord/minecraft:java8  
MAINTAINER John Paul Alcala jp@jpalcala.com  
  
ENV REGROWTH_URL
http://ftb.cursecdn.com/FTB2/modpacks/Regrowth/1_0_1/RegrowthServer.zip  
  
RUN curl -S $REGROWTH_URL -o /tmp/regrowth.zip && \  
unzip /tmp/regrowth.zip -d /opt/minecraft && \  
find /opt/minecraft -name "*.log" -exec rm -f {} \; && \  
rm -rf /opt/minecraft/ops.* /opt/minecraft/whitelist.* /opt/minecraft/logs/*
/tmp/*  
  
ENV MINECRAFT_VERSION 1.7.10  
ENV MINECRAFT_OPTS -server -Xms2048m -Xmx3072m -XX:MaxPermSize=256m
-XX:+UseParNewGC -XX:+UseConcMarkSweepGC  
ENV MINECRAFT_STARTUP_JAR forge-1.7.10-10.13.4.1558-1.7.10-universal.jar  

