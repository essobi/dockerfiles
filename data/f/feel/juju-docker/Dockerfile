FROM base/archlinux  
MAINTAINER Filippo Squillace <feel.squally@gmail.com>  
  
ADD ./run.sh /run.sh  
  
RUN pacman --noconfirm -Sy && pacman -S pacman --noconfirm && pacman-db-
upgrade && \  
pacman -Syy --noconfirm && \  
pacman -S --noconfirm archlinux-keyring && \  
pacman-key --init && \  
pacman-key --populate archlinux && \  
pacman --noconfirm -S git arch-install-scripts base-devel libunistring && \  
useradd juju -m && \  
echo "juju ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && mkdir -p /run/shm  
  
USER juju  
  
RUN mkdir -p /tmp/package-query && cd /tmp/package-query && curl -J -O
https://aur.archlinux.org/packages/pa/package-query/PKGBUILD && makepkg -fsc
--noconfirm  
  
USER root  
  
RUN pacman --noconfirm -U /tmp/package-query/package-query-*.tar.xz && rm -rf
/tmp/package-query /var/cache/pacman/pkg/*  
  
USER juju  
VOLUME ["/tmp/juju-image"]  
WORKDIR /tmp/juju-image  
ENTRYPOINT ["sh", "-c", "/run.sh"]  

