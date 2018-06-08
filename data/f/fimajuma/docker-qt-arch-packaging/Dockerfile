FROM base/archlinux  
MAINTAINER Marco Cyriacks <marco@cyriacks.net>  
  
  
# Install missing packages  
RUN pacman --noconfirm -Syyu \  
git \  
openssh \  
htop \  
vim \  
sudo \  
tree \  
bash-completion \  
base-devel  
  
RUN pacman --noconfirm -Syyu \  
qt5-base \  
qt5-tools  
  
RUN pacman --noconfirm -Syyu \  
qt5-svg \  
qt5-webkit  
  
# Set correct timezone  
ENV TZ=Europe/Berlin  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# Add build user and build/install discount lib  
RUN useradd -s /bin/bash -u 2000 build  
USER build  
RUN git clone https://aur.archlinux.org/discount.git /tmp/discount  
RUN cd /tmp/discount && git checkout 73cfe6e0529981d75c21fbdd23ae5489f747aa68
&& makepkg  
USER root  
RUN pacman --noconfirm -U /tmp/discount/*.pkg.tar.xz  
  

