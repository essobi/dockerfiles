FROM masm/archlinux-base  
MAINTAINER Marco Monteiro <marco@neniu.org>  
  
RUN pacman-key \--populate archlinux && \  
dirmngr </dev/null && \  
pacman-key \--refresh-keys && \  
echo -e '\n[masm]\nSigLevel = Optional TrustAll\nServer = http://pacman-
repo.neniu.org/$arch' >> /etc/pacman.conf && \  
pacman -Sqy pacman \--needed \--noconfirm \--noprogressbar && \  
pacman-db-upgrade && \  
pacman -Sqyyu \--noconfirm \--noprogressbar && \  
yes | pacman -Sqcc && \  
rm -rf /usr/share/man/* && \  
useradd \--create-home \--gid users \--password x \--uid 500 arch  
  
ONBUILD RUN pacman -Sqy pacman \--needed \--noconfirm \--noprogressbar && \  
pacman-db-upgrade && \  
pacman -Sqyyu \--noconfirm \--noprogressbar && \  
yes | pacman -Sqcc && \  
rm -rf /usr/share/man/*  

