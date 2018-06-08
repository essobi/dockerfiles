FROM base/archlinux  
MAINTAINER Oscar Morante <oscar@mooistudios.com>  
  
# update key  
RUN pacman -Syy  
RUN pacman-key --populate  
RUN pacman-key --keyserver ipv4.pool.sks-keyservers.net --refresh-keys  
RUN pacman --noconfirm -Sy archlinux-keyring  
  
# upgrade system and install dependencies  
RUN pacman --noconfirm -Syyu  
RUN pacman-db-upgrade  
  
# Add sudo user  
RUN pacman --noconfirm -S sudo  
RUN useradd -m user -s /bin/bash  
RUN echo "user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
# Install base-devel  
RUN pacman --noconfirm -S base-devel  
RUN pacman --noconfirm -S vi  
USER user  
# Install cower from AUR  
RUN gpg --keyserver ipv4.pool.sks-keyservers.net --recv-keys 1EB2638FF56C0C53  
RUN curl -s https://aur.archlinux.org/cgit/aur.git/snapshot/cower.tar.gz \  
| tar zxf - -C /tmp \  
&& cd /tmp/cower \  
&& makepkg --noconfirm -rsi  
RUN rm -rf /tmp/cower  
  
# Install pacaur from AUR  
RUN curl -s https://aur.archlinux.org/cgit/aur.git/snapshot/pacaur.tar.gz \  
| tar zxf - -C /tmp \  
&& cd /tmp/pacaur \  
&& makepkg --noconfirm -rsi  
  
RUN rm -rf /tmp/pacaur  
  
# Clean up  
RUN sudo rm -rf /var/cache/pacman  
  

