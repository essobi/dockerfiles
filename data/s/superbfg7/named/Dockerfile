FROM superbfg7/archlinux-minimal  
  
RUN pacmaster.sh -Syu --noconfirm systemd bind && /bin/yes | pacman -Scc && \  
pacmaster.sh -Rns --noconfirm systemd  
  
VOLUME /var/named  
EXPOSE 53 53/udp 953  
CMD ["/usr/sbin/named", "-f", "-u", "named", "-L", "/var/log/named"]  
  

