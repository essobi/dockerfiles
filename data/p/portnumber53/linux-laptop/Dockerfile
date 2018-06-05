FROM base/archlinux  
MAINTAINER grimlock@portnumber53.com  
  
# Updating keys and system  
RUN pacman-db-upgrade  
RUN pacman -Sy --noconfirm archlinux-keyring  
RUN pacman-key --init && pacman-key --populate archlinux && pacman-key
--refresh-keys  
RUN pacman -Syyu --noconfirm  
  

