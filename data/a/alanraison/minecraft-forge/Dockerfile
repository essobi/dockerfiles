FROM alanraison/minecraft:1.10.2  
RUN mkdir -p /mc/mods  
WORKDIR /mc  
ADD \  
http://files.minecraftforge.net/maven/net/minecraftforge/forge/1.10-12.18.0.2000-1.10.0/forge-1.10-12.18.0.2000-1.10.0-installer.jar
\  
http://files.minecraftforge.net/maven/net/minecraftforge/forge/1.10-12.18.0.2000-1.10.0/forge-1.10-12.18.0.2000-1.10.0-universal.jar
\  
./  
EXPOSE 25565  
RUN ["java", "-jar",
"forge-1.10-12.18.0.2000-1.10.0-installer.jar","-installServer"]  
RUN ["rm","forge-1.10-12.18.0.2000-1.10.0-installer.jar"]  
RUN ["rm","forge-1.10-12.18.0.2000-1.10.0-installer.jar.log"]  
CMD ["java", "-jar", "forge-1.10-12.18.0.2000-1.10.0-universal.jar","nogui"]  

