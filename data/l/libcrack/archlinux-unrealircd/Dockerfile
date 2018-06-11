FROM base/archlinux:latest  
  
MAINTAINER libcrack <devnull@libcrack.so>  
  
RUN echo -e "[extra]\nInclude = /etc/pacman.d/mirrorlist\n" >>
/etc/pacman.conf && \  
echo -e "[community]\nInclude = /etc/pacman.d/mirrorlist\n" >>
/etc/pacman.conf && \  
pacman -Syy --noconfirm && \  
pacman -S --noconfirm archlinux-keyring && \  
pacman-db-upgrade && \  
pacman -S --noconfirm extra/c-ares core/curl community/unrealircd  
  
EXPOSE 6697  
EXPOSE 7000  
CMD ["/usr/bin/unrealircd","-F"]  
  

