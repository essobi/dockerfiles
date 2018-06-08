FROM base/archlinux  
MAINTAINER Taylor "Nekroze" Lawson  
  
RUN pacman -Sy --noconfirm  
RUN pacman -S --noconfirm python2-pyopenssl git  
RUN pacman -S --noconfirm python2-cheetah  
  
RUN git clone https://github.com/midgetspy/Sick-Beard.git /sickbeard  
  
VOLUME /mnt/state  
expose 8081  
ENTRYPOINT python2 /sickbeard/SickBeard.py --datadir=/mnt/state  

