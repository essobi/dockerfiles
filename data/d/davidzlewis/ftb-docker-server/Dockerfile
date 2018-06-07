FROM dlord/minecraft  
MAINTAINER Lima3Whiskey  
  
ENV FTB_URL http://addons-
origin.cursecdn.com/files/2269/309/FTBInfinityServer.zip  
ENV LAUNCHWRAPPER net/minecraft/launchwrapper/1.11/launchwrapper-1.11.jar  
ENV MINECRAFT_HOME /opt/ftb  
ENV MINECRAFT_EULA true  
ENV DEFAULT_OP dinnerbone  
  
RUN \  
curl -S $FTB_URL -o /tmp/ftb.zip && \  
unzip /tmp/ftb.zip -d $MINECRAFT_HOME && \  
mkdir -p $MINECRAFT_HOME/libraries && \  
#curl -S https://libraries.minecraft.net/$LAUNCHWRAPPER -o
$MINECRAFT_HOME/libraries/$LAUNCHWRAPPER && \  
find $MINECRAFT_HOME -name "*.log" -exec rm -f {} \; && \  
rm -rf $MINECRAFT_HOME/ops.* $MINECRAFT_HOME/whitelist.*
$MINECRAFT_HOME/logs/* /tmp/*  
  
RUN mv /opt/ftb/FTBServer* /opt/ftb/FTBServer.jar  
  
ENV MINECRAFT_VERSION 1.7.10  
ENV MINECRAFT_OPTS -server -Xms2048m -Xmx3072m -XX:MaxPermSize=256m
-XX:+UseParNewGC -XX:+UseConcMarkSweepGC  
ENV MINECRAFT_STARTUP_JAR FTBServer.jar  
EXPOSE 25565/tcp  

