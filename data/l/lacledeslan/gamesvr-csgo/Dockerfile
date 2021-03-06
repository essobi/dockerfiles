# escape=`  
FROM lacledeslan/steamcmd:linux as csgo-builder  
  
ARG contentServer=content.lacledeslan.net  
  
RUN if [ "$contentServer" = false ] ; then `  
echo "\n\nSkipping custom LL content\n\n"; `  
else `  
echo "\nDownloading custom LL content from $contentServer" &&`  
mkdir --parents /tmp/maps/ /output &&`  
cd /tmp/maps/ &&`  
wget -rkpN -l 1 -nH --no-verbose --cut-dirs=3 -R "*.htm*" -e robots=off
"http://"$contentServer"/fastDownloads/csgo/maps/" &&`  
echo "Decompressing files" &&`  
bzip2 --decompress /tmp/maps/*.bz2 &&`  
echo "Moving uncompressed files to destination" &&`  
mkdir --parents /output/csgo/maps/ &&`  
mv *.bsp *.nav /output/csgo/maps/; `  
fi;  
  
#=======================================================================  
FROM debian:stable-slim  
  
ARG BUILDNODE=unspecified  
ARG SKIP_STEAMCMD=false  
ARG SOURCE_COMMIT=unspecified  
  
HEALTHCHECK NONE  
  
RUN dpkg --add-architecture i386 &&`  
apt-get update && apt-get install -y `  
ca-certificates lib32gcc1 libstdc++6 libstdc++6:i386 locales locales-all tmux
&&`  
apt-get clean &&`  
rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*;  
  
ENV LANG=en_US.UTF-8 LANGUAGE=en_US.UTF-8 LC_ALL=en_US.UTF-8  
LABEL maintainer="Laclede's LAN <contact @lacledeslan.com>" `  
com.lacledeslan.build-node=$BUILDNODE `  
org.label-schema.schema-version="1.0" `  
org.label-schema.url="https://github.com/LacledesLAN/README.1ST" `  
org.label-schema.vcs-ref=$SOURCE_COMMIT `  
org.label-schema.vendor="Laclede's LAN" `  
org.label-schema.description="Counter-Strike: Global Offensive Dedicated
Server" `  
org.label-schema.vcs-url="https://github.com/LacledesLAN/gamesvr-csgo"  
# Set up Enviornment  
RUN useradd --home /app --gid root --system CSGO &&`  
mkdir -p /app/ll-tests &&`  
chown CSGO:root -R /app;  
  
## CSGO is so large we can't reliably use multi-stage builds in docker cloud  
# Copy cached build files (if any)  
COPY ./steamcmd-cache /app  
  
#Pull in SteamCMD  
COPY \--from=csgo-builder /app /app/steamcmd  
  
# Copy files in from builder  
COPY \--from=csgo-builder /output /app  
# Ownership shim until [github.com/moby/moby/pull/34263] makes it into Docker
Cloud  
RUN chown -R CSGO:root /app;  
  
## Add in tests  
COPY ./ll-tests /app/ll-tests  
  
RUN chmod +rx /app/ll-tests/*.sh &&`  
chmod +rwx /app/ll-tests &&`  
chown CSGO:root -R /app/ll-tests;  
  
USER CSGO  
  
# Download CSGO via SteamCMD  
RUN if [ "$SKIP_STEAMCMD" = true ] ; then `  
echo "\n\nSkipping SteamCMD install -- using only contents from steamcmd-
cache\n\n"; `  
else `  
echo "\n\nDownloading Counter-Strike: Global Offensive via SteamCMD"; `  
/app/steamcmd/steamcmd.sh `  
+login anonymous `  
+force_install_dir /app `  
+app_update 740 validate `  
+quit; `  
fi;  
  
RUN echo $'\n\nLinking steamclient.so to prevent srcds_run errors' &&`  
mkdir --parents /app/.steam/sdk32 &&`  
ln -s /app/bin/steamclient.so /app/.steam/sdk32/steamclient.so;  
  
WORKDIR /app  
  
ONBUILD USER root  

