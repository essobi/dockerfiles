# escape=`  
FROM lacledeslan/steamcmd:linux as hldms-builder  
  
RUN echo "Downloading content from LL public ftp server" &&`  
mkdir \--parents /tmp/maps/ /output &&`  
cd /tmp/maps/ &&`  
wget -m `  
ftp://llgameserverbot:6gDyfNJhm4UsraE5@raw.content.lacledeslan.net/hldms/maps/
`  
-nH \--no-verbose \--cut-dirs 4 &&`  
rm -f .listing &&`  
echo "Decompressing files" &&`  
bzip2 \--decompress /tmp/maps/*.*.bz2 &&`  
rm -f /tmp/maps/*.bz2 &&`  
echo "Moving uncompressed files to destination" &&`  
mkdir \--parents /output/hl1mp/maps/ &&`  
mv /tmp/maps/*.bsp /output/hl1mp/maps/ &&`  
echo "Performing Cleanup" &&`  
rm -rf /tmp/*/*;  
  
#=======================================================================  
FROM debian:stable-slim  
  
ARG BUILDNODE=unspecified  
ARG SOURCE_COMMIT=unspecified  
  
HEALTHCHECK NONE  
  
RUN dpkg \--add-architecture i386 &&`  
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
org.label-schema.description="Half-Life Deathmatch Source Dedicated Server" `  
org.label-schema.vcs-url="https://github.com/LacledesLAN/gamesvr-hldms"  
# Set up Enviornment  
RUN useradd \--home /app \--gid root \--system HLDMS &&`  
mkdir -p /app/ll-tests &&`  
chown HLDMS:root -R /app;  
  
## Half-Life Deathmatch Source Dedicated Server is so large we can't reliably
use multi-stage builds in docker cloud  
# Copy cached build files (if any)  
COPY ./build-cache /app  
#Pull in SteamCMD  
COPY \--from=hldms-builder /app /app/steamcmd  
# Copy files in from builder  
COPY \--from=hldms-builder /output /app  
# Ownership shim until [github.com/moby/moby/pull/34263] makes it into Docker
Cloud  
RUN chown -R HLDMS:root /app;  
  
## Add in tests  
COPY ./ll-tests /app/ll-tests  
  
RUN chmod +rx /app/ll-tests/*.sh &&`  
chmod +rwx /app/ll-tests &&`  
chown HLDMS:root -R /app/ll-tests;  
  
USER HLDMS  
  
# Install Half-Life Deathmatch Source Dedicated Server using SteamCMD  
RUN echo $'\n\nDownloading Half-Life Deathmatch Source Dedicated Server via
SteamCMD' &&`  
/app/steamcmd/steamcmd.sh `  
+login anonymous `  
+force_install_dir /app `  
+app_update 255470 validate `  
+quit;  
  
RUN echo $'\n\nLinking steamclient.so to prevent srcds_run errors' &&`  
mkdir -p /app/.steam/sdk32 &&`  
ln -s /app/bin/steamclient.so /app/.steam/sdk32/steamclient.so;  
  
WORKDIR /app  
  
ONBUILD USER root  

