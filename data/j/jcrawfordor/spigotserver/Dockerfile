FROM openjdk:8-jdk-alpine  
  
RUN apk --no-cache add bash git  
ADD
https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
/root/BuildTools.jar  
RUN cd /root && java -jar /root/BuildTools.jar --rev 1.11.2 && mv spigot-*.jar
spigot.jar  
RUN mv /root/spigot.jar /spigot.jar && rm -rf /root/*  
RUN adduser -S -h /data mine  
  
EXPOSE 25565  
USER mine  
ENTRYPOINT cd /data && java -Xms512M -Xmx1024M -jar /spigot.jar  

