FROM base/archlinux  
MAINTAINER Taylor "Nekroze" Lawson  
  
RUN pacman -Sy --noconfirm  
RUN pacman -S --noconfirm python2-pyopenssl git  
  
RUN git clone -b tvrage-fix https://github.com/Nekroze/usntssearch.git
/usntssearch  
  
VOLUME /mnt/state  
expose 5000  
CMD touch /mnt/state/custom_params.ini && ln -s /mnt/state/custom_params.ini
/usntssearch/NZBmegasearch/custom_params.ini && python2
/usntssearch/NZBmegasearch/mega2.py  

