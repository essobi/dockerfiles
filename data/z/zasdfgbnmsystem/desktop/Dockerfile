FROM zasdfgbnmsystem/archlinux-kde  
  
# install packages  
USER root  
COPY yaourt pacman /  
COPY dockersh /usr/bin/  
RUN pacman -Syu --noconfirm && pacman -S --noconfirm $(grep '^\w.*' /pacman)  
USER user  
RUN yaourt -Syua --noconfirm || true  
RUN for i in $(grep '^\w.*' /yaourt); do yaourt -S --noconfirm $i || true;
done  
USER root  
  
# setting up mkinitcpio  
RUN sed -i 's/archlinux-kde/desktop/g' /etc/docker-btrfs.json  
  
# setting up services  
RUN systemctl enable docker netdata  

