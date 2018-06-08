FROM base/archlinux  
MAINTAINER Taylor "Nekroze" Lawson  
  
RUN pacman -Sy --noconfirm  
RUN pacman -S --noconfirm python2-pyopenssl git  
RUN pacman -S --noconfirm python2-cheetah  
RUN pacman -S --noconfirm par2cmdline unzip unrar  
  
RUN git clone https://github.com/sabnzbd/sabnzbd.git /sabnzbd  
  
VOLUME /config  
  
expose 8080  
ENTRYPOINT python2 /sabnzbd/SABnzbd.py --config-file /config --server :8080  

