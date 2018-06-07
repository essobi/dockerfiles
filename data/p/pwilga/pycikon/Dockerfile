FROM ubuntu:18.04  
MAINTAINER Piotr Wilga <pwilga@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV PYTHONUNBUFFERED 1  
RUN apt-get update && apt-get install -y \  
curl \  
exuberant-ctags \  
git \  
locales \  
python \  
python-pip \  
python3 \  
python3-pip \  
tmux \  
vim \  
wget  
  
ENV LANG en_US.UTF-8  
RUN locale-gen en_US.UTF-8  
  
WORKDIR /root  
RUN git clone https://bitbucket.org/pwilga/dotfiles  
RUN dotfiles/.make.sh  
RUN vim -E -u NONE -S /root/.vimrc +qall  
  

