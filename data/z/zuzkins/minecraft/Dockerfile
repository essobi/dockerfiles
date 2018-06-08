# Minecraft Server image  
FROM openjdk:8-jre-alpine  
  
MAINTAINER Jiri Zuna <jiri@zunovi.cz>  
  
ENV MINECRAFT_VERSION=1.12.2  
# Install wget and certificates  
RUN apk update \  
&& apk add ca-certificates wget \  
&& update-ca-certificates  
  
# Download the server jar file  
RUN mkdir -p /opt/minecraft \  
&& cd /opt/minecraft \  
&& wget -q
https://s3.amazonaws.com/Minecraft.Download/versions/$MINECRAFT_VERSION/minecraft_server.$MINECRAFT_VERSION.jar  
  
WORKDIR /data  
VOLUME /data  
  
EXPOSE 25565  
CMD echo eula=true > /data/eula.txt && java -jar
/opt/minecraft/minecraft_server.$MINECRAFT_VERSION.jar  

