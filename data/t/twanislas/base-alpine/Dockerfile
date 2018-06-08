FROM alpine:latest  
MAINTAINER Antoine Rahier <antoine.rahier@gmail.com>  
  
# Build-time metadata  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date="$BUILD_DATE" \  
org.label-schema.name="base-alpine" \  
org.label-schema.description="Docker container used as a base for other
containers, based on latest Alpine Linux" \  
org.label-schema.url="https://github.com/Twanislas/docker-base-alpine" \  
org.label-schema.vcs-ref="$VCS_REF" \  
org.label-schema.vcs-url="https://github.com/Twanislas/docker-base-alpine" \  
org.label-schema.vendor="Antoine Rahier" \  
org.label-schema.version="$VERSION" \  
org.label-schema.schema-version="1.0"  
  
# root filesystem  
COPY rootfs /  
  
# Install s6 overlay  
RUN \  
apk add --no-cache curl openssl && \  
wget "https://github.com/just-containers/s6-overlay/releases/download/$(wget
-q https://github.com/just-containers/s6-overlay/releases/latest -O - | grep
-m 1 -E \"\>v | awk -F "[><]" '{print $3}')/s6-overlay-amd64.tar.gz" && \  
tar -xzf s6-overlay-amd64.tar.gz -C / && \  
rm s6-overlay-amd64.tar.gz  
  
## Init  
ENTRYPOINT [ "/init" ]  

