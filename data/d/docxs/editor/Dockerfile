########################################################################  
# Dockerfile for editing  
#  
# ## .  
# ## ## ## ==  
# ## ## ## ## ===  
# /""""""""""""""""\\___/ ===  
# ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ / ===- ~~~  
# \\______ o __/  
# \ \ __/  
# \\____\\______/  
#  
# Author: pjan vandaele <pjan@pjan.io>  
# Scm url: https://github.com/docxs/editor  
# License: MIT  
########################################################################  
  
# pull base image  
FROM docxs/base:latest  
  
# maintainer details  
MAINTAINER pjan vandaele "pjan@pjan.io"  
  
# Set environment variables  
ENV TERM xterm-256color  
  
# add a post-invoke hook to dpkg which deletes cached deb files  
# update the sources.list  
# update/dist-upgrade  
# clear the caches  
RUN \  
apt-prepare && \  
apt-get install -q -y \  
vim-nox \  
git \  
python \  
python-pip \  
fontconfig \  
ack-grep \  
exuberant-ctags \  
tmux \  
curl \  
wget \  
tree \  
findutils \  
sed && \  
apt-cleanup  
  
# setup dotfiles  
RUN \  
git clone https://github.com/pjan/ubuntu-dotfiles.git && \  
cd ubuntu-dotfiles && \  
chmod +x bootstrap.sh && ./bootstrap.sh --force && cd .. && \  
rm -r ubuntu-dotfiles  
  
# configure powerline  
COPY ./config/etc_fonts_conf.d_10-powerline-symbols.conf
/etc/fonts/conf.d/10-powerline-symbols.conf  
COPY ./config/fonts /usr/share/fonts  
RUN fc-cache -vf  
  
# configure vim  
RUN \  
git clone https://github.com/pjan/vim-config.git && \  
cd vim-config && \  
chmod +x bootstrap.sh && ./bootstrap.sh --force && cd .. && \  
rm -r vim-config  
  
ENTRYPOINT \  
["/bin/bash","--login"]  

