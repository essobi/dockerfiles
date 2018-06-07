# escape=`  
FROM lacledeslan/steamcmd:linux as hl2dm-builder  
  
RUN echo $'\n\nDownloading LL custom content from public ftp server' &&`  
mkdir --parents /tmp/maps/ &&`  
cd /tmp/maps/ &&`  
wget -m `  
ftp://llgameserverbot:6gDyfNJhm4UsraE5@raw.content.lacledeslan.net/hl2dm/maps/
`  
-nH --no-verbose --cut-dirs 4 &&`  
rm -f .listing &&`  
echo "Decompressing downloaded content" &&`  
bzip2 --decompress /tmp/maps/*.*.bz2 &&`  
rm -f /tmp/maps/*.bz2 &&`  
echo "Moving uncompressed files to destination" &&`  
mkdir /output/hl2mp/maps --parents &&`  
mv /tmp/maps/*.* /output/hl2mp/maps;  
  
#=======================================================================  
FROM debian:stable-slim  
  
ARG BUILDNODE=unspecified  
ARG SOURCE_COMMIT=unspecified  
  
HEALTHCHECK NONE  
  
RUN dpkg --add-architecture i386 &&`  
apt-get update && apt-get install -y `  
ca-certificates lib32gcc1 lib32tinfo5 libcurl4-gnutls-dev:i386 libstdc++6
libstdc++6:i386 libtcmalloc-minimal4:i386 procps screen &&`  
apt-get clean &&`  
rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*;  
  
LABEL maintainer="Laclede's LAN <contact @lacledeslan.com>" `  
com.lacledeslan.build-node=$BUILDNODE `  
org.label-schema.schema-version="1.0" `  
org.label-schema.url="https://github.com/LacledesLAN/README.1ST" `  
org.label-schema.vcs-ref=$SOURCE_COMMIT `  
org.label-schema.vendor="Laclede's LAN" `  
org.label-schema.description="Half-Life 2 Deathmatch Dedicated Server" `  
org.label-schema.vcs-url="https://github.com/LacledesLAN/gamesvr-hl2dm"  
# Set up Enviornment  
RUN useradd --home /app --gid root --system HL2DM &&`  
mkdir -p /app/ll-tests &&`  
chown HL2DM:root -R /app;  
  
## HL2DM is so large we can't reliably use multi-stage builds in docker cloud  
# Copy cached build files (if any)  
COPY ./build-cache /app  
  
# Pull in SteamCMD  
COPY \--from=hl2dm-builder /app /app/steamcmd  
  
# Copy files in from builder (if any)  
COPY \--from=hl2dm-builder /output /app  
# Ownership shim until [github.com/moby/moby/pull/34263] makes it into Docker
Cloud  
RUN chown -R HL2DM:root /app;  
  
## Add in tests  
COPY ./ll-tests /app/ll-tests  
  
RUN chmod +rx /app/ll-tests/*.sh &&`  
chmod +rwx /app/ll-tests &&`  
chown HL2DM:root -R /app/ll-tests;  
  
USER HL2DM  
  
# Install Half-Life 2 Deathmatch Server  
RUN echo $'\n\nDownloading Half-Life 2 Deathmatch Server via SteamCMD' &&`  
/app/steamcmd/steamcmd.sh `  
+login anonymous `  
+force_install_dir /app `  
+app_update 232370 validate `  
+quit;  
  
RUN echo $'\n\nLinking steamclient.so to prevent srcds_run errors' &&`  
mkdir --parents /app/.steam/sdk32 &&`  
ln -s /app/bin/steamclient.so /app/.steam/sdk32/steamclient.so  
  
WORKDIR /app  
  
ONBUILD USER root  

