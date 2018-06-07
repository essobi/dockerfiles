FROM base/archlinux:latest  
  
MAINTAINER escalade  
  
# Set working directory to /root  
WORKDIR /root  
  
# Add archlinuxcn repository  
RUN echo -e " \n\  
[archlinuxcn] \n\  
SigLevel = Optional TrustedOnly \n\  
Server = https://cdn.repo.archlinuxcn.org/\$arch \n\  
" >> /etc/pacman.conf  
  
# Add multilib repository  
RUN echo -e " \n\  
[multilib] \n\  
Include = /etc/pacman.d/mirrorlist \n\  
" >> /etc/pacman.conf  
  
# Set locale  
RUN sed -i -e "s/#en_US\\.UTF-8/en_US\\.UTF-8/" /etc/locale.gen  
RUN echo -e "LANG=en_US.UTF-8" > /etc/locale.conf  
RUN locale-gen  
  
# Update system and install apps  
RUN pacman -Sy --noconfirm archlinux-keyring && pacman -Su --noconfirm &&
pacman-db-upgrade && update-ca-trust && pacman -S --noconfirm archlinuxcn-
keyring vim  
  
# Set VIM as default editor  
RUN echo >> /etc/bash.bashrc  
RUN echo export VISUAL=vim >> /etc/bash.bashrc  
  
# Remove downloaded packages  
RUN yes | pacman -Scc  
  
# Set default command  
CMD ["bash","-l"]  

