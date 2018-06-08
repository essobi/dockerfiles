FROM scratch  
  
ADD add_files/archlinux.tar.xz /  
  
RUN /bin/pacman-key --init \  
&& /bin/pacman-key --populate archlinux \  
&& /bin/pacman -Syu --noconfirm  
  
ENTRYPOINT [ "/bin/bash" ]  

