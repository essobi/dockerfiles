#ubuntu 14  
FROM phusion/baseimage:0.9.17  
  
RUN sed -i 's/archive.ubuntu.com/free.nchc.org.tw/g' /etc/apt/sources.list &&
\  
echo 'deb http://www.emdebian.org/debian/ squeeze main' >>
/etc/apt/sources.list && \  
apt-key update && apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install -y wget zsh git tmux vim python-dev zip unzip && \  
apt-get install -y mtd-utils gzip bzip2 tar arj lhasa p7zip p7zip-full
cabextract cramfsprogs cramfsswap squashfs-tools sleuthkit default-jdk lzop
srecord && \  
apt-get install -y python-pip python-lzma python-crypto && \  
apt-get install -y emdebian-archive-keyring && \  
apt-get install -y \--force-yes binutils-mips-linux-gnu binutils-mipsel-linux-
gnu binutils-arm-linux-gnueabi && \  
apt-get install -y qemu-user-static && \  
pip install -U pip==9.0.1 && \  
pip install nose coverage && \  
git clone https://github.com/devttys0/binwalk.git ~/binwalk && \  
git clone --recursive https://github.com/zet235/dotfiles.git ~/.dotfiles && \  
cd ~/binwalk && \  
sudo python setup.py install && \  
apt-get install zlib1g-dev liblzma-dev liblzo2-dev && \  
cd ~ && \  
git clone https://github.com/rampageX/firmware-mod-kit && \  
git clone https://github.com/devttys0/sasquatch && \  
cd ~/sasquatch && ./build.sh  

