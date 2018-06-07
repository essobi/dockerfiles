FROM openjdk:jre  
  
WORKDIR /minecraft  
  
COPY minecraft/server ./server  
COPY minecraft/mods ./mods  
COPY minecraft/entrypoint.sh .  
  
VOLUME /minecraft/volume  
WORKDIR /minecraft/volume  
  
EXPOSE 25565  
ENTRYPOINT /minecraft/entrypoint.sh  
  

