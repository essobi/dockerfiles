FROM debian:jessie  
  
# USER  
ENV SHELL /bin/zsh  
ENV TERM xterm-256color  
ENV USER user  
ENV HOME /home/$USER  
RUN \  
apt-get update &&\  
apt-get install -y \  
autoconf \  
automake \  
build-essential \  
cmake \  
curl \  
g++ \  
git \  
libssl-dev \  
libtool \  
libtool-bin \  
pkg-config \  
python-dev python-pip python3-dev python3-pip \  
stow \  
sudo \  
tmux \  
unzip \  
zsh \  
&&\  
git clone https://github.com/neovim/neovim &&\  
cd neovim &&\  
make CMAKE_BUILD_TYPE=Release &&\  
make install &&\  
cd .. &&\  
rm -rf ./neovim &&\  
pip3 install neovim &&\  
pip2 install neovim &&\  
apt-get autoremove -y && apt-get clean -y &&\  
rm -rf /var/lib/apit/lists &&\  
adduser --disabled-password --gecos '' \--shell $SHELL $USER &&\  
adduser $USER sudo &&\  
chown -R $USER:$USER $HOME &&\  
echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
WORKDIR $HOME  
USER $USER  
ENTRYPOINT ["zsh", "-c", "STOW_INSTALL=\"$HOME/.dotfiles/scripts/install.sh\";
[[ -f $STOW_INSTALL ]] && bash $STOW_INSTALL &>/dev/null; zsh -i"]  

