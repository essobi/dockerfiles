FROM railgunaccelerator/archlinux  
RUN pacman -S freeradius --noconfirm  
EXPOSE 1812/udp 1813/udp  
CMD ["/usr/sbin/radiusd", "-f"]  

