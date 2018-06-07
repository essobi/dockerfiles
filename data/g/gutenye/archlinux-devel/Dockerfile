FROM nfnty/arch-devel  
  
#RUN echo 'Server = http://mirrors.aliyun.com/archlinux/$repo/os/$arch' >
/etc/pacman.d/mirrorlist  
RUN sed -i 's/#RemoteFileSigLevel = Required/RemoteFileSigLevel = Optional/'
/etc/pacman.conf && \  
pacman -U --noconfirm
https://github.com/gutenye/archive/releases/download/pacaur/cower-12-2-x86_64.pkg.tar.xz
https://github.com/gutenye/archive/releases/download/pacaur/pacaur-4.2.27-1-any.pkg.tar.xz
&& \  
echo -e "y\ny" | sudo pacman -Scc && \  
useradd -m -G wheel docker && \  
sed -i 's/# %wheel ALL=(ALL) NOPASSWD: ALL/%wheel ALL=(ALL) NOPASSWD: ALL/g'
/etc/sudoers  
  
USER docker  
WORKDIR /home/docker  
  
COPY pacaur.conf /etc/xdg/pacaur/config  
RUN pacaur -S --noconfirm gutaur  

