FROM base/archlinux  
MAINTAINER Sebastian Schneider <mail@sesc.eu>  
  
# install fetchmail  
RUN pacman -Sy \  
&& pacman-db-upgrade \  
&& pacman -S fetchmail --noconfirm --ignore systemd \  
&& rm -rf /home /srv /mnt /opt /boot /root /tmp/* /var/tmp/  
  
VOLUME ["/data"]  
ADD fetchmail_daemon.sh /bin/fetchmail_daemon.sh  
  
ENTRYPOINT ["/bin/fetchmail_daemon.sh"]  
  

