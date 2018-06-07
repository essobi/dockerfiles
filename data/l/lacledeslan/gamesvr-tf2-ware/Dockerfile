# escape=`  
FROM lacledeslan/gamesvr-tf2  
  
LABEL MAINTAINER="Laclede's LAN <contact@lacledeslan.com>" `  
org.label-schema.url="https://github.com/LacledesLAN" `  
org.label-schema.vendor="Laclede's LAN" `  
org.label-schema.vcs-ref=$VCS_REF `  
org.label-schema.name="gamesvr-tf2-ware" `  
org.label-schema.description="LL Team Fortress 2 'TF2-Ware' Server" `  
org.label-schema.vcs-url="https://github.com/LacledesLAN/gamesvr-tf2-ware"  
HEALTHCHECK NONE  
  
COPY ./dist /app/tf/  
  
COPY ./dist.linux /app/tf/  
  
# UPDATE USERNAME  
RUN usermod -l TF2Ware TF2 &&`  
find /app -type d -exec chmod 775 {} + &&`  
chmod +x /app/ll-tests/*.sh  
  
USER TF2Ware  
  
WORKDIR /app/  

