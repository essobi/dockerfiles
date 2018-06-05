FROM library/java:latest  
RUN mkdir /mc  
WORKDIR /mc  
ADD \  
banned-ips.json \  
banned-players.json \  
eula.txt \  
https://s3.amazonaws.com/Minecraft.Download/versions/1.8.8/minecraft_server.1.8.8.jar
\  
ops.json \  
server.properties \  
whitelist.json \  
/mc/  
EXPOSE 25565  
CMD ["java",
"-Xmx1024M","-Xms1024M","-jar","minecraft_server.1.8.8.jar","nogui"]  

