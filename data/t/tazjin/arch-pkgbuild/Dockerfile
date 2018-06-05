FROM logankoester/archlinux  
MAINTAINER Vincent Ambo <tazjin@gmail.com>  
  
# Adding mirrorlist with Swedish servers for when I build locally  
# Doesn't matter much on Docker Hub  
ADD mirrorlist /etc/pacman.d/mirrorlist  
  
RUN pacman -Sy --noconfirm && \  
pacman -S archlinux-keyring --noconfirm && \  
pacman -Su --noconfirm  
RUN pacman -S --noconfirm base-devel sudo  
  
VOLUME /build  
WORKDIR /build  
  
ADD sudoers /etc/sudoers  
# Set up user & sudo  
RUN useradd -d /build -G wheel build && \  
chmod 0400 /etc/sudoers  
  
USER build  
  
# Options: Install dependencies, force package build, clean afterwards  
ENTRYPOINT sudo chown build: /build && \  
/usr/bin/makepkg -sfc --noconfirm --needed  

