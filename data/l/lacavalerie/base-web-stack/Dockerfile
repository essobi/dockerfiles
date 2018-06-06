# CAVALERIE WEB BASE  
#  
# Cavalerie base image for web stack  
FROM debian:wheezy  
MAINTAINER Arnaud Lenglet <arnaud@agencecavalerie.com>  
  
# ------------ BASE PACKAGES INSTALLATION ------------  
RUN apt-get update && apt-get install -y \  
zsh  
  
RUN apt-get install -y \  
git \  
curl \  
vim \  
ruby \  
php5-mysql \  
nfs-common \  
mysql-client \  
git-flow \  
php5-curl \  
net-tools  
  
# ------------ OH-MY-ZSH INSTALLATION ------------  
WORKDIR /  
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh && \  
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc && \  
chsh -s /bin/zsh

