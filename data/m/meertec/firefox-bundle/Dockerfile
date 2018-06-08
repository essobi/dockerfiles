FROM meertec/archlinux:latest  
  
MAINTAINER meertec  
  
ENV uid 1000  
ENV gid 1000  
RUN mkdir -p /etc/pacman.d/;echo 'nameserver 8.8.8.8'>/etc/resolv.conf  
COPY mirrorlist /etc/pacman.d/mirrorlist  
  
RUN pacman -Syy --noconfirm;pacman -S firefox ttf-bitstream-vera
--noconfirm;useradd -m firefox; rm -rf /var/cache/pacman/pkg;  
  
USER firefox  
ENV HOME /home/firefox  
  
CMD /usr/bin/firefox --new-instance  
  

