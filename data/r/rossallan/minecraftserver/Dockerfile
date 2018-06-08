FROM openjdk:jre-alpine  
MAINTAINER Ross Allan <docker@nallar.me>  
  
ENV LANG=C.UTF-8 \  
MCVER=1.10.2 \  
ENABLEFORGE=false \  
LAUNCHWRAPPERVERSION=1.12 \  
MCEULA=true \  
AUTORESTART=true \  
JAVAPARAMETERS="-Xms4G -Xmx4G -XX:+AlwaysPreTouch -XX:+UseG1GC
-XX:+AggressiveOpts -XX:+DisableExplicitGC" \  
JARPARAMETERS="nogui" \  
FIX_PERMISSIONS=true \  
MCJAR=minecraft_server.VER.jar \  
FORGEJAR=minecraft_forge.jar  
  
ENV MCJARURL
https://s3.amazonaws.com/Minecraft.Download/versions/${MCVER}/minecraft_server.${MCVER}.jar  
ENV LAUNCHWRAPPERFQNAME
net/minecraft/launchwrapper/${LAUNCHWRAPPERVERSION}/launchwrapper-${LAUNCHWRAPPERVERSION}.jar  
ENV LAUNCHWRAPPERJAR libraries/${LAUNCHWRAPPERFQNAME}  
ENV LAUNCHWRAPPERJARURL https://libraries.minecraft.net/${LAUNCHWRAPPERFQNAME}  
  
COPY root/ /  
RUN chmod +x /root/*.sh && /bin/sh /root/install.sh  
  
VOLUME /minecraft  
  
ENTRYPOINT ["/sbin/tini", "-v", "--", "/root/init.sh"]  

