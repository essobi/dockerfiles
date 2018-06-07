# escape=`  
FROM lacledeslan/steamcmd:linux as steamcmd-builder  
  
#=======================================================================  
FROM debian:stable-slim  
  
HEALTHCHECK NONE  
  
ARG BUILDNODE="unspecified"  
ARG SOURCE_COMMIT  
  
LABEL maintainer="Laclede's LAN <contact @lacledeslan.com>" `  
com.lacledeslan.build-node=$BUILDNODE `  
org.label-schema.schema-version="1.0" `  
org.label-schema.url="https://github.com/LacledesLAN/README.1ST" `  
org.label-schema.vcs-ref=$SOURCE_COMMIT `  
org.label-schema.vendor="Laclede's LAN" `  
org.label-schema.description="7 Days to Die Server in Docker" `  
org.label-schema.vcs-url="https://github.com/LacledesLAN/gamesvr-7daystodie"  
RUN dpkg --add-architecture i386 &&`  
apt-get update && apt-get install -y `  
ca-certificates lib32gcc1 libc6-i386 lib32stdc++6 xmlstarlet &&`  
apt-get clean &&`  
rm -rf /var/lib/apt/lists/*;  
  
## 7 Days to Die is so large we can't reliably use multi-stage builds in
docker cloud  
# Copy cached build files (if any)  
COPY ./build-cache /app  
  
#Pull in SteamCMD  
COPY \--from=steamcmd-builder /app /app/steamcmd  
  
## Add in tests  
COPY ./ll-tests /app/ll-tests  
  
# Install 7 Days to Die using SteamCMD  
RUN echo $'\n\nDownloading 7 Days to Die via SteamCMD' &&`  
/app/steamcmd/steamcmd.sh `  
+login anonymous `  
+force_install_dir /app `  
+app_update 294420 validate `  
+quit;  
  
RUN chmod +x /app/ll-tests/*.sh;  
  
WORKDIR /app  

