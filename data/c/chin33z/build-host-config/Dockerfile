#FROM ubuntu:14.04  
FROM debian:jessie  
  
MAINTAINER David Hu <chin33z@gmail.com>  
  
# cscope exuberant-ctags silversearcher-ag strace  
RUN \  
apt-get update && \  
apt-get install -y gcc build-essential libtool-bin gettext ncdu git jq man
wget screen pv xz-utils unzip vim-nox openssh-server \  
sudo make cmake pkg-config flex mtd-utils u-boot-tools texinfo bison gawk bc
automake scons net-tools \  
libglib2.0-dev libglib2.0-bin transfig libncurses5-dev && \  
rm -rf /var/lib/apt/lists/* &&\  
apt-get clean -yq  
  
# setup ssh login  
#RUN \  
# mkdir /var/run/sshd &&\  
# echo 'root:root123' | chpasswd &&\  
# sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
#CMD ["/usr/sbin/sshd", "-D"]  
  
ENV HOME /root  
WORKDIR /root  
  
# compile/install Facebook watchman  
#RUN \  
# cd ~ &&\  
# git clone https://github.com/facebook/watchman.git &&\  
# cd watchman && ./autogen.sh && ./configure &&\  
# make && make install &&\  
# cd ~ && rm -fr watchman  
  
# 1\. git clone the vim setting  
# 2\. git clone the env setting  
RUN \  
cd ~ && rm -fr .vim &&\  
git clone https://github.com/chin33z/dotvim.git ~/.vim &&\  
rm -fr ~/.vimrc &&\  
ln -s ~/.vim/vimrc ~/.vimrc &&\  
git clone https://github.com/chin33z/build_dotfiles.git ~/dotfiles &&\  
cd dotfiles && ./link.sh  

