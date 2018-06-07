FROM twanislas/base-alpine  
MAINTAINER Antoine Rahier <antoine.rahier@gmail.com>  
LABEL maintainer="Antoine Rahier <antoine.rahier@gmail.com>"  
# Build-time metadata  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION=0.0.9  
LABEL org.label-schema.build-date="$BUILD_DATE" \  
org.label-schema.name="docker-deluge" \  
org.label-schema.description="Docker container for Deluge torrent client,
based on latest Alpine Linux" \  
org.label-schema.url="https://github.com/Twanislas/docker-deluge" \  
org.label-schema.vcs-ref="$VCS_REF" \  
org.label-schema.vcs-url="https://github.com/Twanislas/docker-deluge" \  
org.label-schema.vendor="Antoine Rahier" \  
org.label-schema.version="$VERSION" \  
org.label-schema.schema-version="1.0"  
# FreeNAS metadata  
LABEL org.freenas.autostart="true" \  
org.freenas.bridged="false" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.port-mappings="8112:8112/tcp,53160:53160/tcp,53160:53160/udp" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"DELUGE_UID\", \  
\"descr\": \"User ID to run Deluge\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"DELUGE_GID\", \  
\"descr\": \"Group ID to run Deluge\", \  
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
\"descr\": \"Downloads volume/dataset\" \  
} \  
]" \  
org.freenas.web-ui-protocol="http" \  
org.freenas.web-ui-port=8112 \  
org.freenas.web-ui-path=""  
# Add repos and install what we need  
RUN \  
echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk upgrade \--no-cache && \  
apk add \--no-cache py-pip deluge@testing && \  
pip install -U pip && \  
pip install service_identity attr  
  
# Copy needed files  
COPY rootfs/ /  
  
# Ports  
EXPOSE 8112/tcp 58846/tcp 53160/tcp 53160/udp  
  
# Volumes  
VOLUME /config /data  
  
# Health check  
HEALTHCHECK CMD curl --connect-timeout 15 --show-error \--silent --fail
--location "http://localhost:8112" > /dev/null || exit 1  

