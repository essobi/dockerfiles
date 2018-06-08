FROM openjdk:jdk-alpine  
MAINTAINER Oliver Meyer <mail@iskaron.de>  
  
RUN apk update && apk add ca-certificates wget && update-ca-certificates &&
apk upgrade && \  
apk add --no-cache bash git openssh && \  
rm -rf /tmp/* && rm -rf /var/cache/apk/*  
  
ENV MINECRAFT_VERSION=1.12.2  
RUN mkdir /build /minecraft /data && cd /build && \  
wget
https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
&& \  
java -jar BuildTools.jar --rev $MINECRAFT_VERSION && \  
cp spigot-$MINECRAFT_VERSION.jar /minecraft/spigot.jar && \  
cd /minecraft && rm -rf /build  
  
RUN addgroup -g 1000 minecraft && adduser -D -G minecraft -s /bin/bash -u 1000
minecraft && \  
chown -R minecraft /minecraft /data  
  
RUN apk del git openssh && \  
rm -rf /tmp/* && rm -rf /var/cache/apk/*  
  
EXPOSE 25566/tcp  
EXPOSE 8123/tcp  
  
USER minecraft  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
ADD rcon /bin/rcon  
ENTRYPOINT /docker-entrypoint.sh  
  

