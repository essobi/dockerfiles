FROM merciless210/centos6-java8  
  
RUN mkdir /minecraft  
  
WORKDIR /minecraft  
  
ENV MINECRAFT_VERSION 1.7.10  
ENV FORGE_VERSION 10.13.4.1614-1.7.10  
ENV FORESTRY_VERSION forestry_1.7.10-4.2.16.64.jar  
ENV FORESTRY_URL
https://minecraft.curseforge.com/projects/forestry/files/2333823/download  
ENV INDUSTRIAL_VERSION industrialcraft-2-2.2.816-experimental.jar  
ENV INDUSTRIAL_URL http://minecraft.curseforge.com/projects/industrial-
craft/files/2286867/download  
ENV BUILDCRAFT_VERSION buildcraft-7.1.21.jar  
ENV BUILDCRAFT_URL http://www.mod-
buildcraft.com/releases/BuildCraft/7.1.21/buildcraft-7.1.21.jar  
  
RUN curl -sS
http://files.minecraftforge.net/maven/net/minecraftforge/forge/${MINECRAFT_VERSION}-${FORGE_VERSION}/forge-${MINECRAFT_VERSION}-${FORGE_VERSION}-installer.jar
> /minecraft/forge-${MINECRAFT_VERSION}-${FORGE_VERSION}-installer.jar  
RUN java -jar
/minecraft/forge-${MINECRAFT_VERSION}-${FORGE_VERSION}-installer.jar
--installServer  
RUN rm -f /minecraft/forge-${MINECRAFT_VERSION}-${FORGE_VERSION}-installer.jar  
RUN java -jar forge-${MINECRAFT_VERSION}-${FORGE_VERSION}-universal.jar  
RUN curl -SL ${FORESTRY_URL} -o /minecraft/mods/${FORESTRY_VERSION}  
RUN curl -SL ${INDUSTRIAL_URL} -o /minecraft/mods/${INDUSTRIAL_VERSION}  
RUN curl -SL ${BUILDCRAFT_URL} -o /minecraft/mods/${BUILDCRAFT_VERSION}  
RUN sed -i s/false/true/g /minecraft/eula.txt  
  
VOLUME ["/config","/world","/logs"]  
  
EXPOSE 25565  
CMD /bin/bash  

