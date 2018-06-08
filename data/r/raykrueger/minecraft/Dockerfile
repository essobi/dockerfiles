FROM openjdk  
MAINTAINER Ray Krueger <raykrueger@gmail.com>  
  
ENV MINECRAFT_VERSION 1.11.2  
RUN mkdir /minecraft  
WORKDIR /minecraft  
  
ADD minecraft_server.sha1 .  
  
RUN curl -sSL
https://s3.amazonaws.com/Minecraft.Download/versions/${MINECRAFT_VERSION}/minecraft_server.${MINECRAFT_VERSION}.jar
-o minecraft_server.jar \  
&& shasum -c minecraft_server.sha1  
  
VOLUME /minecraft/world  
COPY /minecraft/ /minecraft/  
  
ONBUILD ADD server.properties /minecraft/server.properties  
  
EXPOSE 25565  
CMD ["java", "-jar", "minecraft_server.jar"]  

