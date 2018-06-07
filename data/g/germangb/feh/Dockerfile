#  
# docker run --rm \  
# -v $HOME/Pictures:/root \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -e DISPLAY=$DISPLAY \  
# germangb/feh "$@"  
#  
FROM rafaelsoares/archlinux  
MAINTAINER German Gomez <germangb42@gmail.com>  
  
## Update package database  
RUN pacman -Sy  
  
## Install alsa-utils package, which contains alsamixer  
## and amixer utilities  
RUN pacman -S --noconfirm feh  
  
## Entrypoint script  
COPY entry.sh /entry.sh  
RUN chmod +x /entry.sh  
  
## Working directory set to root  
WORKDIR /root  
  
## Entry point  
ENTRYPOINT ["/entry.sh"]  

