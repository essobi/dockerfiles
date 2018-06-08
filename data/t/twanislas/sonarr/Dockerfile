FROM twanislas/base-debian  
MAINTAINER Antoine Rahier <antoine.rahier@gmail.com>  
LABEL maintainer="Antoine Rahier <antoine.rahier@gmail.com>"  
# Build-time metadata  
ARG DEBIAN_FRONTEND=noninteractive  
ARG BUILD_DATE  
ARG VCS_REF  
LABEL org.label-schema.build-date="$BUILD_DATE" \  
org.label-schema.name="docker-sonarr" \  
org.label-schema.description="Docker container for Sonarr, based on latest
Debian stable" \  
org.label-schema.url="https://github.com/Twanislas/docker-sonarr" \  
org.label-schema.vcs-ref="$VCS_REF" \  
org.label-schema.vcs-url="https://github.com/Twanislas/docker-sonarr" \  
org.label-schema.vendor="Antoine Rahier" \  
org.label-schema.schema-version="1.0"  
# FreeNAS metadata  
LABEL org.freenas.autostart="true" \  
org.freenas.bridged="false" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.port-mappings="8989:8989/tcp,9898:9898/tcp" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"SONARR_UID\", \  
\"descr\": \"User ID to run Sonarr\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"SONARR_GID\", \  
\"descr\": \"Group ID to run Sonarr\", \  
\"optional\": true \  
} \  
]" \  
org.freenas.upgradeable="true" \  
org.freenas.version="$VERSION" \  
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
org.freenas.web-ui-port=8989 \  
org.freenas.web-ui-path=""  
# Environment settings  
ENV HOME="/config" \  
XDG_CONFIG_HOME="/config" \  
XDG_DATA_HOME="/config"  
# Add sonarr repository and install packages  
RUN \  
apt-get install -y gnupg && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FDA5DFFC && \  
echo "deb http://apt.sonarr.tv/ master main" >
/etc/apt/sources.list.d/sonarr.list && \  
apt-get update && \  
apt-get install -y curl nzbdrone  
  
# Copy needed files  
COPY rootfs/ /  
  
# Ports  
EXPOSE 8989/tcp 9898/tcp  
  
# Volumes  
VOLUME /config /data  
  
## Init  
ENTRYPOINT [ "/init" ]  
  
# Health check  
HEALTHCHECK CMD curl --connect-timeout 15 --show-error \--silent --fail
--location "http://localhost:8989" > /dev/null || exit 1  

