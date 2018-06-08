FROM ubuntu:16.04  
MAINTAINER rubenrua  
  
# Install packages: wget, git and emacs  
RUN apt-get update && \  
apt-get install -y curl git emacs-nox build-essential && \  
apt-get clean  
  
# Create a workspace directory  
RUN mkdir -p /workspace  
  
ADD https://raw.githubusercontent.com/rubenrua/dotfiles/master/.gitconfig
/root/.gitconfig  
ADD https://raw.githubusercontent.com/rubenrua/dotfiles/master/.bashrc
/root/.bashrc  
ADD
https://raw.githubusercontent.com/rubenrua/dotfiles/master/.emacs.d/init.el
/root/.emacs.d/init.el  
  
ENV EDITOR emacs  
  
ENTRYPOINT bash  

