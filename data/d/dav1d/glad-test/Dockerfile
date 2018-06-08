FROM greyltc/archlinux  
  
RUN pacman -Syu --noconfirm base-devel  
  
# glad dependencies  
RUN pacman -Syu --noconfirm python python-jinja python-lxml  
# test dependencies  
RUN pacman -Syu --noconfirm \  
xorg-server-xvfb \  
gcc glfw-x11  
# special test dependencies  
RUN echo -e "\n[multilib]\nInclude = /etc/pacman.d/mirrorlist\n" >>
/etc/pacman.conf  
RUN pacman -Syu --noconfirm wine winetricks  
RUN echo -e "\n[aur]\nSigLevel = Never\nServer =
http://repo.dav1d.de/archlinux/aur/os/\$arch\n" >> /etc/pacman.conf  
RUN pacman -Syu --noconfirm mingw-w64-gcc mingw-w64-glfw  
  
# setup  
RUN mkdir -p /var/lib/wine  
RUN chmod 777 /var/lib/wine  
  
# entrypoint setup  
ADD run /usr/local/bin/run  
  
WORKDIR /mnt  
VOLUME /mnt  
  
ENTRYPOINT ["/usr/local/bin/run"]  
CMD ["./utility/test.sh"]  
  

