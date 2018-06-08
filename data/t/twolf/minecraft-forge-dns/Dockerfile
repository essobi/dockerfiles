FROM twolf/minecraft-forge:10.13.2  
MAINTAINER Thomas Boerger <thomas@webhippie.de>  
  
RUN mkdir -p /minecraft/backups  
RUN mkdir -p /minecraft/dynmap  
RUN mkdir -p /minecraft/template  
ADD template /minecraft/template  
  
VOLUME ["/minecraft/merge", "/minecraft/world", "/minecraft/logs",
"/minecraft/backups", "/minecraft/dynmap"]  
  
EXPOSE 25565 25575 8123  
WORKDIR /minecraft  
ENTRYPOINT ["manage"]  
CMD ["bash"]  

