FROM alpine:3.6  
MAINTAINER Yuxiang Zhu <vfreex+spigot@gmail.com>  
  
EXPOSE 25565  
WORKDIR /opt/spigot/data  
  
ARG SPIGOT_VERSION=1.10.2  
ARG SPIGOT_LINK=https://cdn.getbukkit.org/spigot/spigot-1.10.2-R0.1-SNAPSHOT-
latest.jar  
  
RUN apk --no-cache add ca-certificates wget openjdk8-jre-base && \  
adduser -D spigot && \  
mkdir -p /opt/spigot/lib && \  
mkdir -p /opt/spigot/data && \  
wget -O /opt/spigot/lib/spigot.jar "$SPIGOT_LINK" && \  
chown -R spigot: /opt/spigot && \  
apk del ca-certificates wget  
USER spigot  
CMD ["java", "-Dcom.mojang.eula.agree=true", "-jar",
"/opt/spigot/lib/spigot.jar"]  

