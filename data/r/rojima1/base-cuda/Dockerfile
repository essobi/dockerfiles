FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04  
RUN apt-get update && \  
apt-get install -y \  
emacs \  
emacs-mozc \  
expect \  
fonts-vlgothic \  
sudo \  
unzip \  
wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN groupadd --gid 1000 developer && \  
useradd --uid 1000 --gid 1000 --groups sudo --create-home --shell /bin/bash
developer && \  
echo 'developer:P@ssw0rd' | chpasswd  
  
COPY init.el /home/developer/.emacs.d/init.el  
COPY install-packages.el /home/developer  
  
RUN chown --recursive developer:developer /home/developer  
  
USER developer  
WORKDIR /home/developer  
  
RUN emacs --script install-packages.el && rm install-packages.el  

