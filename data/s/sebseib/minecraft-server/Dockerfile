##########################  
# Docker Minecraft Server  
# Based on Spigot  
# sebseib, 23.08.2017  
##########################  
  
#STEP1: Build Spigot  
FROM openjdk:latest as builder  
MAINTAINER seibseb@gmail.com  
RUN mkdir /TEMP  
WORKDIR /TEMP  
RUN apt-get update  
RUN apt-get install -y wget git  
RUN wget
https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar  
RUN java -jar BuildTools.jar --rev 1.12.2  
  
#STEP2: Multistaged: copy builded jar file from STEP1  
FROM ubuntu:16.04  
MAINTAINER seibseb@gmail.com  
RUN apt-get update  
RUN apt-get install -y openjdk-8-jre  
RUN mkdir /opt/minecraft  
WORKDIR /opt/minecraft  
RUN mkdir bin  
RUN mkdir home  
COPY --from=builder /TEMP/spigot-*.jar bin/spigot.jar  
ENV MC_MEMORY_INIT=512M  
ENV MC_MEMORY_MAX=1024M  
  
COPY ./start.sh start.sh  
RUN chmod 775 start.sh  
CMD /opt/minecraft/start.sh  

