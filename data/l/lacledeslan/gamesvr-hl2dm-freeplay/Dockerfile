# escape=`  
FROM lacledeslan/gamesvr-hl2dm  
  
HEALTHCHECK NONE  
  
ARG BUILDNODE="unspecified"  
ARG SOURCE_COMMIT  
  
LABEL maintainer="Laclede's LAN <contact @lacledeslan.com>" `  
com.lacledeslan.build-node=$BUILDNODE `  
org.label-schema.schema-version="1.0" `  
org.label-schema.url="https://github.com/LacledesLAN/README.1ST" `  
org.label-schema.vcs-ref=$SOURCE_COMMIT `  
org.label-schema.vendor="Laclede's LAN" `  
org.label-schema.description="LL Half-Life 2 Deathmatch Dedicated Freeplay
Server" `  
org.label-schema.vcs-url="https://github.com/LacledesLAN/gamesvr-hl2dm"  
COPY ./sourcemod.linux /app/hl2mp/  
  
COPY ./sourcemod-configs /app/hl2mp/  
  
COPY ./dist /app/  
  
COPY ./ll-tests/*.sh /app/ll-tests  
  
RUN chmod +rx /app/ll-tests/*.sh &&`  
chmod +rwx /app/ll-tests &&`  
chown HL2DM:root -R /app/ll-tests;  
  
# UPDATE USERNAME & ensure permissions  
RUN usermod -l HL2DMFreeplay HL2DM &&`  
find /app -type d -exec chmod 774 {} + &&`  
chmod +x /app/ll-tests/*.sh &&`  
mkdir -p /app/hl2mp/logs &&`  
echo "Permissions hacks until 17.09+ makes it into Docker Cloud" &&`  
chmod -R 774 /app/hl2mp/addons &&`  
chmod -R 774 /app/hl2mp/cfg &&`  
chmod -R 774 /app/hl2mp/logs;  
  
USER HL2DMFreeplay  
  
WORKDIR /app/  
  
ONBUILD USER root  

