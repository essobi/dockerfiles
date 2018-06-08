FROM archimg/base-devel  
  
RUN pacman-key --init \  
&& pacman-key --populate archlinux \  
&& pacman --noconfirm -Syu \  
&& pacman --noconfirm -S texlive-most minted \  
&& rm -f \  
/var/cache/pacman/pkg/*  
  
WORKDIR /data

