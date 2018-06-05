FROM base/archlinux  
  
# update the base system and install tools for building packages  
RUN pacman -Syu --noconfirm base-devel  
  
# add a non-root user in order to build packages  
RUN useradd -ms /bin/bash docker \  
&& echo "docker ALL=NOPASSWD:/usr/bin/pacman,/usr/bin/aura" >> /etc/sudoers  
WORKDIR /home/docker  
  
# download aura package manager  
ADD https://aur.archlinux.org/cgit/aur.git/snapshot/aura-bin.tar.gz
/home/docker/aura.tar.gz  
RUN chown docker aura.tar.gz  
  
# build and install the aura package manager  
USER docker  
RUN tar -zxvf aura.tar.gz \  
&& cd aura-bin \  
&& makepkg \  
&& sudo pacman -U --noconfirm aura-bin-*.tar.xz  

