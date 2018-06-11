FROM twanislas/base-debian  
MAINTAINER Antoine Rahier <antoine.rahier@gmail.com>  
LABEL maintainer="Antoine Rahier <antoine.rahier@gmail.com>"  
# Build-time metadata  
ARG DEBIAN_FRONTEND=noninteractive  
ARG BUILD_DATE  
ARG VCS_REF  
LABEL org.label-schema.build-date="$BUILD_DATE" \  
org.label-schema.name="docker-unifi" \  
org.label-schema.description="Docker container for Unifi, based on Debian" \  
org.label-schema.url="https://github.com/Twanislas/docker-unifi" \  
org.label-schema.vcs-ref="$VCS_REF" \  
org.label-schema.vcs-url="https://github.com/Twanislas/docker-unifi" \  
org.label-schema.vendor="Antoine Rahier" \  
org.label-schema.schema-version="1.0"  
# Environment settings  
ENV HOME="/config"  
# Copy needed files  
COPY rootfs/ /  
  
# Install Unifi  
RUN \  
addgroup --system --gid ${APP_GID:-2000} unifi && \  
adduser --system --home /config \--shell /sbin/nologin --no-create-home --uid
${APP_UID:-2000} \--ingroup unifi --disabled-password --disabled-login unifi
&& \  
apt-get install -y gnupg && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv 06E85760C0A52C50 && \  
apt-get update && \  
mkdir /usr/share/man/man1 && \  
apt-get install -y curl unifi  
  
# Ports  
EXPOSE \  
3478/udp \  
5656:5699/udp \  
8080/tcp \  
8443/tcp \  
8880/tcp \  
6789/tcp \  
10001/udp  
  
# Volumes  
VOLUME /config  
  
## Init  
ENTRYPOINT [ "/init" ]  
  
# Health check  
HEALTHCHECK CMD curl --connect-timeout 15 --show-error \--silent --fail
--insecure --location "http://localhost:8080" > /dev/null || exit 1

