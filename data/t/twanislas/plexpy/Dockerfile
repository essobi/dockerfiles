FROM twanislas/base-debian  
MAINTAINER Antoine Rahier <antoine.rahier@gmail.com>  
LABEL maintainer="Antoine Rahier <antoine.rahier@gmail.com>"  
# Build-time metadata  
ARG DEBIAN_FRONTEND=noninteractive  
ARG BUILD_DATE  
ARG VCS_REF  
LABEL org.label-schema.build-date="$BUILD_DATE" \  
org.label-schema.name="docker-plexpy" \  
org.label-schema.description="Docker container for PlexPy, based on latest
Debian stable" \  
org.label-schema.url="https://github.com/Twanislas/docker-plexpy" \  
org.label-schema.vcs-ref="$VCS_REF" \  
org.label-schema.vcs-url="https://github.com/Twanislas/docker-plexpy" \  
org.label-schema.vendor="Antoine Rahier" \  
org.label-schema.schema-version="1.0"  
# Environment settings  
ENV HOME="/config"  
# Add repos and install what we need  
RUN \  
apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get -y install curl git python2.7  
  
# Copy needed files  
COPY rootfs/ /  
  
# Ports  
EXPOSE 8181/tcp  
  
# Volumes  
VOLUME /config /logs  
  
# Health check  
HEALTHCHECK CMD curl --connect-timeout 15 --show-error \--silent --fail
--location "http://localhost:8181" > /dev/null || exit 1  

