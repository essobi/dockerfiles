FROM alpine:latest  
  
LABEL maintainer "docker@marcermarc.de"  
# -------------------------------------  
# Define version, heap and extra params  
# -------------------------------------  
ARG VERSION=latest  
  
#
-----------------------------------------------------------------------------------------------------------  
# Default extra params from:  
# https://aquifermc.org/threads/optimizing-paper-remove-lag-spikes-fix-tps-
improve-performance.101/#post-822  
# Set the classpath can start the Start.class  
#
-----------------------------------------------------------------------------------------------------------  
ENV HEAP=2G \  
PARAMS="-XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:MaxGCPauseMillis=100
-XX:+DisableExplicitGC -XX:TargetSurvivorRatio=90 -XX:G1NewSizePercent=50
-XX:G1MaxNewSizePercent=80 -XX:InitiatingHeapOccupancyPercent=10
-XX:G1MixedGCLiveThresholdPercent=50 -XX:+AggressiveOpts -XX:+AlwaysPreTouch
-XX:+UseLargePagesInMetaspace" \  
CLASSPATH=/opt/start  
# ------------------------------  
# Compile Spigot with BuildTools  
# Compile Start.java  
# Add user minecraft  
# ------------------------------  
RUN mkdir -p /tmp/buildtool /opt/minecraft /mnt/minecraft /opt/start \  
&& apk add \--update \--no-cache \--virtual=.build-dependencies git wget
openjdk8 \  
&& cd /tmp/buildtool \  
&& wget
https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
\  
&& java -jar BuildTools.jar \--rev $VERSION \  
&& mv spigot-*.jar /opt/minecraft/spigot.jar \  
&& rm -rf /tmp/buildtool \  
&& cd /opt/start \  
&& wget
https://raw.githubusercontent.com/marcermarc/DockerMinecraft/master/StartProgram/Start.java
\  
&& /usr/lib/jvm/java-1.8-openjdk/bin/javac /opt/start/Start.java \  
&& chmod +x /opt/start/Start.class \  
&& apk del \--no-cache .build-dependencies \  
&& apk add \--no-cache openjdk8-jre-base \  
&& adduser -D minecraft \  
&& chown -R minecraft /mnt/minecraft \  
&& chmod -R 777 /mnt/minecraft  
# ------------  
# Expose ports  
# ------------  
EXPOSE 25565:25565/tcp 25565:25565/udp  
  
# -------------  
# Define volume  
# -------------  
VOLUME ["/mnt/minecraft"]  
  
# ----------------  
# Set startup user  
# ----------------  
USER minecraft  
  
#
---------------------------------------------------------------------------------------  
# Start the Start.class with two parameters:  
# 1. The minecraft execute command ([HEAP] and [PARAM] are replaced by the
startprogram)  
# 2. The minecraft workdir  
#
---------------------------------------------------------------------------------------  
ENTRYPOINT ["java", "Start", "java -Xmx&HEAP& -Xms&HEAP& &PARAMS& -d64
-Dcom.mojang.eula.agree=true -Dfile.encoding=UTF-8 -jar
/opt/minecraft/spigot.jar nogui", "/mnt/minecraft"]

