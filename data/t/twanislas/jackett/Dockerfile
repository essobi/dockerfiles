FROM twanislas/base-debian  
MAINTAINER Antoine Rahier <antoine.rahier@gmail.com>  
LABEL maintainer="Antoine Rahier <antoine.rahier@gmail.com>"  
  
# Build-time metadata  
ARG DEBIAN_FRONTEND=noninteractive  
ARG BUILD_DATE  
ARG VCS_REF  
LABEL org.label-schema.build-date="$BUILD_DATE" \  
org.label-schema.name="docker-jackett" \  
org.label-schema.description="Docker container for Jackett, based on latest
Debian stable" \  
org.label-schema.url="https://github.com/Twanislas/docker-jackett" \  
org.label-schema.vcs-ref="$VCS_REF" \  
org.label-schema.vcs-url="https://github.com/Twanislas/docker-jackett" \  
org.label-schema.vendor="Antoine Rahier" \  
org.label-schema.schema-version="1.0"  
  
# FreeNAS metadata  
LABEL org.freenas.autostart="true" \  
org.freenas.bridged="false" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.port-mappings="9117:9117/tcp" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"JACKETT_UID\", \  
\"descr\": \"User ID to run Jackett\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"JACKETT_GID\", \  
\"descr\": \"Group ID to run Jackett\", \  
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
org.freenas.web-ui-port=9117 \  
org.freenas.web-ui-path=""  
  
# Environment settings  
ENV HOME="/config" \  
XDG_CONFIG_HOME="/config" \  
XDG_DATA_HOME="/config"  
  
# Add repos and install what we need  
RUN \  
apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get -y install curl mono-devel ca-certificates-mono libcurl4-openssl-dev  
  
# Install Jackett  
RUN \  
wget -O /tmp/Jackett.tar.gz $(wget -q -O -
https://api.github.com/repos/jackett/jackett/releases/latest | grep -E
"download.*Mono" | awk '{print $2}' | tr -d \") && \  
tar -xzf /tmp/Jackett.tar.gz -C /opt/ && \  
rm /tmp/Jackett.tar.gz  
  
# Copy needed files  
COPY rootfs/ /  
  
# Ports  
EXPOSE 9117/tcp  
  
# Volumes  
VOLUME /config /data  
  
# Health check  
HEALTHCHECK CMD curl --connect-timeout 15 --show-error --silent --fail
--location "http://localhost:9117/UI/Dashboard" > /dev/null || exit 1  

