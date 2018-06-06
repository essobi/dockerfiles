FROM debian:jessie  
  
MAINTAINER David Hu <chin33z@gmail.com>  
  
# Host package neeeded  
RUN \  
apt-get update && \  
apt-get install -y man vim-nox cscope exuberant-ctags silversearcher-ag screen
ncdu pax-utils dtrx libncurses5-dev bc gdb\  
git tar python nasm uuid-dev iasl subversion patchutils lzop parted locales\  
gawk wget diffstat unzip texinfo gcc-multilib build-essential chrpath socat
cpio pkg-config libsdl1.2-dev sudo iptables &&\  
rm -rf /var/lib/apt/lists/* &&\  
apt-get clean -yq  
  
RUN useradd -c 'YiHu user' -m -d /home/yihu -G sudo -s /bin/bash yihu  
RUN echo "yihu:yihu" | chpasswd  
  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen &&\  
echo 'LANG="en_US.UTF-8"'>/etc/default/locale &&\  
dpkg-reconfigure --frontend=noninteractive locales &&\  
update-locale LANG=en_US.UTF-8  
  
USER yihu  
ENV HOME /home/yihu  
  
# 1. git clone the vim setting  
# 2. git clone the env setting  
RUN \  
rm -fr ~/.vim ~/.vimrc &&\  
cd ~ && git clone https://github.com/chin33z/dotvim.git ~/.vim &&\  
ln -s ~/.vim/vimrc ~/.vimrc &&\  
cd ~ && git clone https://github.com/chin33z/dotfiles.git ~/dotfiles &&\  
cd dotfiles && ./link.sh  
  
# need .gitconfig, so we put it after the environment setting  
RUN cd ~ &&\  
wget
https://downloadmirror.intel.com/23197/eng/BSP_Sources_and_Docs_for_Intel_Quark_v1.2.1.zip
&&\  
dtrx -r BSP_Sources_and_Docs_for_Intel_Quark_v1.2.1.zip &&\  
mv
BSP_Sources_and_Docs_for_Intel_Quark_v1.2.1/Board_Support_Package_Intel_Quark_v1.2.1/meta-
clanton_v1.2.1 ~ &&\  
rm -fr BSP_Sources_and_Docs_for_Intel_Quark_* &&\  
cd meta-clanton_v1.2.1 &&\  
./setup.sh  
  
  
WORKDIR /home/yihu  

