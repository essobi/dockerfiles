FROM java:8  
  
MAINTAINER CJ O'Hara (mmonkey)  
  
ENV MINECRAFT_PORT 25566  
ENV MINECRAFT_EULA true  
ENV MINECRAFT_MAXHEAP 1024M  
  
ENV FORGE_VERSION 1.8.9-11.15.1.1890-1.8.9  
ENV FORGE_URL
http://files.minecraftforge.net/maven/net/minecraftforge/forge/${FORGE_VERSION}/forge-${FORGE_VERSION}-installer.jar  
  
ENV SPONGE_VERSION 1.8.9-1890-4.2.0-BETA-1402  
ENV SPONGE_URL
http://files.minecraftforge.net/maven/org/spongepowered/spongeforge/${SPONGE_VERSION}/spongeforge-${SPONGE_VERSION}.jar  
  
ENV EXECUTABLE_JAR forge-${FORGE_VERSION}-universal.jar  
  
RUN DEBIAN_FRONTEND=noninteractive  
VOLUME ["/forge"]  
  
ADD ./scripts/start.sh /start_forge  
RUN chmod +x /start_forge  
  
EXPOSE ${MINECRAFT_PORT}  
CMD ["/start_forge"]

