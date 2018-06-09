FROM justin8/archlinux  
MAINTAINER justin@dray.be  
  
RUN pacman -Syq --noprogressbar --noconfirm expect && rm -rf
/var/cache/pacman/pkg/*  
ADD installer.sh /  
RUN chmod +x /installer.sh; /installer.sh && rm -rf /var/cache/pacman/pkg/* &&
\  
pacman -Syq --noprogressbar --noconfirm sonarr-develop && rm -rf
/var/cache/pacman/pkg/*  
  
VOLUME "/config"  
  
EXPOSE 8989  
CMD ["/usr/bin/sonarr", "-nobrowser", "-data=/config"]  

