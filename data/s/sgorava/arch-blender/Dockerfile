FROM base/archlinux  
MAINTAINER Juraj Oravec <sgd.orava@gmail.com>  
  
RUN pacman -Syu --noconfirm && \  
pacman -S --noconfirm \  
blender \  
git \  
python-lxml \  
python-prettytable \  
python-testfixtures  
  
RUN pacman -Scc --noconfirm  
  
RUN mkdir /data  
RUN mkdir /root/.glportal  
  
COPY data/userpref.blend /root/.config/blender/2.79/config/userpref.blend  
COPY data/run-tests /usr/bin/run-tests  
  
WORKDIR /data  
  
CMD run-tests  

