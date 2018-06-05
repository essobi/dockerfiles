FROM zasdfgbnm/archlinux-yaourt  
  
# setup  
USER root  
COPY yaourt pacman /  
COPY zshrc /etc/zsh/  
COPY locale.gen /etc/locale.gen  
  
# RUN /select-mirrors.sh  
RUN pacman -Syu --noconfirm  
RUN pacman -S --noconfirm man-db man-pages  
RUN pacman -S --noconfirm base  
RUN locale-gen  
RUN pacman -S --noconfirm $(grep '^\w.*' /pacman)  
  
# install packages  
USER user  
RUN yaourt -Syua --noconfirm || true  
RUN for i in $(grep '^\w.*' /yaourt); do yaourt -S --noconfirm $i || true;
done  
  
USER root  
  
# setting up services  
RUN systemctl enable sshd  
  
# setting up sshd  
RUN sed -i 's/.*PasswordAuthentication .*/PasswordAuthentication no/g'
/etc/ssh/sshd_config  
  
# setting up mkinitcpio  
RUN sed -i 's/archlinux\/base/zasdfgbnmsystem\/basic/g' /etc/docker-btrfs.json  
RUN perl -i -p -e 's/(?<=^HOOKS=\\()(.*)(?=\\))/$1 docker-btrfs/g'
/etc/mkinitcpio.conf  
  
# copy gen_boot  
COPY gen_boot /usr/bin  

