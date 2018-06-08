FROM magikcraft/java  
  
MAINTAINER Josh Wulf "josh@magikcraft.io"  
# Expose Minecraft server ports  
EXPOSE 25565 25575  
# Add Minecraft server  
COPY server-build /home/server/  
COPY export-world.py /home/  
RUN rm -rf /home/server/.git \  
&& apk add --update python py-yaml  
WORKDIR /home/server  
ENTRYPOINT ["java", "-Xmx1024M","-Xms1024M", "-jar", "paperclip.jar"]

