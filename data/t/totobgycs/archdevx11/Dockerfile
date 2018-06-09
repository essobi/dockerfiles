FROM totobgycs/archdev  
MAINTAINER totobgycs  
  
ENV TERM xterm  
USER build  
WORKDIR /home/build  
RUN yaourt -Syy ; \  
yaourt -S --noconfirm xorg-server-common xorg-xhost\  
ttf-ubuntu-font-family ttf-freefont freetype2 \  
mesa-libgl ; \  
yes | yaourt -Scc  
  
USER root  
RUN useradd -m guiuser ; \  
echo 'guiuser ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers  
  

