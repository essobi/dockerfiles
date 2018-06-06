FROM craftdock/alpine-runit:latest  
  
LABEL maintainer="Hexosse <hexosse@gmail.com>" \  
description="Minimal Alpine image with Caddy server."  
  
RUN \  
# Print executed commands  
set -x \  
# Update repository indexes  
&& apk-update \  
# Install Caddy server  
&& apk-install --repository http://dl-
cdn.alpinelinux.org/alpine/edge/community/ \  
caddy \  
# Clear apk's cache  
&& apk-remove .build-dependencies \  
&& apk-cleanup  
  
# Copy scripts  
COPY ./rootfs /  
  
# Add volume to allow persistence  
VOLUME ["/etc/caddy", "/etc/caddy/certificates", "/var/www", "/var/log"]  
  
# Expose http, https and caddy port  
EXPOSE 80 443 2015  

