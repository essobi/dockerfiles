FROM axeclbr/java:jre8  
  
RUN apk --update add curl \  
&& curl -L
https://s3.amazonaws.com/Minecraft.Download/versions/1.8.7/minecraft_server.1.8.7.jar
-o minecraft_server.jar \  
&& apk del curl \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /data  
VOLUME /data  
  
EXPOSE 25565  
CMD echo eula=true > /data/eula.txt && java -jar /minecraft_server.jar  

