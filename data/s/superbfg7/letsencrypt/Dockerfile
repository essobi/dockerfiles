FROM superbfg7/archlinux-minimal  
  
RUN pacmaster.sh -Syu --noconfirm certbot && /bin/yes | pacman -Scc  
  
VOLUME /etc/letsencrypt  
VOLUME /var/log/letsencrypt  
VOLUME /srv/httpd  
  
CMD ["/usr/bin/certbot", "renew"]  

