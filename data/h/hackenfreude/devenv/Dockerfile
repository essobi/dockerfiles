FROM debian:stretch-20171009  
#### packages ####  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get --assume-yes
upgrade  
RUN apt-get --assume-yes install \  
build-essential \  
cmake \  
curl \  
ctags \  
git \  
make \  
pkg-config \  
procps \  
python-dev \  
python3-dev \  
python-pip \  
jq \  
screen \  
tree \  
vim-gnome \  
wget \  
zsh  
  
RUN pip install \  
yamllint  
  
##### zsh #####  
RUN chsh -s /bin/zsh  
ENV SHELL /bin/zsh  
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git /root/.oh-my-zsh  
ADD https://raw.githubusercontent.com/hackenfreude/dotfiles/master/zshrc
/root/.zshrc  
RUN chmod 0664 /root/.zshrc  
  
##### screen #####  
ADD https://raw.githubusercontent.com/hackenfreude/dotfiles/master/screenrc
/root/.screenrc  
RUN chmod 0664 /root/.screenrc  
  
##### git #####  
ADD https://raw.githubusercontent.com/hackenfreude/dotfiles/master/gitconfig
/root/.gitconfig  
RUN chmod 0664 /root/.gitconfig  
  
##### vim #####  
ADD https://raw.githubusercontent.com/hackenfreude/dotfiles/master/vimrc
/root/.vimrc  
RUN chmod 0664 /root/.vimrc  
ADD https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
/root/.vim/autoload/plug.vim  
RUN chmod 0664 /root/.vim/autoload/plug.vim  
RUN vim -c "PlugInstall" -c "qa"  
  
##### youcompleteme #####  
RUN mkdir /root/ycm_build  
RUN cd /root/ycm_build && cmake -G "Unix Makefiles" .
/root/.vim/plugged/YouCompleteMe/third_party/ycmd/cpp  
RUN cd /root/ycm_build && cmake --build . --target ycm_core  
RUN rm --recursive /root/ycm_build  
  
CMD ["/bin/zsh"]  

