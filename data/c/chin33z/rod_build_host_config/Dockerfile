#FROM ubuntu:14.04  
FROM debian:jessie  
  
MAINTAINER David Hu <chin33z@gmail.com>  
  
# command-t: ruby ruby-dev  
RUN \  
apt-get update && \  
apt-get install -y gcc build-essential libtool-bin nfs-common gettext ncdu git
jq man wget screen pv xz-utils unzip vim-nox openssh-server \  
sudo make cmake pkg-config flex mtd-utils u-boot-tools texinfo bison gawk bc
automake scons net-tools cpio rpm2cpio openjdk-7-jre nasm \  
libglib2.0-dev libglib2.0-bin transfig libncurses5-dev libmysqlclient-dev
python-dev ruby ruby-dev && \  
rm -rf /var/lib/apt/lists/* &&\  
apt-get clean -yq  
  
RUN sed -i '/env_reset/d;/secure_path/d' /etc/sudoers  
  
CMD ["/usr/sbin/sshd", "-D"]  
  
ENV HOME /root  
WORKDIR /root  
  
RUN \  
mkdir -p /opt/cross-project/x86/sys-root/bin &&\  
ln -sf /usr/bin/openssl /opt/cross-project/x86/sys-root/bin/openssl  
  
# 1. git clone the vim setting  
# 2. git clone the env setting  
RUN \  
rm -fr ~/.vim ~/.vimrc &&\  
cd ~ && git clone https://github.com/chin33z/dotvim.git ~/.vim &&\  
cd ~/.vim/bundle/command-t/ruby/command-t && ruby extconf.rb && make &&\  
ln -s ~/.vim/vimrc ~/.vimrc &&\  
cd ~ && git clone https://github.com/chin33z/rod_build_dotfiles.git ~/dotfiles
&&\  
cd dotfiles && ./link.sh  

