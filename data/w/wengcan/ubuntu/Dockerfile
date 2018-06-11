# Ubuntu Dockerfile  
#  
# https://github.com/dockerfile/ubuntu  
#  
# Pull base image.  
FROM ubuntu:14.04  
# Install.  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential autoconf libtool libssl-dev && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu zsh curl git htop man unzip vim wget python python-
dev python-pip python-virtualenv && \  
rm -rf /var/lib/apt/lists/*  
  
# Add files.  
ADD root/.bashrc /root/.bashrc  
ADD root/.gitconfig /root/.gitconfig  
ADD root/.scripts /root/.scripts  
  
RUN git clone git://github.com/bwithem/oh-my-zsh.git /root/.oh-my-zsh \  
&& cp /root/.oh-my-zsh/templates/zshrc.zsh-template /root/.zshrc \  
&& chsh -s /bin/zsh  
  
# Set environment variables.  
ENV HOME /root  
  
# Define working directory.  
WORKDIR /root  
  
# Define default command.  
CMD ["zsh"]  

