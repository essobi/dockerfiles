FROM base/archlinux  
MAINTAINER Taylor "Nekroze" Lawson  
  
RUN pacman -Sy --noconfirm  
RUN pacman -S --noconfirm python2-pyopenssl git  
  
RUN git clone https://github.com/rembo10/headphones.git /headphones  
  
VOLUME /config  
  
EXPOSE 8181  
CMD python2 /headphones/Headphones.py --datadir /config  

