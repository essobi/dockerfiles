# x11docker/fluxbox  
#  
# Run fluxbox window manager in docker.  
# Use x11docker to run image.  
# Get x11docker from github:  
# https://github.com/mviereck/x11docker  
#  
# Examples: x11docker --desktop x11docker/fluxbox  
# x11docker x11docker/lxde eterm  
#  
# Options:  
# Persistent home folder stored on host with --home  
# Shared host folder with --sharedir DIR  
# Clipboard sharing with option --clipboard  
# Sound support with option --alsa  
#  
# See x11docker --help for further options.  
  
FROM debian:stretch-slim  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --no-install-recommends \  
fluxbox eterm && \  
rm -rf /var/lib/apt/lists/*  
ENV DEBIAN_FRONTEND newt  
  
CMD fluxbox  

