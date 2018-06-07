FROM base/archlinux  
MAINTAINER Taylor "Nekroze" Lawson  
  
RUN pacman -Sy --noconfirm  
RUN pacman -S --noconfirm python2 git  
  
RUN git clone https://github.com/itsmegb/LazyLibrarian.git /lazylibrarian  
  
VOLUME /config  
  
EXPOSE 5299  
CMD python2 /lazylibrarian/LazyLibrarian.py --datadir /config  

