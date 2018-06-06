FROM ubuntu:16.04  
  
RUN apt-get update &&\  
apt-get install -y sudo git-core subversion build-essential gcc-multilib \  
libssl-dev \  
libncurses5-dev zlib1g-dev gawk flex gettext wget unzip python &&\  
apt-get clean &&\  
useradd -m openwrt &&\  
echo 'openwrt ALL=NOPASSWD: ALL' > /etc/sudoers.d/openwrt &&\  
sudo -iu openwrt git clone https://github.com/openwrt/openwrt &&\  
sudo -iu openwrt openwrt/scripts/feeds update

