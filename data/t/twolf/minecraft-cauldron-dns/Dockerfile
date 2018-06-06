FROM twolf/minecraft-cauldron:latest  
MAINTAINER Thomas Boerger <thomas@webhippie.de>  
  
VOLUME ["/minecraft/merge", "/minecraft/world", "/minecraft/logs",
"/minecraft/backups"]  
  
ADD rootfs /  
EXPOSE 25565 25575  
WORKDIR /minecraft  
CMD ["/usr/bin/s6-svscan","/etc/s6"]  

