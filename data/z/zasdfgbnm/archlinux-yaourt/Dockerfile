FROM heichblatt/archlinux-yaourt  
USER root  
RUN echo 'ALL ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
COPY remove-pkg-cache.hook /etc/pacman.d/hooks/  
RUN curl -s
"https://www.archlinux.org/mirrorlist/?country=CN&country=US&protocol=https&use_mirror_status=on"
| sed -e 's/^#Server/Server/' -e '/^#/d' | rankmirrors -n 5 - >
/etc/pacman.d/mirrorlist  
  
USER user  
# a system upgrade might break package-query binaries, so always rebuild it
after upgrading  
RUN sudo mkdir -p /package-query && sudo chown user:user /package-query && cd
/package-query && yaourt -G package-query && yaourt -Syua --noconfirm && cd
package-query && makepkg -i --noconfirm && cd / && sudo rm -rf /package-query  
RUN yaourt -Syua --noconfirm  

