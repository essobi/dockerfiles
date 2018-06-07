FROM mooistudios/archlinux  
MAINTAINER Oscar Morante <oscar@mooistudios.com>  
  
RUN pacaur --noconfirm -S bitlbee libotr bitlbee-libpurple purple-hangouts-hg  
ADD run.sh /run.sh  
  
USER root  
RUN rm -rf /var/cache/pacman  
RUN rm -rf /home/user/.cache/pacaur  
  
WORKDIR /var/lib/bitlbee  
CMD /run.sh  
  

