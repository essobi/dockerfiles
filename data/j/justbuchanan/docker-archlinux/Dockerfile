FROM base/archlinux  
MAINTAINER Justin Buchanan <justbuchanan@gmail.com>  
  
# update/init keyring  
RUN pacman-key --init  
RUN pacman-key --populate archlinux  
  
# update keyring  
RUN pacman --noconfirm -Sy archlinux-keyring  
  
# update packages  
RUN pacman -Syyu --noconfirm  
#clear package cache  
RUN rm /var/cache/pacman/pkg/*  
  
# upgrade db  
RUN pacman-db-upgrade  
  
# clear package cache to save disk space  
RUN pacman -Scc --noconfirm  

