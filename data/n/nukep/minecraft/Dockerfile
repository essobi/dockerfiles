FROM jeanblanchard/busybox-java  
  
MAINTAINER Dan Spencer <dan@atomicpotato.net>  
  
ENV VERSION 1.8.6  
RUN curl -o minecraft_server.jar
http://s3.amazonaws.com/Minecraft.Download/versions/$VERSION/minecraft_server.$VERSION.jar  
  
COPY init.sh /init.sh  
COPY start.sh /start.sh  
  
VOLUME '/data'  
WORKDIR /data  
  
ENV JVM_OPTS -Xmx1024M -Xms1024M  
  
RUN adduser -H -D -s /bin/sh minecraft  
EXPOSE 25565  
CMD ["/init.sh"]  

