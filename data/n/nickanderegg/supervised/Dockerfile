FROM ubuntu:16.04  
MAINTAINER Nick Anderegg <git@anderegg.io>  
  
ARG OVERLAY_VERSION="v1.19.1.1"  
ARG OVERLAY_ARCHITECTURE="amd64"  
ARG OVERLAY_URL="https://github.com/just-
containers/s6-overlay/releases/download/${OVERLAY_VERSION}/s6-overlay-${OVERLAY_ARCHITECTURE}.tar.gz"  
ARG DEBIAN_FRONTEND="noninteractive"  
  
ENV TERM="xterm" \  
LANG="C.UTF-8" \  
LC_ALL="C.UTF-8" \  
HOME="/root"  
  
RUN \  
# Enable Universe and Multiverse  
sed -i 's/^#\s*\\(deb.*universe\\)$/\1/g' /etc/apt/sources.list && \  
sed -i 's/^#\s*\\(deb.*multiverse\\)$/\1/g' /etc/apt/sources.list && \  
# Install necessary utilities  
apt-get update && \  
apt-get install \--assume-yes \--no-install-recommends apt-utils && \  
apt-get install \--assume-yes \--no-install-recommends \  
ca-certificates \  
curl && \  
  
# Download, verify, and install s6 overlay  
curl \  
\--silent \--show-error \  
\--output /tmp/s6-overlay.tar.gz \  
\--location "${OVERLAY_URL}" && \  
  
curl -sS https://keybase.io/justcontainers/key.asc | gpg \--quiet \--import &&
\  
curl -sS -L "${OVERLAY_URL}.sig" | gpg \--quiet \--verify \-
/tmp/s6-overlay.tar.gz && \  
tar xzf /tmp/s6-overlay.tar.gz -C / && \  
  
# Cleanup  
# Upgrade packages  
apt-get dist-upgrade \--assume-yes \--no-install-recommends && \  
apt-get autoremove && \  
apt-get clean && \  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
ENTRYPOINT ["/init"]  

