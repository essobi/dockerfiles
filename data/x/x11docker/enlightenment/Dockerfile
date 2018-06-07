# x11docker/enlightenment  
#  
# Run enlightenment desktop in docker.  
#  
# Use x11docker to run image.  
# Get x11docker script and x11docker-gui from github:  
# https://github.com/mviereck/x11docker  
#  
# Run with hardware acceleration and init system runit:  
# x11docker --desktop --gpu --runit x11docker/enlightenment  
#  
  
# Options:  
# Persistent home folder stored on host with --home  
# Shared host folder with --sharedir DIR  
# Hardware acceleration with option --gpu  
# Clipboard sharing with option --clipboard  
# Sound support with option --alsa  
# With pulseaudio in image, sound support with --pulseaudio  
# Language locale setting with --lang=$LANG  
#  
# Look at x11docker --help for further options.  
  
FROM voidlinux/voidlinux  
  
RUN xbps-install -Su -y  
RUN xbps-install -S -y enlightenment liberation-fonts-ttf \  
ConsoleKit2 leafpad lxterminal \  
mesa-ati-dri mesa-intel-dri mesa-nouveau-dri kmod xz ||:  
  
CMD enlightenment_start  

