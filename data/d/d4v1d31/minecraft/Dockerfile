FROM alpine  
RUN apk add --update bash git openjdk8 && rm -rf /var/cache/apk/*  
  
# Dockerfile for latest spigot version  
# build spigot  
RUN mkdir /minecraft_build  
WORKDIR /minecraft_build  
ADD
https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
/minecraft_build/BuildTools.jar  
#RUN /usr/bin/git config --global --unset core.autocrlf  
RUN java -jar BuildTools.jar  
  
# setup for production  
RUN mkdir -p /minecraft/config  
RUN mv /minecraft_build/spigot-*.jar /minecraft/spigot.jar  
RUN rm -R /minecraft_build  
  
WORKDIR /minecraft/config  
ADD start.sh /  
RUN chmod +x /start.sh  
  
VOLUME "/minecraft/config/"  
  
EXPOSE 25565  
ENTRYPOINT ["/start.sh"]  

