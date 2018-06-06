#FROM ubuntu:14.04  
FROM debian:jessie  
  
MAINTAINER David Hu <chin33z@gmail.com>  
  
RUN \  
apt-get update && \  
apt-get install -y git man wget cscope exuberant-ctags silversearcher-ag\  
screen openssh-server xz-utils unzip locate psmisc lsof ncdu vnstat htop
ipcalc nethogs tree figlet \  
make automake gcc build-essential python-dev libncurses5-dev ruby ruby-dev \  
bison gawk pax-utils bc &&\  
rm -rf /var/lib/apt/lists/* &&\  
apt-get clean -yq  
  
RUN \  
mkdir /var/run/sshd &&\  
echo 'root:root5023' | chpasswd &&\  
sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config &&\  
sed -i '/AcceptEnv/d' /etc/ssh/sshd_config &&\  
sed -i 's/Port 22/Port 5023/' /etc/ssh/sshd_config  
EXPOSE 5023  
CMD ["/usr/sbin/sshd", "-D"]  
  
ENV HOME /root  
  
WORKDIR /root  
  
# compile the customized vim with cscope/ruby/python support  
RUN \  
cd ~ &&\  
git clone https://github.com/vim/vim.git vim-source &&\  
cd vim-source &&\  
./configure --with-features=huge \  
\--enable-multibyte \  
\--enable-pythoninterp \  
\--with-python-config-dir=/usr/lib/python2.7/config-x86_64-linux-gnu \  
\--enable-cscope \  
\--enable-rubyinterp &&\  
make &&\  
make install &&\  
cd ~ &&\  
rm -fr vim-source  
  
  
# 1. git clone the vim setting  
# 2. git clone the env setting  
RUN \  
rm -fr ~/.vim ~/.vimrc &&\  
cd ~ && git clone https://github.com/chin33z/dotvim.git ~/.vim &&\  
cd ~/.vim/bundle/command-t/ruby/command-t && ruby extconf.rb && make &&\  
ln -s ~/.vim/vimrc ~/.vimrc &&\  
cd ~ && git clone https://github.com/chin33z/dotfiles.git ~/dotfiles &&\  
cd dotfiles && ./link.sh  
  
RUN updatedb  

