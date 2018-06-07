FROM scratch  
MAINTAINER ChihChieh Huang <soem.hcc@gmail.com>  
  
ADD ONBUILD/archlinux-base.tar.xz /  
  
RUN pacman-key --init && \  
pacman-key --populate archlinux && \  
pacman -Syy --noconfirm  

