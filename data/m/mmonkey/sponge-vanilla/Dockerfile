FROM java:8  
  
MAINTAINER CJ O'Hara (mmonkey)  
  
ENV MINECRAFT_PORT 25567  
ENV MINECRAFT_EULA true  
ENV MINECRAFT_MAXHEAP 1024M  
  
ENV SPONGE_VERSION 1.8.9-4.2.0-BETA-337  
ENV SPONGE_URL
https://repo.spongepowered.org/maven/org/spongepowered/spongevanilla/${SPONGE_VERSION}/spongevanilla-${SPONGE_VERSION}.jar  
  
ENV EXECUTABLE_JAR spongevanilla-${SPONGE_VERSION}.jar  
  
RUN DEBIAN_FRONTEND=noninteractive  
VOLUME ["/vanilla"]  
  
ADD ./scripts/start.sh /start_vanilla  
RUN chmod +x /start_vanilla  
  
EXPOSE ${MINECRAFT_PORT}  
CMD ["/start_vanilla"]

