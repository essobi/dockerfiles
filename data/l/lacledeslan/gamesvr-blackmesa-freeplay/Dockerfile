# escape=`  
FROM lacledeslan/gamesvr-blackmesa  
  
ARG BUILDNODE="unspecified"  
ARG SOURCE_COMMIT  
  
LABEL maintainer="Laclede's LAN <contact @lacledeslan.com>" `  
com.lacledeslan.build-node=$BUILDNODE `  
org.label-schema.schema-version="1.0" `  
org.label-schema.url="https://github.com/LacledesLAN/README.1ST" `  
org.label-schema.vcs-ref=$SOURCE_COMMIT `  
org.label-schema.vendor="Laclede's LAN" `  
org.label-schema.description="Laclede's LAN Black Mesa Freeplay Dedicated
Server" `  
org.label-schema.vcs-url="https://github.com/LacledesLAN/gamesvr-blackmesa-
freeplay"  
COPY ./sourcemod.linux /app/bms/  
  
COPY ./sourcemod-configs /app/bms/  
  
COPY ./dist /app/bms/  
  
COPY ./ll-tests /app/ll-tests  
  
RUN chmod +rx /app/ll-tests/*.sh &&`  
chmod +rwx /app/ll-tests &&`  
chown BlackMesa:root -R /app/ll-tests;  
  
# UPDATE USERNAME & ensure permissions  
RUN usermod -l BlackMesaFreeplay BlackMesa &&`  
find /app -type d -exec chmod 774 {} + &&`  
chmod +x /app/ll-tests/*.sh &&`  
mkdir -p /app/bms/logs &&`  
echo "Permissions hacks until 17.09+ makes it into Docker Cloud" &&`  
chmod -R 774 /app/bms/addons &&`  
chmod -R 774 /app/bms/cfg &&`  
chmod -R 774 /app/bms/logs;  
  
USER BlackMesaFreeplay  
  
WORKDIR /app/  
  
ONBUILD USER root  

