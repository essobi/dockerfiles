FROM base/archlinux  
  
  
# Add non privileged user  
RUN useradd -m user -s /bin/bash  
RUN echo "user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
# update key  
RUN pacman -Syy  
RUN pacman-key --populate  
RUN pacman-key --refresh-keys  
RUN pacman --noconfirm -Sy archlinux-keyring  
  
# upgrade system and install dependencies  
RUN pacman --noconfirm -Syyu  
RUN pacman-db-upgrade  
RUN pacman --noconfirm -S ca-certificates  
RUN pacman --noconfirm -S ca-certificates-mozilla  
  
# install yaourt  
RUN pacman --noconfirm -S sudo  
RUN pacman --noconfirm -S wget  
RUN pacman --noconfirm -S base-devel  
RUN pacman -S --noconfirm wget base-devel yajl  
ADD install_aur.sh /tmp/install_aur.sh  
RUN chmod +x /tmp/install_aur.sh  
USER user  
WORKDIR /tmp  
RUN /tmp/install_aur.sh package-query  
RUN /tmp/install_aur.sh yaourt  
  
RUN yaourt -V  
  

