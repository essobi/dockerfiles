# DESCRIPTION: LXQt desktop on Arch Linux  
# AUTHOR: rookiepeng (https://zpeng.me)  
FROM base/archlinux:latest  
MAINTAINER rookiepeng  
  
RUN pacman --sync --noconfirm --refresh --sysupgrade && \  
pacman --sync --noconfirm lxqt \  
breeze-icons \  
sudo \  
gvfs \  
&& \  
find /var/cache/pacman/pkg -mindepth 1 -delete  
  
RUN useradd -m -G wheel -d /home/archie -s /bin/bash archie  
RUN echo "archie:archie" | chpasswd  
RUN echo '%wheel ALL=(ALL) ALL' >> /etc/sudoers  
  
USER archie  
  
#ENV HOME /home/archie  
ENTRYPOINT [ "startlxqt" ]

