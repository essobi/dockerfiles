FROM openjdk:8-alpine  
  
RUN apk add --no-cache wget  
  
EXPOSE 25565  
RUN mkdir /minecraft && wget -q
"https://s3.amazonaws.com/Minecraft.Download/versions/1.12.2/minecraft_server.1.12.2.jar"
-O /minecraft/minecraft_server.jar  
  
WORKDIR /data  
RUN echo "eula=true" > /data/eula.txt  
  
CMD java -Xmx1024M -Xms1024M -jar /minecraft/minecraft_server.jar nogui  

