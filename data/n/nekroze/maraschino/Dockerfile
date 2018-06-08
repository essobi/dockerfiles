FROM base/archlinux  
MAINTAINER Taylor "Nekroze" Lawson  
  
RUN pacman -Sy --noconfirm  
RUN pacman -S --noconfirm git python2-pyopenssl  
RUN pacman -S --noconfirm openssh sshpass  
  
RUN git clone https://github.com/mrkipling/maraschino.git /maraschino  
  
VOLUME /config  
  
EXPOSE 7000  
CMD python2 /maraschino/Maraschino.py --datadir /config  

