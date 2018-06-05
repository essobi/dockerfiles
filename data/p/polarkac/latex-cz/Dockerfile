FROM base/archlinux:latest  
  
MAINTAINER Lukáš Pohlreich <pohlreichlukas@gmail.com>  
  
RUN pacman-key --refresh-keys && \  
pacman -Syu --noconfirm \  
mesa-libgl \  
texlive-most && \  
pacman-db-upgrade && \  
pacman -Scc --noconfirm  
  
ADD ./vlna /usr/sbin/vlna  

