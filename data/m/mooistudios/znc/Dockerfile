FROM mooistudios/archlinux  
MAINTAINER Oscar Morante <oscar@mooistudios.com>  
  
RUN pacaur --noconfirm -S znc-git znc-clientbuffer-git  
  
USER root  
RUN rm -rf /var/cache/pacman  
RUN rm -rf /home/user/.cache/pacaur  
  
WORKDIR /var/lib/znc  
CMD znc -rf  
  

