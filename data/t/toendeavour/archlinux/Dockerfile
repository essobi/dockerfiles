FROM toendeavour/archlinux:arm  
  
RUN [ "cross-build-start" ]  
RUN pacman --needed --noconfirm -Syu base base-devel && \  
rm -Rf "/var/cache" && \  
rm -Rf "/var/lib/pacman/sync" && \  
rm -Rf "/var/log/*" && \  
install -m 0755 -d "/var/cache/pacman/pkg"  
RUN [ "cross-build-end" ]  

