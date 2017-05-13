FROM zoltanthedestroyer/minecraft-docker:java8
MAINTAINER Justin Barone https://github.com/cloudish https://hub.docker.com/u/zoltanthedestroyer/

ENV SERVER_URL https://github.com/MyM-ModpackTeam/GalacticScience/releases/download/1.6.4/Galactic.Science_1.6.4_Server.zip
ENV LAUNCHWRAPPER net/minecraft/launchwrapper/1.12/launchwrapper-1.12.jar

RUN curl -SL $SERVER_URL -o /tmp/server.zip && \
    unzip /tmp/server.zip -d /opt/minecraft && \
    mkdir -p /opt/minecraft/$(dirname libraries/${LAUNCHWRAPPER}) && \
    curl -S https://libraries.minecraft.net/$LAUNCHWRAPPER -o /opt/minecraft/libraries/$LAUNCHWRAPPER && \
    find /opt/minecraft -name "*.log" -exec rm -f {} \; && \
    rm -rf /opt/minecraft/ops.* /opt/minecraft/whitelist.* /opt/minecraft/logs/* /tmp/* && \
	chmod +x /opt/minecraft/ServerStart-Other.sh

ENV MINECRAFT_VERSION 1.7.10
ENV MINECRAFT_OPTS -server -Xms2048m -Xmx4096m -XX:MaxPermSize=256m -XX:+UseParNewGC -XX:+UseConcMarkSweepGC
ENV MINECRAFT_STARTUP_SCRIPT ServerStart-Other.sh
