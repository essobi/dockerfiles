FROM alpine:latest  
ENV VERSION 1.11.2  
RUN mkdir -p /minecraft/jar /minecraft/server  
ADD run.sh /minecraft/run.sh  
WORKDIR /tmp  
RUN apk add --no-cache git openjdk8-jre openssl && \  
wget
https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
&& \  
java -jar BuildTools.jar --rev $VERSION && \  
mv spigot* /minecraft/jar/spigot.jar && \  
rm -Rf * && \  
apk del git openssl && \  
adduser -H -D -s /bin/sh minecraft && \  
chown -R minecraft /minecraft  
VOLUME ['/minecraft/server']  
WORKDIR /minecraft/server  
USER minecraft  
CMD sh /minecraft/run.sh

