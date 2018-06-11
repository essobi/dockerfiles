FROM zasdfgbnmsystem/basic  
  
# setup  
COPY yaourt custom_repo.conf startkde /  
  
USER root  
RUN cat custom_repo.conf >> /etc/pacman.conf  
RUN pacman -Sy --noconfirm archlinuxcn-keyring  
RUN pacman -Syu --noconfirm  
  
# install packages  
USER user  
RUN yaourt -Syua --noconfirm || true  
RUN for i in $(grep '^\w.*' /yaourt); do yaourt -S --noconfirm $i || true;
done && sudo rm /boot/*.img  
  
USER root  
  
# setting up services  
RUN systemctl enable sddm NetworkManager  
  
# setting up mkinitcpio  
RUN sed -i 's/basic/archlinux-kde/g' /etc/docker-btrfs.json  
  
USER user  
CMD [ "dbus-launch", "--exit-with-session", "/startkde" ]

