FROM ubuntu:latest  
MAINTAINER Spencer Tsai <spencer.tsai@gmail.com>  
  
# environment variables  
ENV DEBIAN_FRONTEND noninteractive  
  
#ADD fs/ /  
COPY fs/home/dev/* /home/spencer/  
COPY fs/home/dev/* /root/  
  
# install pagkages  
RUN apt-get update && \  
apt-get install -y ncurses-dev libtolua-dev exuberant-ctags \  
python python-dev ruby ruby-dev \  
mercurial cscope git make bash-completion wget fontconfig && \  
cd /tmp && \  
# build and install vim  
hg clone https://code.google.com/p/vim/ && \  
cd vim && \  
./configure --with-features=huge --enable-luainterp \  
\--enable-gui=no \--without-x \--enable-cscope \  
\--enable-rubyinterp --enable-pythoninterp \  
\--enable-perlinterp \  
\--prefix=/usr && \  
make VIMRUNTIMEDIR=/usr/share/vim/vim74 && \  
make install && \  
# add dev user  
adduser spencer --disabled-password --gecos "" && \  
echo "ALL ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
cp /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && \  
dpkg-reconfigure locales && \  
locale-gen en_US.UTF-8 && \  
/usr/sbin/update-locale LANG=en_US.UTF-8 && \  
chown -R spencer:spencer /home/spencer && \  
# cleanup  
apt-get remove -y ncurses-dev && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /home/spencer  
ENV HOME=/home/spencer \  
USER=spencer  
ENV LC_ALL en_US.UTF-8  
USER spencer  
  
# install vim plugins  
RUN mkdir -p ~/.vim/bundle && \  
cd ~/.vim/bundle && \  
git clone --depth 1 https://github.com/gmarik/Vundle.vim.git && \  
vim +PluginInstall +qall && \  
# cleanup  
rm -rf Vundle.vim/.git  
  
# Powerline fonts  
RUN mkdir -p $HOME/.fonts $HOME/.config/fontconfig/conf.d && \  
wget -P $HOME/.fonts
https://github.com/Lokaltog/powerline/raw/develop/font/PowerlineSymbols.otf &&
\  
wget -P $HOME/.config/fontconfig/conf.d/
https://github.com/Lokaltog/powerline/raw/develop/font/10-powerline-
symbols.conf && \  
fc-cache -vf $HOME/.fonts/ && \  
echo "set guifont=Droid\\\ Sans\\\ Mono\\\ 10"  
  
CMD vim  

