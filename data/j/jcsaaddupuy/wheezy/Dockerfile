FROM debian:wheezy  
MAINTAINER Jc Saad-Dupuy "jc.saaddupuy@fsfe.org"  
# install base packages  
RUN apt-get update -qq && apt-get upgrade -y  
RUN apt-get install -y wget git tmux vim-nox zsh  
RUN apt-get install -y make  
RUN apt-get install -y nmap  
RUN git clone https://github.com/jcsaaddupuy/dotfiles.git  
RUN cd dotfiles && git submodule init && git submodule update  
RUN cd dotfiles && make install  
  

