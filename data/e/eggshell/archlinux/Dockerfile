FROM base/archlinux  
MAINTAINER eggshell <cullentaylor@outlook.com>  
  
# update pacman's mirror list  
RUN curl -so /etc/pacman.d/mirrorlist
"https://www.archlinux.org/mirrorlist/?country=all&protocol=https&ip_version=6&use_mirror_status=on"
&& \  
sed -i 's/^#//' /etc/pacman.d/mirrorlist  
  
# find the fastest mirror according to the image's build location  
RUN mv /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.orig && \  
rankmirrors -n 6 /etc/pacman.d/mirrorlist.orig > /etc/pacman.d/mirrorlist && \  
pacman -Syy  
  
# refresh keys, sync packages, refresh package database and upgrade all
packages  
# that exist on the image  
ONBUILD RUN pacman-key --refresh-keys && \  
pacman -Sy --noprogressbar --noconfirm && \  
pacman -S --force openssl pacman --noconfirm && \  
pacman-db-upgrade && \  
pacman -Syyu --noprogressbar --noconfirm  

