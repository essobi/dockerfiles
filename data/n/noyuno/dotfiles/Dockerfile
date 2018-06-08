FROM base/archlinux  
  
ARG DRYRUN=${DRYRUN}  
ARG QUIET=${QUIET}  
run pacman -Syu --noconfirm && \  
pacman --noconfirm -S base base-devel && \  
groupadd sudo && \  
echo '%sudo ALL=(ALL:ALL) ALL' >> /etc/sudoers && \  
useradd tu -d /home/tu -p '' -s /bin/bash && \  
usermod -aG sudo tu && \  
mkdir -p /home/tu && \  
chown -R tu:tu /home/tu  
ADD . /home/tu/dotfiles  
USER tu  
WORKDIR /home/tu  
RUN sudo chown -R tu:tu /home/tu/dotfiles && \  
sudo sync && \  
./dotfiles/arch/bin/dflocal all  
  

