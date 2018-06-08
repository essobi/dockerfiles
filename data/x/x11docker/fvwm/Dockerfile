# x11docker/fvwm  
#  
# FVWM window manager in docker  
# Petite image based on alpine  
#  
# Use x11docker to run image.  
# Get x11docker from github:  
# https://github.com/mviereck/x11docker  
#  
# Examples:  
# Desktop:  
# x11docker --desktop x11docker/fvwm  
# Desktop with init system openrc:  
# x11docker --desktop --openrc x11docker/fvwm  
# Single application (terminal):  
# x11docker x11docker/fvwm xterm  
#  
# Options:  
# Persistent home folder stored on host with --home  
# Shared host folder with --sharedir DIR  
# Clipboard sharing with option --clipboard  
# Sound support with option --alsa  
#  
# Look at x11docker --help for further options.  
  
FROM alpine:edge  
RUN apk add --no-cache fvwm font-bitstream-type1 xterm && \  
apk add --no-cache dbus openrc && \  
cp /usr/share/fvwm/default-config/Fvwm* /usr/share/fvwm  
CMD fvwm  

