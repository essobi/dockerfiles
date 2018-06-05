#  
# docker run -ti --rm \  
# \--device /dev/snd \  
# germangb/alsa-utils \  
# alsamixer "@"  
#  
FROM rafaelsoares/archlinux  
MAINTAINER German Gomez <germangb42@gmail.com>  
  
## Update package database  
RUN pacman -Sy  
  
## Install alsa-utils package, which contains alsamixer  
## and amixer utilities  
RUN pacman -S --noconfirm alsa-utils && pacman -Scc --noconfirm  

