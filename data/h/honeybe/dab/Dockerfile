FROM archimg/base-devel  
  
MAINTAINER 윤병익 <by_yeun@daum.net>  
  
RUN curl -o /etc/pacman.d/mirrorlist
"https://www.archlinux.org/mirrorlist/?country=all&protocol=https&ip_version=6&use_mirror_status=on"
&& sed -i 's/^#//' /etc/pacman.d/mirrorlist  
  
RUN pacman-key \--refresh-keys && \  
pacman \--sync \--refresh \--noconfirm \--noprogressbar \--quiet && \  
pacman \--sync \--noconfirm \--noprogressbar \--quiet archlinux-keyring
openssl pacman && \  
pacman-db-upgrade && \  
pacman \--sync \--sysupgrade \--noconfirm \--noprogressbar \--quiet && \  
pacman \--sync \--noconfirm \--noprogressbar \--quiet base-devel git namcap
pkgbuild-introspection gd  
  
RUN useradd \--create-home \--comment "Arch Build User" build  
ENV HOME /home/build  
  
RUN mkdir /package  
RUN chown build /package  
WORKDIR /package  
  
USER build  
  
CMD ["makepkg", "--force"]  

