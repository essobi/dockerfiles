# escape=`  
FROM lacledeslan/gamesvr-dods  
  
HEALTHCHECK NONE  
  
ARG BUILDNODE="unspecified"  
ARG SOURCE_COMMIT  
  
LABEL maintainer="Laclede's LAN <contact @lacledeslan.com>" `  
com.lacledeslan.build-node=$BUILDNODE `  
org.label-schema.schema-version="1.0" `  
org.label-schema.url="https://github.com/LacledesLAN/README.1ST" `  
org.label-schema.vcs-ref=$SOURCE_COMMIT `  
org.label-schema.vendor="Laclede's LAN" `  
org.label-schema.description="LL Day of Defeat Dedicated Freeplay Server" `  
org.label-schema.vcs-url="https://github.com/LacledesLAN/gamesvr-dods-
freeplay"  
COPY ./sourcemod.linux /app/dod/  
  
COPY ./sourcemod-configs /app/dod/  
  
COPY ./dist /app/  
  
COPY ./ll-tests/*.sh /app/ll-tests  
  
RUN chmod +rx /app/ll-tests/*.sh &&`  
chmod +rwx /app/ll-tests &&`  
chown DODS:root -R /app/ll-tests;  
  
# UPDATE USERNAME & ensure permissions  
RUN usermod -l DODSFreeplay DODS &&`  
find /app -type d -exec chmod 774 {} + &&`  
chmod +x /app/ll-tests/*.sh &&`  
mkdir -p /app/dod/logs &&`  
echo "Permissions hacks until 17.09+ makes it into Docker Cloud" &&`  
chmod -R 774 /app/dod/addons &&`  
chmod -R 774 /app/dod/cfg &&`  
chmod -R 774 /app/dod/logs;  
  
USER DODSFreeplay  
  
WORKDIR /app/  
  
ONBUILD USER root  

