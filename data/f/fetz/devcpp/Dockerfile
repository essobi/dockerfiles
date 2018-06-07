FROM ubuntu:15.04  
  
ENV BUILD_PKGS curl nmap cmake clang clang-format-3.6 python-dev npm
libc++-dev build-essential qemu-system-x86 git vim ctags libncurses5-dev
libclang-dev netcat pv tmux sudo geany geany-plugin-addons geany-plugin-
autoclose geany-plugin-codenav geany-plugin-defineformat geany-plugin-debugger
gcc-multilib bash-completion  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
RUN \  
apt-get update && \  
apt-get install -y $BUILD_PKGS && \  
locale-gen en_US.UTF-8 && \  
mkdir -p ~/.vim/autoload && \  
curl -fLo ~/.vim/autoload/plug.vim
https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim && \  
curl -fLo ~/.vimrc https://bitbucket.org/ameruntz/devcpp/raw/master/vimrc && \  
curl -fLo ~/.ycm_extra_conf.py
https://bitbucket.org/ameruntz/devcpp/raw/master/ycm_extra_conf.py && \  
curl -fLo ~/.tmux.conf
https://bitbucket.org/ameruntz/devcpp/raw/master/tmux.conf && \  
vim +PlugInstall +qall && \  
cd ~/.vim/plugged/YouCompleteMe/ && \  
./install.py \--clang-completer --system-libclang && \  
mkdir -p /opt/vim_files/ && \  
mv ~/.vim ~/.vimrc ~/.ycm_extra_conf.py ~/.tmux.conf /opt/vim_files/ && \  
chmod -R 755 /opt/vim_files/ && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

