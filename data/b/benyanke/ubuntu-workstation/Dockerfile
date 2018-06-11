FROM phusion/baseimage:latest  
MAINTAINER Ben Yanke "ben@benyanke.com"  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install user tools, x2go, and kde  
RUN set -x \  
&& add-apt-repository ppa:x2go/stable -y \  
&& add-apt-repository ppa:libreoffice/libreoffice-6-0 -y \  
&& add-apt-repository ppa:remmina-ppa-team/remmina-next -y \  
&& add-apt-repository universe -y \  
&& apt-get update -y \  
&& apt-get install -y \  
sudo \  
pass \  
nano \  
git \  
htop \  
vim \  
zip \  
unzip \  
curl \  
screen \  
libreoffice \  
remmina \  
remmina-plugin-rdp \  
scribus \  
iputils-ping \  
mysql-workbench \  
pdftk \  
gimp \  
inkscape \  
traceroute \  
nfs-common \  
cifs-utils \  
httpie \  
fping \  
golang-go \  
npm \  
virtualenv \  
zip \  
unzip \  
python-pip \  
lynx \  
x2goserver \  
x2goserver-xsession \  
kubuntu-desktop \  
&& rm -rf /var/lib/apt/lists/*  
  
# Snappy - not fully working but leaving in comments for later  
# APT: fuse snapd snap-confine squashfuse \  
# RUN systemctl enable snapd  
# Enable SSH  
RUN rm -f /etc/service/sshd/down ; /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Configure default user  
RUN adduser --gecos "Ubuntu User" \--disabled-password ubuntu && echo
"ubuntu:ubuntu" | chpasswd && usermod -aG sudo ubuntu  
  
# Setup hostname for terminal  
RUN echo "ubuntu-workstation" > /etc/hostname  
  
# Clean up when done  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Expose port 22 for SSH  
EXPOSE 22  

