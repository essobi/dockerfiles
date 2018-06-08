FROM merciless210/centos6-java8  
  
RUN mkdir /minecraft  
  
WORKDIR /minecraft  
  
ENV MINECRAFT_VERSION 1.12.2  
ENV FORGE_VERSION 14.23.3.2681  
#Disabled - unable to find correct version or dynmap  
#ENV DYNMAP_URL
https://minecraft.curseforge.com/projects/dynmapforge/files/2380603/download  
#ENV DYNMAP_VERSION Dynmap-2.4-forge-1.11.2.jar  
RUN curl -sS
http://files.minecraftforge.net/maven/net/minecraftforge/forge/${MINECRAFT_VERSION}-${FORGE_VERSION}/forge-${MINECRAFT_VERSION}-${FORGE_VERSION}-installer.jar
> /minecraft/forge-${MINECRAFT_VERSION}-${FORGE_VERSION}-installer.jar  
RUN java -jar
/minecraft/forge-${MINECRAFT_VERSION}-${FORGE_VERSION}-installer.jar
--installServer  
RUN rm -f /minecraft/forge-${MINECRAFT_VERSION}-${FORGE_VERSION}-installer.jar  
#Used to download DYNMAP  
#RUN curl -SL ${DYNMAP_URL} -o /minecraft/mods/${DYNMAP_VERSION}  
RUN java -jar /minecraft/minecraft_server.${MINECRAFT_VERSION}.jar  
RUN sed -i s/false/true/g /minecraft/eula.txt  
  
VOLUME ["/dynmap","/world","/logs"]  
  
EXPOSE 25565 8123  
CMD /bin/bash  

