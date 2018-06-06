#FROM ubuntu:14.04  
FROM debian:jessie  
  
MAINTAINER David Hu <chin33z@gmail.com>  
  
RUN \  
apt-get update && \  
apt-get install -y gcc build-essential git screen xz-utils unzip vim-nox
openssh-server \  
make flex bison gawk bc texinfo pkg-config libtool-bin gettext zlib1g-dev && \  
rm -rf /var/lib/apt/lists/* &&\  
apt-get clean -yq  
  
# setup ssh login  
RUN \  
mkdir /var/run/sshd &&\  
echo 'root:root123' | chpasswd &&\  
sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config &&\  
sed -i 's/Port 22/Port 44444/g' /etc/ssh/sshd_config  
  
EXPOSE 44444  
CMD ["/usr/sbin/sshd", "-D"]  
  
ENV HOME /root  
WORKDIR /root  
  
# 1. git clone the vim setting  
# 2. git clone the env setting  
RUN \  
cd ~ && rm -fr .vim &&\  
git clone https://github.com/chin33z/dotvim.git ~/.vim &&\  
rm -fr ~/.vimrc &&\  
ln -s ~/.vim/vimrc ~/.vimrc &&\  
git clone https://github.com/chin33z/build_dotfiles.git ~/dotfiles &&\  
cd dotfiles && ./link.sh  

