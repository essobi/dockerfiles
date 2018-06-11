FROM archimg/base-devel  
MAINTAINER Krzysztof Nazarewski <nazarewk+docker@gmail.com>  
  
ADD archlinuxfr /tmp/archlinuxfr  
RUN cat /tmp/archlinuxfr >> /etc/pacman.conf && pacman -Syu --noconfirm  
RUN pacman -S --noconfirm yaourt && paccache -rk 0  
ADD sudoers /etc/sudoers.d/sudoers  
RUN useradd -G wheel arch  
USER arch  
WORKDIR /home/arch  

