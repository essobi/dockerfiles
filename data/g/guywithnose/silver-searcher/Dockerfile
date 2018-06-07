FROM nubs/arch-build  
  
# Fix permissions on /home/build because of a bug in the docker hub.  
USER root  
RUN chown build:build /home/build  
WORKDIR /home/build  
  
# Build package from PKGBUILD  
USER build  
RUN curl -sS https://aur.archlinux.org/packages/si/silver-searcher-git/silver-
searcher-git.tar.gz | tar -xz  
RUN cd silver-searcher-git && makepkg --clean --noconfirm --noprogressbar  
  
# Install package  
USER root  
RUN pacman --upgrade --noconfirm --noprogressbar silver-searcher-git/silver-
searcher-git*.pkg.tar.xz  
  
USER build  
  
WORKDIR /workdir  

