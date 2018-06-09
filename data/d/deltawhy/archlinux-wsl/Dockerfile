FROM archimg/base-devel  
  
RUN : \  
&& useradd --user-group \--create-home user \  
&& chown user /usr/src \  
&& pacman -Sy --noconfirm gd git  
USER user  
RUN : \  
&& cd /usr/src \  
&& git clone https://aur.archlinux.org/glibc-wsl.git \  
&& cd glibc-wsl \  
&& makepkg -si \  
&& cd .. \  
&& git clone git://git.archlinux.org/svntogit/packages.git --depth=1
\--branch=packages/fakeroot \  
&& cd packages/trunk \  
&& sed -i 's/--with-ipc=sysv$/--with-ipc=tcp/' PKGBUILD \  
&& makepkg -si --noconfirm \  
&& cd && rm -rf /usr/src/glibc-wsl && rm -rf /usr/src/packages  
USER root  
RUN : \  
&& userdel --remove user \  
&& groupdel user  

