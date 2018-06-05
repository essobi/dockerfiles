FROM vsense/baseimage:alpine  
  
MAINTAINER <docker@vsense.fr> (@vsense)  
  
ENV VERSION 1.9.2  
RUN apk --update add \  
openjdk7 \  
wget \  
&& mkdir /minecraft \  
&& wget --no-check-certificate
https://s3.amazonaws.com/Minecraft.Download/versions/$VERSION/minecraft_server.$VERSION.jar
-O /minecraft/minecraft_server.jar \  
&& adduser -D -h /minecraft -s /sbin/nologin minecraft \  
&& chown -R minecraft:minecraft /minecraft \  
&& apk del wget \  
&& rm -rf /var/cache/apk/*  
  
USER minecraft  
  
WORKDIR /minecraft  
  
RUN java -Xms1G -Xmx1G -jar minecraft_server.jar nogui  
  
RUN sed -i -e 's/false/true/' eula.txt  
  
COPY server.properties /minecraft/server.properties  
  
USER root  
  
RUN chown -R minecraft:minecraft /minecraft  
  
VOLUME /minecraft  
  
EXPOSE 25565  
CMD ["java","-Xms1G","-Xmx1G","-jar","minecraft_server.jar","nogui"]  

