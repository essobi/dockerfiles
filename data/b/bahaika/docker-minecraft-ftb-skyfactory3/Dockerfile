# This is based on itzg/minecraft-server  
FROM java:8  
MAINTAINER Jeremy SEBAN  
  
ENV VERSION=3.0.13  
RUN apt-get update && apt-get install -y wget unzip  
RUN addgroup --gid 1234 minecraft  
RUN adduser --disabled-password --home=/data --uid 1234 --gid 1234 --gecos
"minecraft user" minecraft  
  
RUN mkdir /tmp/feed-the-beast && cd /tmp/feed-the-beast && \  
wget -c https://addons-
origin.cursecdn.com/files/2435/246/FTBPresentsSkyfactory3Server_3.0.13.zip -O
FTBInfinityServer.zip && \  
unzip FTBInfinityServer.zip && \  
rm FTBInfinityServer.zip && \  
bash -x FTBInstall.sh && \  
chown -R minecraft /tmp/feed-the-beast  
  
USER minecraft  
  
EXPOSE 25565  
ADD start.sh /start  
  
VOLUME /data  
ADD server.properties /tmp/server.properties  
WORKDIR /data  
  
CMD /start  
  
ENV MOTD A Minecraft (FTB SkyFactory 3 ${VERSION}) Server Powered by Docker  
ENV LEVEL world  
ENV JVM_OPTS -Xms2048m -Xmx2048m  

