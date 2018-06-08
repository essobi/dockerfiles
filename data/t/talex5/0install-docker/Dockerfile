FROM nfnty/arch-mini  
RUN useradd -m user  
RUN pacman --noconfirm -Sy  
RUN pacman --noconfirm -S git sudo base-devel unzip  
WORKDIR /home/user  
RUN echo 'user ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers  
USER user  
RUN git clone https://aur.archlinux.org/package-query.git  
RUN git clone https://aur.archlinux.org/yaourt.git  
WORKDIR /home/user/package-query  
RUN makepkg --noconfirm -si  
WORKDIR /home/user/yaourt  
RUN makepkg --noconfirm -si  
RUN yaourt --noconfirm -Syu  
  
RUN gpg --recv-key AE07828059A53CC1  
RUN echo '92429807C9853C0744A68B9AAE07828059A53CC1:6:' | gpg --import-
ownertrust  
RUN yaourt --noconfirm -S zeroinstall-injector  

