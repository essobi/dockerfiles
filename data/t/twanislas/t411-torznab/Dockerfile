FROM twanislas/base-alpine:latest  
MAINTAINER Antoine Rahier <antoine.rahier@gmail.com>  
LABEL maintainer="Antoine Rahier <antoine.rahier@gmail.com>"  
  
# Build-time metadata  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date="$BUILD_DATE" \  
org.label-schema.name="docker-T411-Torznab" \  
org.label-schema.description="Docker container for T411-Torznab, based on
latest Alpine Linux" \  
org.label-schema.url="https://github.com/Twanislas/docker-T411-Torznab" \  
org.label-schema.vcs-ref="$VCS_REF" \  
org.label-schema.vcs-url="https://github.com/Twanislas/docker-T411-Torznab" \  
org.label-schema.vendor="Antoine Rahier" \  
org.label-schema.version="$VERSION" \  
org.label-schema.schema-version="1.0"  
  
# FreeNAS metadata  
LABEL org.freenas.autostart="true" \  
org.freenas.bridged="false" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.port-mappings="9876:9876/tcp" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"T411_USERNAME\", \  
\"descr\": \"T411 login name\", \  
\"optional\": false \  
}, \  
{ \  
\"env\": \"T411_PASSWORD\", \  
\"descr\": \"T411 password\", \  
\"optional\": false \  
} \  
]" \  
org.freenas.upgradeable="false" \  
org.freenas.version="$VERSION"  
  
# Add repos and install what we need  
RUN \  
apk upgrade --no-cache && \  
apk add --no-cache nodejs  
  
# Install T411-Torznab  
ADD https://github.com/KiLMaN/T411-Torznab/archive/master.zip /master.zip  
RUN unzip master.zip && \  
rm master.zip && \  
cd /T411-Torznab-master; npm install  
  
# Copy needed files  
COPY rootfs/ /  
  
# Ports  
EXPOSE 9876/tcp  
  
# Health check  
HEALTHCHECK CMD curl --connect-timeout 15 --show-error --silent --fail
--location "http://localhost:9876" > /dev/null || exit 1  

