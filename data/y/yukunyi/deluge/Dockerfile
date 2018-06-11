FROM yukunyi/archlinux  
  
  
RUN pacman -S --noconfirm --needed deluge\  
python2-mako libtorrent-rasterbar python2-chardet python2-pyopenssl \  
python2-setuptools python2-twisted python2-xdg python2-notify \  
intltool librsvg python2-service-identity  
  
ADD start.sh /start.sh  
  
VOLUME ["/data"]  
# Torrent port  
EXPOSE 53160  
EXPOSE 53160/udp  
# WebUI  
EXPOSE 8112  
# Daemon  
EXPOSE 58846  
CMD ["/start.sh"]  

