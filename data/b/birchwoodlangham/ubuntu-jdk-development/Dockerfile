FROM birchwoodlangham/ubuntu-jdk:latest  
  
MAINTAINER Tan Quach <tan.quach@birchwoodlangham.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# install zsh, python pip etc.  
RUN apt-get update && \  
apt-get install -y python-pip python-dev powerline && \  
apt-get clean && rm -rf /var/lib/apt/lists/* && \  
pip install --upgrade pip && \  
pip install psutil thefuck sexpdata websocket-client && \  
useradd -d /home/user -m -U user  
  
USER user  
WORKDIR /home/user  
  
# Use this one to install the plugins etc.  
COPY vimrc_plugins /home/user/.vimrc  
  
# Now for vim plugins, the powerline fonts and nerd fonts required for
powerline  
RUN git clone https://github.com/powerline/fonts.git && \  
fonts/install.sh && \  
rm -rf fonts && \  
git clone \--depth 1 https://github.com/ryanoasis/nerd-fonts.git fonts && \  
cd /home/user/fonts && \  
./install.sh -q --copy --complete && \  
cd /home/user && \  
rm -rf fonts && \  
mkdir -p /home/user/.vim && \  
git clone https://github.com/VundleVim/Vundle.vim.git
/home/user/.vim/bundle/Vundle.vim && \  
vim +PluginInstall +qall  
  
# copy configuration files for vim, zsh and tmux  
COPY vimrc /home/user/.vimrc  
  
VOLUME ["/home/user/code", "/home/user/.m2", "/home/user/.ivy2"]  
  
ENV JAVA_HOME=/usr/lib/jvm/java-8-oracle  
ENV DERBY_HOME=/usr/lib/jvm/java-8-oracle/db  
  
CMD ["/bin/bash"]  

