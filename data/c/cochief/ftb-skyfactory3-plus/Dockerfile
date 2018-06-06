  
FROM openjdk:alpine  
MAINTAINER Stefan Urban <stefan.urban@live.de>  
  
  
ENV VERSION="3_0_9"  
USER root  
WORKDIR /minecraft  
  
VOLUME ["/minecraft/world"]  
EXPOSE 25565  
# Download and unzip minecraft files  
RUN apk update && apk add curl wget && \  
mkdir -p /minecraft/world && \  
curl -LO
http://ftb.cursecdn.com/FTB2/modpacks/FTBPresentsSkyfactory3/${VERSION}/FTBPresentsSkyfactory3Server.zip
&& \  
unzip FTBPresentsSkyfactory3Server.zip  
  
# Accept EULA  
RUN echo "# EULA accepted on $(date)" > /minecraft/eula.txt && \  
echo "eula=TRUE" >> eula.txt  
  
# Install additional mods with config files  
RUN mkdir -p /minecraft-mods/  
  
COPY install_mods.sh /minecraft-mods/  
COPY mods.txt /minecraft-mods/  
COPY config /minecraft-mods/config  
  
RUN chmod u+x /minecraft-mods/install_mods.sh && \  
sync && sleep 1 && \  
/minecraft-mods/install_mods.sh /minecraft  
  
# Install minecraft server itself  
RUN /bin/sh /minecraft/FTBInstall.sh  
  
# Startup script  
CMD ["/bin/sh", "/minecraft/ServerStart.sh"]  

