FROM docku/spigot  
MAINTAINER Jon Chen <bsd@voltaire.sh>  
  
EXPOSE 25565  
VOLUME ["/srv/spigot/bsdlp", "/srv/spigot/bsdlp_nether",
"/srv/spigot/bsdlp_the_end", "/srv/spigot/logs",
"/srv/spigot/plugins/dynmap/web/tiles"]  
  
ADD . /srv/spigot/  
  
ADD http://dev.bukkit.org/media/files/758/666/CraftIRC.jar
/srv/spigot/plugins/CraftIRC.jar  
ADD http://dev.bukkit.org/media/files/853/318/dynmap-2.1.jar
/srv/spigot/plugins/dynmap.jar  
ADD http://dev.bukkit.org/media/files/793/351/WorldBorder.jar
/srv/spigot/plugins/WorldBorder.jar  
  
ADD start /service/voltairemc/run  

