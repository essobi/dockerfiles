# Minecraft Craftbukkit 1.7.9 Dockerfile  
FROM debian:wheezy  
MAINTAINER Tony Pai <tony77794@gmail.com>  
  
RUN apt-get -y update  
RUN apt-get -y install openjdk-7-jre-headless wget  
  
WORKDIR /data  
VOLUME /data  
  
COPY craftbukkit-1.7.9-R0.2-3092.jar ./craftbukkit-1.7.9-R0.2-3092.jar  
COPY server.properties ./server.properties  
  
EXPOSE 25565  
# Automatically accept Minecraft EULA, and start Minecraft server  
CMD echo eula=true > /data/eula.txt && java -Xms2G -jar
./craftbukkit-1.7.9-R0.2-3092.jar nogui --noconsole

