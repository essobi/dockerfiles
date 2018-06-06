# use the ubuntu 16.04 base image  
FROM ppc64le/ubuntu:16.04  
MAINTAINER Lei YU mine260309@gmail.com  
  
# Replace sources.list with mirror in China  
COPY apt-source-cn-16.04.list /etc/apt/sources.list  
  
# Update package repository  
RUN apt-get update  
  
# Install g++, git, zlib, etc  
RUN apt-get install -y build-essential g++ zlib1g-dev libbz2-dev  
RUN apt-get install -y git vim tmux  
RUN apt-get install -y aptitude bash-completion dos2unix ftp gcc-multilib-
powerpc-linux-gnu \  
gdb ghex gitk libboost-all-dev libc6-dbg meld python \  
quilt wget zip ctags  
  
# Add user `mine`, change to your favorite name  
RUN useradd -ms /bin/bash mine && echo "mine:mine" | chpasswd && adduser mine
sudo  
RUN mkdir -p /home/mine && chown -R mine:mine /home/mine  
USER mine  
WORKDIR /home/mine  
RUN git clone git://github.com/andsens/homeshick.git
/home/mine/.homesick/repos/homeshick  
RUN /bin/bash -c 'source /home/mine/.homesick/repos/homeshick/homeshick.sh &&
homeshick clone -b mine260309/dotfiles && homeshick link -f -b dotfiles'  
RUN git clone https://github.com/VundleVim/Vundle.vim.git
/home/mine/.vim/bundle/Vundle.vim && vim +PluginInstall +qall  
CMD /bin/bash  

