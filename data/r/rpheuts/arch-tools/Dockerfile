# Use when bootstrapping  
#FROM rpheuts/arch-build  
FROM rpheuts/archlinux  
  
RUN mkdir /run/shm  
RUN mkdir /work  
  
RUN pacman -S --noconfirm archiso  
RUN pacman -S --noconfirm expect  
  
WORKDIR /work/  
ENTRYPOINT exec /work/mkimage-arch.sh  

