FROM base/archlinux  
MAINTAINER Taylor "Nekroze" Lawson  
  
RUN pacman -Sy --noconfirm  
RUN pacman -S --noconfirm python2-mako deluge unrar unzip  
  
VOLUME /config  
  
EXPOSE 8112 58846  
  
CMD /usr/bin/deluged -c /config && /usr/bin/deluge-web -c /config  

