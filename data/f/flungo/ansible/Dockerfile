FROM base/archlinux  
  
# Install ansible  
RUN pacman -Syyu --noconfirm python ansible  
  
# Add a basic hosts file  
COPY hosts /etc/ansible/hosts  

