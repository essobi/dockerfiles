FROM alpine:latest  
  
LABEL maintainer "docker@marcermarc.de"  
# --------------  
# Define version  
# --------------  
ARG VERSION=latest  
  
#
-----------------------------------------------------------------------------------------------------------  
# Define heap and extra params  
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
# --------------------------  
# Download and install forge  
# Compile Start.java  
# Add user minecraft  
# --------------------------  
RUN mkdir -p /opt/minecraft /mnt/minecraft /opt/start /tmp/install \  
&& apk add \--update \--no-cache \--virtual=.build-dependencies jq openjdk8
curl \  
&& cd /tmp/install \  
&& if [ "$VERSION" = "latest" ]; then INDEX="index"; else
INDEX="index_${VERSION}"; fi \  
&& curl -o forge-install.jar
"https://files.minecraftforge.net/maven/net/minecraftforge/forge/$(curl
https://files.minecraftforge.net/maven/net/minecraftforge/forge/${INDEX}.json
| jq --raw-output '.md.versions | map(select(.marker ==
"LATEST"))[0].classifiers.installer.path')" \  
&& cd /opt/minecraft \  
&& java -jar /tmp/install/forge-install.jar \--installServer \  
&& mv forge-*.jar forge.jar \  
&& rm -rf /tmp/install /opt/minecraft/forge-install.jar.log
/opt/minecraft/mods \  
&& cd /opt/start \  
&& curl -o Start.java
https://raw.githubusercontent.com/marcermarc/DockerMinecraft/master/StartProgram/Start.java
\  
&& /usr/lib/jvm/java-1.8-openjdk/bin/javac /opt/start/Start.java \  
&& chmod +x /opt/start/Start.class \  
&& apk del \--no-cache .build-dependencies \  
&& apk add \--no-cache openjdk8-jre-base \  
&& adduser -D minecraft \  
&& chown -R minecraft /mnt/minecraft /opt/minecraft \  
&& chmod -R 777 /mnt/minecraft /opt/minecraft  
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
ENTRYPOINT ["java", "Start", "java -Xmx&HEAP& -Xms&HEAP& &PARAMS& -d64 -jar
/opt/minecraft/forge.jar nogui", "/mnt/minecraft"]

