FROM base/archlinux  
MAINTAINER Taylor "Nekroze" Lawson  
  
RUN pacman -Sy --noconfirm  
RUN pacman -S --noconfirm python2-pyopenssl git  
  
RUN git clone https://github.com/RuudBurger/CouchPotatoServer.git /couchpotato  
  
VOLUME /root/.couchpotato/  
  
expose 5050  
ENTRYPOINT python2 /couchpotato/CouchPotato.py  

