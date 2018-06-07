# escape=`  
FROM lacledeslan/gamesvr-tf2  
  
HEALTHCHECK NONE  
  
ARG BUILDNODE="unspecified"  
ARG SOURCE_COMMIT  
  
LABEL maintainer="Laclede's LAN <contact @lacledeslan.com>" `  
com.lacledeslan.build-node=$BUILDNODE `  
org.label-schema.schema-version="1.0" `  
org.label-schema.url="https://github.com/LacledesLAN/README.1ST" `  
org.label-schema.vcs-ref=$SOURCE_COMMIT `  
org.label-schema.vendor="Laclede's LAN" `  
org.label-schema.description="LL Team Fortress 2 Dedicated Freeplay Server" `  
org.label-schema.vcs-url="https://github.com/LacledesLAN/gamesvr-tf2-freeplay"  
COPY ./sourcemod.linux /app/tf/  
  
COPY ./sourcemod-configs /app/tf/  
  
COPY ./dist /app/  
  
COPY ./ll-tests/*.sh /app/ll-tests  
  
RUN chmod +rx /app/ll-tests/*.sh &&`  
chmod +rwx /app/ll-tests &&`  
chown TF2:root -R /app/ll-tests;  
  
# UPDATE USERNAME & ensure permissions  
RUN usermod -l TF2Freeplay TF2 &&`  
find /app -type d -exec chmod 774 {} + &&`  
chmod +x /app/ll-tests/*.sh &&`  
mkdir -p /app/tf/logs &&`  
echo "Permissions hacks until 17.09+ makes it into Docker Cloud" &&`  
chmod -R 774 /app/tf/addons &&`  
chmod -R 774 /app/tf/cfg &&`  
chmod -R 774 /app/tf/logs;  
  
USER TF2Freeplay  
  
WORKDIR /app/  
  
ONBUILD USER root  

