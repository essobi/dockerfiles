FROM ubuntu:12.04  
  
RUN apt-get update &&\  
apt-get install -y git-core subversion build-essential gcc-multilib \  
libncurses5-dev zlib1g-dev gawk flex gettext wget \  
unzip python sudo libssl-dev &&\  
apt-get clean &&\  
useradd -m openwrt &&\  
echo 'openwrt ALL=NOPASSWD: ALL' > /etc/sudoers.d/openwrt &&\  
sudo chmod 0440 /etc/sudoers.d/openwrt &&\  
sudo -iu openwrt git clone git://git.openwrt.org/14.07/openwrt.git &&\  
sudo -iu openwrt openwrt/scripts/feeds update  

