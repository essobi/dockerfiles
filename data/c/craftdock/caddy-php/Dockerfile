FROM craftdock/alpine-php7:latest  
  
LABEL maintainer="Hexosse <hexosse@gmail.com>" \  
description="Minimal Alpine image with Caddy server and php."  
  
# When LOGGER is true, all outputs will be redirected to a log file  
ENV LOGGER=true  
  
RUN \  
# Print executed commands  
set -x \  
# Update repository indexes  
&& apk-update \  
# Add packages  
# Install Caddy server  
&& apk-install --repository http://dl-
cdn.alpinelinux.org/alpine/edge/community/ \  
caddy \  
# Clear apk's cache  
&& apk-cleanup  
  
# Copy scripts  
COPY ./rootfs /  
  
# Add volume to allow persistence  
VOLUME ["/root/.caddy", "/etc/caddy", "/var/www", "/var/log"]  
  
# Expose http, https and caddy port  
EXPOSE 80 443 2015  

