FROM treemo/archlinux-with-yaourt  
  
  
# install pycharm  
RUN sudo pacman --noconfirm -S python2 python2-pip  
RUN sudo pacman --noconfirm -S python3 python-pip  
RUN sudo pacman --noconfirm -S git  
RUN sudo pacman --noconfirm -S libxrender freetype2 libxext libxtst  
RUN yaourt -S --noconfirm pycharm-professional  
  
# running  
ENTRYPOINT ["/usr/bin/pycharm"]  
  

