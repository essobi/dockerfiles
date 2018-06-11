#  
# Arch Linux + Yaourt  
#  
# https://github.com/bmcustodio/docker-archlinux-yaourt  
#  
FROM bmcustodio/archlinux  
MAINTAINER Bruno M. Custódio <bruno@brunomcustodio.com>  
  
RUN pacman --noconfirm -Syyu  
RUN pacman --noconfirm -S base-devel  
RUN pacman --noconfirm -S yajl  
  
RUN groupadd -r yaourt  
RUN useradd -r -g yaourt yaourt  
RUN mkdir /tmp/yaourt  
RUN chown -R yaourt:yaourt /tmp/yaourt  
  
USER yaourt  
  
WORKDIR /tmp/yaourt  
RUN curl https://aur.archlinux.org/packages/pa/package-query/package-
query.tar.gz | tar zx  
WORKDIR /tmp/yaourt/package-query  
RUN makepkg --noconfirm  
  
USER root  
  
WORKDIR /tmp/yaourt/package-query  
RUN pacman --noconfirm -U *.tar.xz  
  
USER yaourt  
  
WORKDIR /tmp/yaourt  
RUN curl https://aur.archlinux.org/packages/ya/yaourt/yaourt.tar.gz | tar zx  
WORKDIR /tmp/yaourt/yaourt  
RUN makepkg --noconfirm  
  
USER root  
  
WORKDIR /tmp/yaourt/yaourt  
RUN pacman --noconfirm -U *.tar.xz  

