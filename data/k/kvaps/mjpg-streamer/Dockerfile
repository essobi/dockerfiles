FROM pritunl/archlinux  
MAINTAINER kvaps <kvapss@gmail.com>  
  
RUN pacman --noconfirm -Sy base-devel  
RUN curl -L https://aur.archlinux.org/cgit/aur.git/snapshot/mjpg-
streamer.tar.gz | tar -xzv -C /usr/src/  
WORKDIR /usr/src/mjpg-streamer  
RUN useradd makepkg ; echo "makepkg ALL = (root) NOPASSWD:ALL" >>
/etc/sudoers.d/makepkg  
RUN chown makepkg -R .  
RUN su -c "makepkg -si --noconfirm" -s /bin/bash makepkg  
  
ENTRYPOINT [ "mjpg_streamer" ]  

