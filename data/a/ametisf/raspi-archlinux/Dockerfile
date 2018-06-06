FROM ametisf/archlinux-devel  
  
RUN useradd normaluser && \  
git clone https://aur.archlinux.org/qemu-user-static.git && \  
cd qemu-user-static && chmod 777 . && \  
su -c 'makepkg -sr --noconfirm' normaluser && \  
pacman -U *.pkg.* --noconfirm && \  
cd .. && rm -rf qemu-user-static && \  
git clone https://aur.archlinux.org/binfmt-qemu-static.git && \  
cd binfmt-qemu-static && chmod 777 . && \  
su -c 'makepkg -sr --noconfirm' normaluser && \  
pacman -U *.pkg.* --noconfirm && \  
cd .. && rm -rf binfmt-qemu-static && \  
rm -rf /var/cache/pacman/pkg/*  
  
# get raspberry pi system  
ADD http://de6.mirror.archlinuxarm.org/os/ArchLinuxARM-rpi-2-latest.tar.gz
/latest.tar.gz  
RUN mkdir /chroot && (cd chroot && tar xpf /latest.tar.gz) && rm -rf
/latest.tar.gz  
  
# compile wrapper for qemu and copy both to chroot  
ADD ./qemu-arm-wrapper-rpi2.c /  
RUN gcc -static qemu-arm-wrapper-rpi2.c -s -o /usr/bin/qemu-arm-wrapper && \  
cp -v /usr/bin/qemu-arm-{static,wrapper} /chroot/usr/bin/ && \  
rm /qemu-arm-wrapper-rpi2.c  
  
# enter chroot  
ENTRYPOINT chroot /chroot /bin/env -i HOME=/root TERM="$TERM" PS1='\u:\w\$ '
PATH="/usr/bin" /usr/bin/bash --login  

