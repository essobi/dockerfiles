############################################################  
# Dockerfile file to build Ubuntu container images  
# AUTHOR: Axel Quack <mail@axelquack.de>  
# Version 0.1  
############################################################  
  
# Pull base image.  
FROM ubuntu:16.04  
MAINTAINER Axel Quack <mail@axelquack.de>  
  
# Install.packages  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip vim wget zsh && \  
rm -rf /var/lib/apt/lists/*  
  
# Install oh-my-zsh and define zsh as default shell  
# change default shell  
RUN \  
git clone git://github.com/robbyrussell/oh-my-zsh.git /root/.oh-my-zsh && \  
chsh -s /usr/bin/zsh  
  
# Add files.  
ADD root/.bashrc $HOME/.bashrc  
ADD root/.gitconfig $HOME/.gitconfig  
ADD root/.scripts $HOME/.scripts  
ADD root/.zshrc $HOME/.zshrc  
ADD root/.wgetrc $HOME/.wgetrc  
ADD root/.htoprc $HOME/.htoprc  
  
# Set environment variables.  
ENV HOME $HOME  
  
# Define working directory.  
WORKDIR $HOME  
  
# Define default command.  
CMD ["zsh"]  

