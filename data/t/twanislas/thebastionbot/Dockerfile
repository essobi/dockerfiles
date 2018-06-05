FROM node:8  
ARG DEBIAN_FRONTEND="noninteractive"  
# Build-time metadata  
ARG BUILD_DATE  
ARG VCS_REF  
LABEL maintainer="Antoine Rahier <antoine.rahier@gmail.com>" \  
org.label-schema.build-date="$BUILD_DATE" \  
org.label-schema.name="thebastionbot" \  
org.label-schema.description="The Bastion Discord bot, Docker edition" \  
org.label-schema.url="https://github.com/Twanislas/docker-thebastionbot" \  
org.label-schema.vcs-ref="$VCS_REF" \  
org.label-schema.vcs-url="https://github.com/Twanislas/docker-thebastionbot" \  
org.label-schema.vendor="Antoine Rahier" \  
org.label-schema.schema-version="1.0"  
  
# Install Bastion & its deps  
RUN \  
apt-get update && \  
apt-get install -y apt-utils && \  
apt-get dist-upgrade -y && \  
apt-get install -y build-essential git openssl python && \  
cd /opt && \  
git clone -b stable -q --depth 1 https://github.com/TheBastionBot/Bastion.git
&& \  
cd Bastion && \  
npm i ffmpeg-binaries && \  
npm i --only=production --no-package-lock  
  
# Volumes  
VOLUME /opt/Bastion/data /opt/Bastion/settings  
  
# Init  
WORKDIR /opt/Bastion  
ENTRYPOINT [ "node","." ]

