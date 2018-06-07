FROM base/archlinux  
RUN pacman -Sy --noconfirm archlinux-keyring  
RUN pacman-key --refresh-keys  
RUN pacman -Syu --noconfirm --force inkscape  
CMD /usr/bin/inkscape  

