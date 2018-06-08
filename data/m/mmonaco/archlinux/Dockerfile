FROM base/archlinux  
MAINTAINER Matthew Monaco <matt@monaco.cx>  
ENV LANG=en_US.UTF-8  
ENV TERM=xterm  
  
RUN pacman --noconfirm -Sy \  
&& pacman --noconfirm -S pacman archlinux-keyring \  
&& pacman-db-upgrade \  
&& pacman --noconfirm -Suu \  
&& yes | pacman -Scc  
  
RUN pacman --noconfirm --needed -S \  
base-devel \  
bash-completion \  
curl \  
git \  
iproute2 \  
man \  
net-tools \  
rsync \  
tree \  
vim-minimal \  
wget \  
&& yes | pacman -Scc  
  
ADD bashrc /root/.bashrc  
WORKDIR /root  
  
CMD [ "/bin/bash" ]  

