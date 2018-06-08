FROM nfnty/arch-mini:latest  
  
LABEL maintainer="Alexis Pereda <alexis@pereda.fr>, Cyrille Pierre"  
LABEL description="A toolchain for Nucleo devices"  
  
RUN echo>>/etc/pacman.conf -e '\n[archlinuxfr]\n\  
SigLevel = Never\n\  
Server = http://repo.archlinux.fr/$arch'  
  
RUN pacman --noconfirm --needed -Sy archlinux-keyring  
RUN pacman --noconfirm -Syu  
RUN pacman --noconfirm --needed -S arm-none-eabi-gcc arm-none-eabi-newlib make
cmake  
RUN pacman --noconfirm --needed -S arm-none-eabi-gdb cgdb  
RUN pacman --noconfirm --needed -S util-linux binutils  
RUN pacman --noconfirm --needed -S wget yaourt awk sudo file fakeroot  
  
RUN pacman -Scc --noconfirm && \  
sudo ln -sv /usr/bin/core_perl/pod2man /usr/sbin && \  
sed -i -e "s/Defaults requiretty.*/ #Defaults requiretty/g" /etc/sudoers && \  
echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
# Add user, group sudo; switch to user (for yaourt)  
RUN groupadd --system sudo && \  
useradd -m --groups sudo user  
USER user  
RUN yaourt --noconfirm -S jlink-software-and-documentation  
  
USER root  
RUN pacman --noconfirm -Rs wget yaourt sudo file fakeroot  
RUN pacman --noconfirm -Sc  
  
ADD tools/gen-jlink /usr/bin/  
ADD tools/gdb-client /usr/bin/  

