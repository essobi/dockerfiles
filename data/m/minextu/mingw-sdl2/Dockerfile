FROM base/archlinux:latest  
MAINTAINER minextu  
  
  
# add mingw repo  
RUN echo -e '[mingw-w64]\nSigLevel = PackageOptional\nServer =
http://downloads.sourceforge.net/project/mingw-w64-archlinux/$arch' >>
/etc/pacman.conf  
  
# update system  
RUN pacman --noconfirm -Syyu  
  
# install build tools  
RUN pacman --noconfirm --needed -Sy \  
base-devel \  
cmake \  
git \  
openssh && \  
find /var/cache/pacman/pkg -mindepth 1 -delete  
  
# install sdl  
RUN pacman --noconfirm -Sy \  
sdl2 \  
sdl2_image \  
sdl2_ttf && \  
find /var/cache/pacman/pkg -mindepth 1 -delete  
  
# install mingw  
RUN pacman --noconfirm -Sy \  
mingw-w64-gcc \  
mingw-w64-sdl2 \  
mingw-w64-sdl2_image \  
mingw-w64-sdl2_ttf && \  
find /var/cache/pacman/pkg -mindepth 1 -delete  
  
CMD /bin/bash  

