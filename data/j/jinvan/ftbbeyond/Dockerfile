FROM openjdk:alpine  
MAINTAINER Jin Van <usconan@gmail.com>  
  
ENV SERVER_PORT 25565  
  
WORKDIR /minecraft  
  
USER root  
  
COPY ./settings-local.sh /minecraft/cfg/settings-local.sh  
  
RUN adduser -D minecraft && \  
apk --no-cache add curl wget && \  
mkdir -p /minecraft/world && \  
mkdir -p /minecraft/cfg && \  
mkdir -p /minecraft/backups &&\  
curl -SLO
http://ftb.cursecdn.com/FTB2/modpacks/FTBBeyond/1_11_0/FTBBeyondServer.zip &&
\  
unzip FTBBeyondServer.zip && \  
chmod u+x *.sh && \  
echo "eula=true" > /minecraft/eula.txt && \  
echo "[]" > /minecraft/cfg/ops.json && \  
echo "[]" > /minecraft/cfg/whitelist.json && \  
echo "[]" > /minecraft/cfg/banned-ips.json && \  
echo "[]" > /minecraft/cfg/banned-players.json && \  
echo "[]" > /minecraft/cfg/server.properties && \  
ln -s /minecraft/cfg/ops.json /minecraft/ops.json && \  
ln -s /minecraft/cfg/whitelist.json /minecraft/whitelist.json && \  
ln -s /minecraft/cfg/banned-ips.json /minecraft/banned-ips.json && \  
ln -s /minecraft/cfg/banned-players.json /minecraft/banned-players.json && \  
ln -s /minecraft/cfg/server.properties /minecraft/server.properties && \  
ln -s /minecraft/cfg/settings-local.sh /minecraft/settings-local.sh && \  
  
chown -R minecraft:minecraft /minecraft  
  
USER minecraft  
  
RUN /minecraft/FTBInstall.sh  
  
VOLUME ["/minecraft/world"]  
VOLUME ["/minecraft/cfg"]  
VOLUME ["/minecraft/backups"]  
  
EXPOSE ${SERVER_PORT}  
  
CMD ["/bin/sh", "/minecraft/ServerStart.sh"]  

