FROM superbfg7/archlinux-minimal  
  
RUN pacmaster.sh -Syu --noconfirm postgrey && /bin/yes | pacman -Scc && \  
mkdir -p /var/spool/postfix/postgrey && \  
groupadd -r postgrey && \  
useradd -r -d /var/spool/postfix/postgrey -g postgrey -s /bin/false postgrey
&& \  
chown postgrey.postgrey /var/spool/postfix/postgrey  
  
EXPOSE 10030  
CMD ["/usr/bin/postgrey", "--inet=0.0.0.0:10030", "--
pidfile=/run/postgrey/postgrey.pid", "--group=postgrey", "--user=postgrey", "
--greylist-text='Greylisted for %s seconds'"]  
  

