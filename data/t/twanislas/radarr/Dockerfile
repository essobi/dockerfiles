FROM twanislas/base-debian  
MAINTAINER Antoine Rahier <antoine.rahier@gmail.com>  
LABEL maintainer="Antoine Rahier <antoine.rahier@gmail.com>"  
  
# Build-time metadata  
ARG DEBIAN_FRONTEND=noninteractive  
ARG BUILD_DATE  
ARG VCS_REF  
LABEL org.label-schema.build-date="$BUILD_DATE" \  
org.label-schema.name="docker-radarr" \  
org.label-schema.description="Docker container for Radarr, based on latest
Debian stable" \  
org.label-schema.url="https://github.com/Twanislas/docker-radarr" \  
org.label-schema.vcs-ref="$VCS_REF" \  
org.label-schema.vcs-url="https://github.com/Twanislas/docker-radarr" \  
org.label-schema.vendor="Antoine Rahier" \  
org.label-schema.schema-version="1.0"  
  
# FreeNAS metadata  
LABEL org.freenas.autostart="true" \  
org.freenas.bridged="false" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.port-mappings="7878:7878/tcp" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"RADARR_UID\", \  
\"descr\": \"User ID to run Radarr\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"RADARR_GID\", \  
\"descr\": \"Group ID to run Radarr\", \  
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
org.freenas.web-ui-port=7878 \  
org.freenas.web-ui-path=""  
  
# Environment settings  
ENV HOME="/config" \  
XDG_CONFIG_HOME="/config" \  
XDG_DATA_HOME="/config"  
  
# Install dependencies  
RUN \  
apt-get update && \  
apt-get install -y curl libmono-cil-dev mono-devel mediainfo sqlite3  
  
# Install Radarr  
RUN \  
wget -O /tmp/Radarr.tar.gz $(wget -q -O -
https://api.github.com/repos/radarr/radarr/releases | grep linux.tar.gz | grep
browser_download_url | head -1 | cut -d \" -f 4) && \  
tar -xzf /tmp/Radarr.tar.gz -C /opt/ && \  
rm /tmp/Radarr.tar.gz  
  
# Copy needed files  
COPY rootfs /  
  
# Ports  
EXPOSE 7878/tcp  
  
# Volumes  
VOLUME /config /data  
  
## Init  
ENTRYPOINT [ "/init" ]  
  
# Health check  
HEALTHCHECK CMD curl --connect-timeout 15 --show-error --silent --fail
--location "http://localhost:7878" > /dev/null || exit 1  

