FROM phusion/baseimage:0.9.19  
RUN apt-get update && DEBIAN_FRONTENT=noninteractive apt-get install -y zsh
git curl grc ccze vim iputils-ping mc httpie  
  
RUN chsh -s /bin/zsh  
  
RUN git clone \--recursive https://github.com/decebal/dotfiles ~/.dotfiles  
  
WORKDIR ~/.dotfiles  
  
RUN ~/.dotfiles/non-interactive-install.sh

