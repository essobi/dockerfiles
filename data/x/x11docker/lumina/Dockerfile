# x11docker/lumina  
#  
# Run lumina desktop in docker.  
# Use x11docker to run image.  
# Get x11docker from github:  
# https://github.com/mviereck/x11docker  
#  
# Run desktop with:  
# x11docker --desktop x11docker/lumina  
#  
# Run single application:  
# x11docker x11docker/lumina xterm  
#  
# You can add hardware acceleration with option --gpu  
# You can create a persistent home folder with option --home  
# You can share clipboard with host with option --clipboard  
# See x11docker --help for further options.  
#  
FROM voidlinux/voidlinux  
  
RUN xbps-install -Suy lumina dbus liberation-fonts-ttf xterm \  
mesa-ati-dri mesa-intel-dri mesa-nouveau-dri kmod xz ||:  
  
CMD start-lumina-desktop  
  

