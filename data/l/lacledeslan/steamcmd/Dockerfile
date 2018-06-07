# escape=`  
FROM debian:stable-slim  
  
ARG BUILDNODE=unspecified  
ARG SOURCE_COMMIT=unspecified  
  
LABEL maintainer="Laclede's LAN <contact @lacledeslan.com>" `  
com.lacledeslan.build-node=$BUILDNODE `  
org.label-schema.schema-version="1.0" `  
org.label-schema.url="https://github.com/LacledesLAN/README.1ST" `  
org.label-schema.vcs-ref=$SOURCE_COMMIT `  
org.label-schema.vendor="Laclede's LAN" `  
org.label-schema.description="SteamCMD in Docker" `  
org.label-schema.vcs-url="https://github.com/LacledesLAN/SteamCMD"  
HEALTHCHECK NONE  
  
# Install dependencies  
RUN apt-get update &&`  
apt-get install -y `  
bzip2 ca-certificates curl lib32gcc1 tar unzip wget &&`  
apt-get clean &&`  
rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*;  
  
# Add in tests  
COPY /ll-tests /app/ll-tests  
  
# Set up Enviornment  
# Adds user 'SteamCMD' to group 'root' until --chown
([github.com/moby/moby/pull/34263]) makes it into Docker Cloud  
RUN mkdir -p /app/ll-tests /output &&`  
useradd --home /app --gid root --system SteamCMD &&`  
chown SteamCMD:root -R /app &&`  
chown SteamCMD:root -R /output &&`  
chmod +x /app/ll-tests/*.sh;  
  
USER SteamCMD  
  
# Obtain SteamCMD; Run so it self-updates  
RUN wget -qO- http://media.steampowered.com/installer/steamcmd_linux.tar.gz |
tar xz -C /app &&`  
chmod +x /app/steamcmd.sh &&`  
/app/steamcmd.sh +login anonymous +force_install_dir /output +quit;  
  
WORKDIR /app  

