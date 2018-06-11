FROM twanislas/base-debian  
MAINTAINER Antoine Rahier <antoine.rahier@gmail.com>  
LABEL maintainer="Antoine Rahier <antoine.rahier@gmail.com>"  
# Build-time metadata  
ARG DEBIAN_FRONTEND=noninteractive  
ARG BUILD_DATE  
ARG VCS_REF  
LABEL org.label-schema.build-date="$BUILD_DATE" \  
org.label-schema.name="docker-qbittorrent" \  
org.label-schema.description="Docker container for qBittorrent, based on
latest Debian stable" \  
org.label-schema.url="https://github.com/Twanislas/docker-qbittorrent" \  
org.label-schema.vcs-ref="$VCS_REF" \  
org.label-schema.vcs-url="https://github.com/Twanislas/docker-qbittorrent" \  
org.label-schema.vendor="Antoine Rahier" \  
org.label-schema.schema-version="1.0"  
# FreeNAS metadata  
LABEL org.freenas.autostart="true" \  
org.freenas.bridged="false" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.port-mappings="8081:8081/tcp,53160:53160/tcp,53160:53160/udp" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"QBITTORRENT_UID\", \  
\"descr\": \"User ID to run qBittorrent\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"QBITTORRENT_GID\", \  
\"descr\": \"Group ID to run qBittorrent\", \  
\"optional\": true \  
} \  
]" \  
org.freenas.upgradeable="true" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/config\", \  
\"descr\": \"Config volume/dataset\" \  
}, \  
{ \  
\"name\": \"/data\", \  
\"descr\": \"Data volume/dataset\" \  
} \  
]" \  
org.freenas.web-ui-protocol="http" \  
org.freenas.web-ui-port=8081 \  
org.freenas.web-ui-path=""  
# Environment settings  
ENV HOME="/config" \  
XDG_CONFIG_HOME="/config" \  
XDG_DATA_HOME="/config"  
# Add repos and install what we need  
RUN \  
apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get -y install curl qbittorrent-nox  
  
# Copy needed files  
COPY rootfs/ /  
  
# Ports  
EXPOSE 8080/tcp  
EXPOSE 53160/tcp  
EXPOSE 53160/udp  
  
# Volumes  
VOLUME /config /data  
  
# Health check  
HEALTHCHECK CMD curl --connect-timeout 15 --show-error \--silent --fail
--location "http://localhost:8080" > /dev/null || exit 1  

