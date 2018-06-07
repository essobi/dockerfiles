# escape=`  
FROM lacledeslan/gamesvr-csgo  
  
HEALTHCHECK NONE  
  
ARG BUILDNODE=unspecified  
ARG SOURCE_COMMIT=unspecified  
  
LABEL maintainer="Laclede's LAN <contact @lacledeslan.com>" `  
com.lacledeslan.build-node=$BUILDNODE `  
org.label-schema.schema-version="1.0" `  
org.label-schema.url="https://github.com/LacledesLAN/README.1ST" `  
org.label-schema.vcs-ref=$SOURCE_COMMIT `  
org.label-schema.vendor="Laclede's LAN" `  
org.label-schema.description="LL Counter-Strike GO Freeplay Server" `  
org.label-schema.vcs-url="https://github.com/LacledesLAN/gamesvr-csgo-
freeplay"  
COPY ./sourcemod.linux /app/csgo/  
  
COPY ./sourcemod-configs /app/csgo/  
  
COPY ./dist /app/  
  
COPY ./ll-tests /app/ll-tests  
  
RUN chmod +rx /app/ll-tests/*.sh &&`  
chmod +rwx /app/ll-tests &&`  
chown CSGO:root -R /app/ll-tests;  
  
# UPDATE USERNAME & ensure permissions  
RUN usermod -l CSGOFreeplay CSGO &&`  
find /app -type d -exec chmod 774 {} + &&`  
chmod +x /app/ll-tests/*.sh &&`  
mkdir -p /app/csgo/logs &&`  
echo "Permissions hacks until 17.09+ makes it into Docker Cloud" &&`  
chmod -R 774 /app/csgo/addons &&`  
chmod -R 774 /app/csgo/cfg &&`  
chmod -R 774 /app/csgo/logs;  
  
USER CSGOFreeplay  
  
WORKDIR /app/  
  
ONBUILD USER root  

