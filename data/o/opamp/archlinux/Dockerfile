## -*- docker-image-name: "opamp/archlinux" -*-  
FROM base/archlinux:latest  
MAINTAINER opamp_sando <opampg@gmail.com>  
  
RUN useradd -m -d /home/user -s /bin/bash -g users -G users,wheel user  
RUN pacman -Syu --noconfirm binutils fakeroot make patch git sudo > /dev/null
&&rm -f /etc/sudoers  
ADD sudoers /etc/sudoers  
RUN chown root:root /etc/sudoers && chmod 440 /etc/sudoers  
  
# Install yaourt  
ADD pacman.conf.patch /tmp/pacman.conf.patch  
RUN patch /etc/pacman.conf < /tmp/pacman.conf.patch && rm -f
/tmp/pacman.conf.patch  
RUN pacman -Syu yaourt --noconfirm > /dev/null  
  
ONBUILD RUN pacman -Syu --noconfirm > /dev/null  

