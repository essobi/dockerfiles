FROM archlinuxjp/archlinux  
MAINTAINER "Masaki Waga" <masakiwaga@gmail.com>  
ENV container docker  
  
# Update building environment  
RUN pacman -Sy --needed base-devel --noconfirm  
  
# Install depending packages  
RUN pacman -S re2 boost-libs boost --noconfirm  

