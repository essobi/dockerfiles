FROM ubuntu:latest  
MAINTAINER Antoine Rahier <antoine.rahier@gmail.com>  
  
ARG DEBIAN_FRONTEND="noninteractive"  
ENV TERM="xterm" LANG="C.UTF-8" LC_ALL="C.UTF-8"  
# Build-time metadata  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION=0.0.4  
LABEL org.label-schema.build-date="$BUILD_DATE" \  
org.label-schema.name="base-ubuntu" \  
org.label-schema.description="Base docker image based on latest Ubuntu LTS
with s6-overlay preinstalled" \  
org.label-schema.url="https://github.com/Twanislas/docker-base-ubuntu" \  
org.label-schema.vcs-ref="$VCS_REF" \  
org.label-schema.vcs-url="https://github.com/Twanislas/docker-base-ubuntu" \  
org.label-schema.vendor="Antoine Rahier" \  
org.label-schema.version="$VERSION" \  
org.label-schema.schema-version="1.0"  
  
# root filesystem  
COPY rootfs /  
  
# Add repos, upgrade, and install s6 overlay  
RUN sed -i 's/^#\s*\\(deb.*multiverse\\)$/\1/g' /etc/apt/sources.list && \  
sed -i 's/^#\s*\\(deb.*backports\\)$/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y apt-utils && \  
apt-get dist-upgrade -y && \  
apt-get install -y wget curl openssl && \  
wget "https://github.com/just-containers/s6-overlay/releases/download/$(wget
-q https://github.com/just-containers/s6-overlay/releases/latest -O - | grep
-m 1 -E \"\>v | awk -F "[><]" '{print $3}')/s6-overlay-amd64.tar.gz" && \  
tar -xzf s6-overlay-amd64.tar.gz -C / && \  
rm s6-overlay-amd64.tar.gz  
  
# Copy needed files  
COPY rootfs/ /  
  
## Init  
ENTRYPOINT [ "/init" ]  

