FROM nitrousio/ubuntu-bare:latest  
MAINTAINER Nitrous.IO <hello@nitrous.io>  
  
# Install essential tools  
RUN \  
apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get install -yy \--no-install-recommends build-essential checkinstall
cmake gdb curl wget screen tmux zsh silversearcher-ag ack-grep gnupg bzip2 zip
unzip unison man-db sqlite3 bison gawk telnet psmisc vim-nox emacs24-nox nano
git git-svn mercurial bzr subversion libssl-dev libyaml-dev libreadline6-dev
zlib1g-dev libxml2-dev libxslt1-dev libbz2-dev libncurses5-dev
libncursesw5-dev libsqlite3-dev libffi-dev && \  
apt-get clean  
  
COPY files/gitconfig /home/$NITROUS_USERNAME/.gitconfig  
COPY files/tmux.conf /home/$NITROUS_USERNAME/.tmux.conf  
COPY files/vimrc /home/$NITROUS_USERNAME/.vimrc  
  
RUN \  
/bin/bash -c 'chown -R $NITROUS_USERNAME:$NITROUS_USERNAME
/home/$NITROUS_USERNAME/.gitconfig /home/$NITROUS_USERNAME/.tmux.conf
/home/$NITROUS_USERNAME/.vimrc'  
  
USER $NITROUS_USERNAME  
  
# hushlogin  
RUN \  
/bin/bash -c 'touch /home/$NITROUS_USERNAME/.hushlogin'  
  
# Install oh-my-zsh  
RUN \  
/bin/bash -c 'git clone https://github.com/robbyrussell/oh-my-zsh.git
/home/$NITROUS_USERNAME/.oh-my-zsh && \  
cp /home/$NITROUS_USERNAME/.oh-my-zsh/templates/zshrc.zsh-template
/home/$NITROUS_USERNAME/.zshrc && \  
sed -i "s|# DISABLE_AUTO_UPDATE|DISABLE_AUTO_UPDATE|g"
/home/$NITROUS_USERNAME/.zshrc && \  
sudo chsh -s /bin/zsh $NITROUS_USERNAME'  
  
# setup vim  
RUN \  
/bin/bash -c 'git clone \--branch v0.10.2 \--depth 1
https://github.com/gmarik/Vundle.vim.git
/home/$NITROUS_USERNAME/.vim/bundle/Vundle.vim && \  
vim -i NONE -c PluginInstall -c quitall > /dev/null'  
  
USER root  

